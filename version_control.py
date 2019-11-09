def update():
    import subprocess, os
    toolchain_path = os.path.dirname(__file__)
    subprocess.call(['git', 'pull', '--recurse-submodules'], cwd=toolchain_path)