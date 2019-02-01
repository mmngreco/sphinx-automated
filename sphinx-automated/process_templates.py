import sys
from pathlib import Path


def main(prj_dir_str):
    PRJ_DIR = Path(prj_dir_str).absolute().resolve()
    MOD_DIR = PRJ_DIR / PRJ_DIR.name
    TAB = "   "
    JOIN_STR = "\n%s" % TAB

    sys.path.insert(0, MOD_DIR)
    # exec("import %s as PKG" % MOD_DIR.name)
    PY_MODULES = find_abs_modules(MOD_DIR.name, str(MOD_DIR))
    import pdb; pdb.set_trace()
    print("done")


def path_import(name, path):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


def find_abs_modules(MOD_NAME, MOD_DIR):
    import importlib
    import pkgutil
    path_list = []
    spec_list = []

    for importer, modname, ispkg in pkgutil.walk_packages([MOD_DIR]):
        import_path = f"{MOD_NAME}.{modname}"

        if ispkg:
            spec = pkgutil._get_spec(importer, modname)
            importlib._bootstrap._load(spec)
            spec_list.append(spec)
        else:
            path_list.append(import_path)

    for spec in spec_list:
        del sys.modules[spec.name]

    return path_list


if __name__ == "__main__":
    args = sys.argv
    prj_dir_str = args[1]
    main(prj_dir_str)
