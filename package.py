"""Rebuild archives from reviewed package files without overwriting source or review notes."""
from pathlib import Path
import hashlib
import json
import re
import sys
import tempfile
import html
import zipfile
from PIL import Image
import yaml
import markdown

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(Path(tempfile.gettempdir()) / 'trolypage-plugin-schema-validator'))
try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

checks=[]
def check(name, passed, detail=''):
    checks.append({'check':name,'passed':bool(passed),'detail':detail})

archives=[]
for target in ['openai','claude']:
    package=ROOT/'packages'/target/'trolypage-mcp'
    manifest_path=package/('plugin.json' if target=='openai' else '.claude-plugin/plugin.json')
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    version=manifest['version']
    check(target+' semantic version',bool(re.fullmatch(r'\d+\.\d+\.\d+(?:-[A-Za-z0-9.-]+)?',version)))
    check(target+' name preserved',manifest['name']=='trolypage-mcp')
    for path in package.rglob('*.json'):
        json.loads(path.read_text(encoding='utf-8'))
    for path in package.rglob('*.yaml'):
        yaml.safe_load(path.read_text(encoding='utf-8'))
    skill_paths=list((package/'skills').glob('*/SKILL.md'))
    check(target+' skills present',len(skill_paths)==(9 if target=='openai' else 8),str(len(skill_paths)))
    for path in skill_paths:
        text=path.read_text(encoding='utf-8')
        front=yaml.safe_load(text.split('---',2)[1])
        check(target+' skill '+path.parent.name,front.get('name')==path.parent.name and isinstance(front.get('description'),str))
        for link in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in link or link.startswith('#'):
                continue
            resolved=(path.parent/link.split('#')[0]).resolve()
            check(target+' contained reference '+path.parent.name+'/'+link, resolved.is_relative_to(package.resolve()) and resolved.exists())
    if target=='openai':
        ext=manifest['extensions']['com.openai'];interface=ext['interface']
        check('Portable root excludes legacy fields',not set(['apps','skills','mcpServers','interface']).intersection(manifest))
        check('OpenAI contains no apps declaration','apps' not in ext)
        check('Listing title/subtitle/name limits',0<len(interface['displayName'])<=30 and 0<len(interface['shortDescription'])<=30 and 0<len(interface['developerName'])<=80)
        check('Long description limit',0<len(interface['longDescription'])<=4000)
        prompts=interface['defaultPrompt']
        check('Starter prompt limits',isinstance(prompts,list) and 0<len(prompts)<=3 and all(0<len(p)<=128 and '\n' not in p and '@' not in p for p in prompts) and len(set(prompts))==len(prompts))
        for field in ['websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL']:
            url=interface[field]
            check('URL shape '+field,url.startswith('https://') and len(url)<=1024 and '@' not in url)
        for field in ['logo','composerIcon']:
            path=(package/interface[field]).resolve()
            check('Contained '+field,path.is_relative_to(package.resolve()) and path.is_file())
            if path.is_file():
                with Image.open(path) as im:
                    minimum=256 if field=='logo' else 48
                    check('PNG asset '+field,im.format=='PNG' and im.width==im.height and im.width>=minimum and path.stat().st_size<=5*1024*1024)
        review=ext['review'];cases=review['test_cases']
        check('5 positive / 3 negative',len(cases['positive'])==5 and len(cases['negative'])==3)
        check('Commerce declared',review.get('commerce') is True and bool(review.get('commerce_description')))
        check('Countries all allowed by platform',ext['publication']['countries']==[])
        if Draft202012Validator:
            for filename,schema_name in [('plugin.json','plugin'),('mcp.json','mcp')]:
                schema=json.loads((ROOT/'evidence/schemas'/f'{schema_name}.schema.json').read_text(encoding='utf-8'))
                Draft202012Validator.check_schema(schema)
                data=json.loads((package/filename).read_text(encoding='utf-8'))
                errors=sorted(Draft202012Validator(schema).iter_errors(data),key=lambda e:str(list(e.path)))
                check('Agent Plugins 1.0 schema: '+filename,not errors,'; '.join(str(list(e.path))+': '+e.message for e in errors))
    archive=ROOT/'archives'/f'{target}-trolypage-mcp-{version}-DRAFT.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for path in sorted(package.rglob('*')):
            if path.is_file():
                assert not path.is_symlink()
                z.write(path,path.relative_to(package).as_posix())
    with zipfile.ZipFile(archive) as z:
        check(target+' ZIP integrity',z.testzip() is None)
        check(target+' no private bindings/hooks/system files',not any(n in ['.app.json','.env'] or n.startswith('hooks/') or Path(n).name in ['.DS_Store','Thumbs.db','desktop.ini'] for n in z.namelist()))
        check(target+' secret pattern scan',not any(re.search(rb'(?:sk-(?:proj-)?[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|Bearer\s+[A-Za-z0-9._-]{20,}|BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY)',z.read(n)) for n in z.namelist()))
        check(target+' no files over 5MiB',all(n.file_size<=5*1024*1024 for n in z.infolist()))
    archives.append(archive)

report=json.loads((ROOT/'validation-report.json').read_text(encoding='utf-8'))
report['local_checks']=checks
report['local_checks_passed']=all(c['passed'] for c in checks)
report['agent_plugins_1_schema_validation']='Passed' if Draft202012Validator and all(c['passed'] for c in checks if c['check'].startswith('Agent Plugins')) else 'Not available or failed'
report['validation_scope']='Local format, references, asset, ZIP and secret-pattern checks; Agent Plugins core schemas when installed. OpenAI extension rules are partly custom-checked. Platform portal scans, Claude official validation and live behavior tests remain pending.'
(ROOT/'validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'archives/SHA256SUMS.txt').write_text('\n'.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name for p in archives)+'\n',encoding='utf-8')
# Refresh only the rendered projection; never regenerate or overwrite reviewed notes.
page_path=ROOT/'review.html'
if page_path.exists():
    page=page_path.read_text(encoding='utf-8')
    start=page.find('<section id="')
    end=page.rfind('</section>')+len('</section>')
    if start>=0 and end>start:
        sections=[]
        for path in sorted((ROOT/'review').glob('0*.md')):
            content=markdown.markdown(path.read_text(encoding='utf-8'),extensions=['tables','fenced_code'])
            sections.append(f'<section id="{path.stem}"><a class="file" href="review/{path.name}">Open Markdown file</a>{content}</section>')
        page_path.write_text(page[:start]+''.join(sections)+page[end:],encoding='utf-8')
        page=page_path.read_text(encoding='utf-8')
        navigation=''.join(f'<a href="#{path.stem}">{html.escape(path.stem)}</a>' for path in sorted((ROOT/'review').glob('0*.md')))
        page=re.sub(r'<nav>.*?</nav>','<nav>'+navigation+'</nav>',page,count=1,flags=re.S)
        page_path.write_text(page,encoding='utf-8')
print(json.dumps({'passed':report['local_checks_passed'],'checks':len(checks),'agent_plugins_schema':report['agent_plugins_1_schema_validation'],'failures':[c for c in checks if not c['passed']]},ensure_ascii=False,indent=2))
sys.exit(0 if report['local_checks_passed'] else 1)
