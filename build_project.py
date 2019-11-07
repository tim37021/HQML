import os, subprocess, json
def check_exists(file):
    return os.path.isfile(file)

def build_project():
    if not check_exists('hqmlconfig.json'):
        print('hqmlconfig does not exist. run `hqml create .` first')
        exit(1)

    with open('hqmlconfig.json', 'r') as f:
        config = json.load(f)
    
    with open('.manifest', 'r') as f:
        manifest = json.load(f)

    manifest['sources'] = config['src']

    with open('.manifest', 'w') as f:
        f.write(json.dumps(manifest))


    toolchain_path = os.path.dirname(__file__)

    subprocess.call(['python3', '%s/qmlcore/build'%toolchain_path])