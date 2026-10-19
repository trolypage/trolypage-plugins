"""Inspect public page metadata only; no authenticated browser session or site changes."""
from html.parser import HTMLParser
from pathlib import Path
import json
import urllib.request

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.title=''; self.in_title=False; self.meta=[]; self.links=[]; self.headings=[]; self.heading=None; self.text=[]; self.schemas=[]; self.schema=None; self.images=[]; self.lang=None; self.anchors=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang')
        if tag=='title': self.in_title=True
        if tag=='meta' and ('name' in a or 'property' in a or 'charset' in a): self.meta.append(a)
        if tag=='link' and a.get('rel') in ['canonical','alternate']: self.links.append(a)
        if tag in ['h1','h2','h3']: self.heading={'tag':tag,'text':''}
        if tag=='script' and a.get('type')=='application/ld+json': self.schema=''
        if tag=='img': self.images.append({k:a.get(k) for k in ['src','alt','loading','width','height']})
        if tag=='a': self.anchors.append(a.get('href',''))
    def handle_data(self,s):
        if self.in_title:self.title+=s
        if self.heading is not None:self.heading['text']+=s
        if self.schema is not None:self.schema+=s
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if self.heading is not None and tag==self.heading['tag']:
            self.heading['text']=' '.join(self.heading['text'].split());self.headings.append(self.heading);self.heading=None
        if tag=='script' and self.schema is not None:
            try:self.schemas.append(json.loads(self.schema))
            except json.JSONDecodeError:self.schemas.append({'parse_error':True})
            self.schema=None

out={'checked_on':'2026-10-19','method':'Unauthenticated public HTTP read; browser navigation failed','pages':[]}
for url in ['https://trolypage.com/features','https://trolypage.com/vi/tinh-nang','https://trolypage.com/robots.txt','https://trolypage.com/sitemap.xml','https://trolypage.com/sitemap-pages.xml']:
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=30) as response:
            body=response.read().decode('utf-8','replace')
            item={'requested_url':url,'final_url':response.url,'status':response.status,'content_type':response.headers.get('Content-Type'),'x_robots_tag':response.headers.get('X-Robots-Tag')}
        if '/features' in url or '/vi/tinh-nang' in url:
            p=Page();p.feed(body)
            item.update({'title':p.title,'language':p.lang,'meta':p.meta,'links':p.links,'headings':p.headings,'structured_data':p.schemas,'image_count':len(p.images),'images_missing_alt':sum(i['alt'] is None for i in p.images),'images_empty_alt':sum(i['alt']=='' for i in p.images),'internal_link_destinations':sorted(set(a for a in p.anchors if a.startswith(('/', 'https://trolypage.com'))))})
        else:item['text']=body[:100000]
        out['pages'].append(item)
    except Exception as e:out['pages'].append({'requested_url':url,'error':str(e)})
Path(__file__).with_name('evidence').joinpath('features-seo.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for p in out['pages']:
    summary={k:v for k,v in p.items() if k not in ['structured_data','images','internal_link_destinations','text']}
    if 'structured_data' in p:summary['schema_types']=[s.get('@type',s.get('@graph')) for s in p['structured_data']]
    if 'text' in p:summary['text_preview']=p['text'][:2500]
    print(json.dumps(summary,ensure_ascii=False,indent=2))
