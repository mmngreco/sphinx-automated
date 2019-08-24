import sys
from pathlib import Path
from .utils import export_file, get_url, find_abs_modules

TMPL_DIR = Path(__file__).absolute().resolve().parents[0] / "templates"

def main(PRJ_DIR, SRC_NAME):
    if not isinstance(PRJ_DIR, Path):
        PRJ_DIR = Path(PRJ_DIR)
    PRJ_DIR = PRJ_DIR.absolute().resolve()
    MOD_DIR = PRJ_DIR / SRC_NAME
    SRC_DIR = PRJ_DIR / "docs" / "source"
    TAB = "   "
    JOIN_STR = "\n%s" % TAB

    sys.path.insert(0, MOD_DIR)
    PY_MODULES = find_abs_modules(MOD_DIR.name, str(MOD_DIR))
    # import pdb; pdb.set_trace()

    # templates
    api_fmt = dict(
        PARENT_MOD_NAME=PY_MODULES[0],
        PY_MODULES=JOIN_STR.join(PY_MODULES[1:])
    )
    export_file(TMPL_DIR, SRC_DIR, "api.rst", api_fmt)

    install_fmt = dict(
        PRJ_NAME=PRJ_DIR.name,
        URL=get_url(PRJ_DIR)
    )
    export_file(TMPL_DIR, SRC_DIR, "install.rst", install_fmt)
    export_file(TMPL_DIR, SRC_DIR, "quickstart.rst")




if __name__ == "__main__":
    args = sys.argv
    prj_dir_str = args[1]
    src_name_str = args[2]
    main(prj_dir_str, src_name_str)
