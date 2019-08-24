from pathlib import Path
import webbrowser
from subprocess import Popen, PIPE
import sys
from .utils import execute

def main(PRJ_DIR, SRC_NAME):
    if not isinstance(PRJ_DIR, Path):
        PRJ_DIR = Path(PRJ_DIR)

    PROJECT_DIR = PRJ_DIR.absolute().resolve()

    PKG_DIR = PROJECT_DIR / SRC_NAME
    SOURCE_DIR = PROJECT_DIR / "docs" / "source"

    RST_CMD = "sphinx-apidoc -M -T -f -e -o \"{SOURCE_DIR}\" \"{PKG_DIR}\""

    fmt = dict(
        PKG_DIR=PKG_DIR,
        SOURCE_DIR=SOURCE_DIR,
        BUILD_DIR = SOURCE_DIR.parent / "build",
    )

    CMD = RST_CMD.format(**fmt)
    out = execute(CMD)


if __name__ == "__main__":
    PROJECT_DIR = sys.argv[1]
    main(PROJECT_DIR)
