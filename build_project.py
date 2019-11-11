import os, subprocess, json, sys
def check_exists(file):
    return os.path.isfile(file)

def build_project():
    if not check_exists('hqmlconfig.json'):
        print('hqmlconfig does not exist. run `hqml create .` first')
        exit(1)

    with open('hqmlconfig.json', 'r') as f:
        config = json.load(f)
    
    manifest = {}
    manifest['sources'] = config['src']

    with open('.manifest', 'w') as f:
        f.write(json.dumps(manifest))

    toolchain_path = os.path.dirname(__file__)
    subprocess.call([sys.executable, '%s/qmlcore/build'%toolchain_path])
    os.remove('.manifest')