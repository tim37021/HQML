def update():
    import subprocess, os
    toolchain_path = os.path.dirname(__file__)

    subprocess.call(['git', 'pull'], cwd=toolchain_path)
    subprocess.call(['git', 'submodule', 'sync'], cwd=toolchain_path)
    subprocess.call(['git', 'submodule', 'update', '--init', '--recursive', '--remote'], cwd=toolchain_path)
