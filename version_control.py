def update():
    import subprocess, os
    toolchain_path = os.path.dirname(__file__)
    subprocess.call(['git', 'pull'], cwd=toolchain_path)