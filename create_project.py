def create_project(path):
    import json
    import os
    import sys
    
    config = json.dumps({
        'channel': 'master',     # hqml branch
        'commit': 'HEAD',
        'packages': ['core', 'controls'],
        'src': ['ui'],
        'entry': './ui/app.qml'
    }, indent=4)

    with open(path+'/hqmlconfig.json', 'w') as f:
        f.write(config)

    os.makedirs(path+'/ui')

    with open(path+'/ui/app.qml', 'w') as f:
        f.write(
"""Rectangle {
anchors.fill: context;
color: "black";
}""")

    #import subprocess

    #toolchain_path = os.path.dirname(__file__)

    #subprocess.call([sys.executable, '%s/qmlcore/build'%toolchain_path, '--boilerplate'], cwd=path)