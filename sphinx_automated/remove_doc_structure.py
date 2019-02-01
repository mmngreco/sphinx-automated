import sys
from pathlib import Path
from .utils import delete_folder

def main(PRJ_DIR):
    if not isinstance(PRJ_DIR, Path):
        PRJ_DIR = Path(PRJ_DIR)
    PRJ_DIR = Path(PRJ_DIR).absolute().resolve()
    DOCS_DIR = PRJ_DIR / "docs"
    delete_folder(DOCS_DIR)


if __name__ == "__main__":
    ARGS = sys.argv
    PRJ_DIR = ARGS[1]  # PROJECT DIRECTORY same level than setup.py
    main(PRJ_DIR)

