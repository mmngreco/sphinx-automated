from pathlib import Path
from shutil import rmtree
import webbrowser
from subprocess import Popen, PIPE, STDOUT, CalledProcessError
import sys


def execute(cmd):
    def _exec(cmd):
        popen = Popen(
                args=cmd,
                stdout=PIPE,
                stderr=PIPE,
                universal_newlines=True,
                shell=True
            )

        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line
        popen.stdout.close()
        return_code = popen.wait()

        if return_code:
            raise CalledProcessError(return_code, cmd)
    for str_line in _exec(cmd):
        print(str_line, end='')


def export_file(from_dir, to_dir, name, fmt_kwargs=None):
    if fmt_kwargs is None:
        fmt_kwargs = dict()

    from_file = from_dir / name
    with from_file.open("r") as f:
        from_str = f.read()

    to_file = to_dir / name
    with to_file.open("w") as f:
        f.write(from_str.format(**fmt_kwargs))


def get_url(dir):
    CMD = "git config --get remote.origin.url"
    out = Popen(CMD, shell=True, cwd=dir, stderr=PIPE, stdout=PIPE)
    # execute(CMD)
    return out.stdout.read().decode("utf-8").strip()


def find_abs_modules(MOD_NAME, MOD_DIR):
    import importlib
    import pkgutil
    path_list = [MOD_NAME]
    spec_list = []

    for importer, modname, ispkg in pkgutil.walk_packages([MOD_DIR]):
        import_path = "{modname}".format(MOD_NAME=MOD_NAME, modname=modname)

        if ispkg:
            spec = pkgutil._get_spec(importer, modname)
            importlib._bootstrap._load(spec)
            spec_list.append(spec)
        else:
            if modname.startswith("_"):
                # avoid private modules
                continue
            path_list.append(import_path)
    for spec in spec_list:
        del sys.modules[spec.name]

    return path_list


def delete_folder(pth) :
    for sub in pth.iterdir():
        if sub.is_dir():
            delete_folder(sub)
        else:
            sub.unlink()
    pth.rmdir()
