import sys
from pathlib import Path

TMPL_DIR = Path(__file__).absolute().resolve().parent / "templates"

def main(PRJ_DIR):
    if not isinstance(PRJ_DIR, Path):
        PRJ_DIR = Path(PRJ_DIR)
    CONFPY_DIR = PRJ_DIR / "docs" / "source" / "conf.py"

    FILE_TO_APPEND = TMPL_DIR / "append_conf.py"

    with FILE_TO_APPEND.open("r") as f:
        CODE_TO_APPEND = f.readlines()

    with CONFPY_DIR.open("a") as f:
        f.writelines(CODE_TO_APPEND)


if __name__ == "__main__":
    args = sys.argv
    PRJ_DIR = Path(args[1]).absolute().resolve()
    main(PRJ_DIR)
