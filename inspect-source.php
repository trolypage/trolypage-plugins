<?php
// Export source contracts without loading .env, booting Laravel or calling tools.
// Usage: php inspect-source.php D:/facebook-support-agent/trolypage
$sourceRoot = realpath($argv[1] ?? 'D:/facebook-support-agent/trolypage');
if (! $sourceRoot || ! is_file($sourceRoot.'/vendor/autoload.php')) {
    fwrite(STDERR, "Provide the local TrolyPage source root with vendor installed.\n");
    exit(1);
}
require $sourceRoot.'/vendor/autoload.php';
$container = new Illuminate\Container\Container;
Illuminate\Container\Container::setInstance($container);
$container->instance('config', new Illuminate\Config\Repository([]));
$container->instance('translator', new Illuminate\Translation\Translator(new Illuminate\Translation\ArrayLoader, 'en'));
Illuminate\Support\Facades\Facade::setFacadeApplication($container);
$result = ['provenance' => 'Local source schema inspection; no authenticated production calls', 'tools' => [], 'errors' => []];
foreach (App\Mcp\Servers\TrolyPageServer::MODULE_SERVERS as $module => $server) {
    foreach ($server::TOOLS as $class) {
        $tool = new $class;
        $name = $tool->name();
        try {
            $data = $tool->toArray();
        } catch (Throwable $error) {
            $data = ['name' => $name, 'description' => $tool->description(), 'annotations' => $tool->annotations()];
            $result['errors'][] = ['tool' => $name, 'error' => $error->getMessage()];
        }
        $data['module'] = $module;
        $data['source'] = str_replace('\\', '/', substr((new ReflectionClass($class))->getFileName(), strlen($sourceRoot) + 1));
        $result['tools'][$name] = $data;
    }
}
$tool = new App\Mcp\Tools\GetMcpActionTool;
$result['tools'][$tool->name()] = [...$tool->toArray(), 'module' => 'shared', 'source' => 'app/Mcp/Tools/GetMcpActionTool.php'];
$result['tools'] = array_values($result['tools']);
file_put_contents(__DIR__.'/evidence/local-tool-catalog.json', json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR)."\n");
echo json_encode(['tools' => count($result['tools']), 'schema_errors' => $result['errors']], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
