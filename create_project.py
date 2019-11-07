def create_project(path):
    import json
    import os

    
    config = json.dumps({
        'channel': 'master',     # hqml branch
        'commit': 'HEAD',
        'packages': ['core', 'controls'],
        'src': ['ui'],
        'entry': './ui/app.qml'
    }, indent=4)

    with open(path+'/hqmlconfig.json', 'w') as f:
        f.write(config)

    import subprocess

    toolchain_path = os.path.dirname(__file__)

    subprocess.call(['python3', '%s/qmlcore/build'%toolchain_path, '--boilerplate'], cwd=path)