from pathlib import Path
import webbrowser
import sys
from .utils import execute

def main(PRJ_DIR, SRC_NAME):
    if not isinstance(PRJ_DIR, Path):
        PRJ_DIR = Path(PRJ_DIR)
    PROJECT_DIR = PRJ_DIR.absolute().resolve()

    PKG_DIR = PROJECT_DIR / SRC_NAME
    SOURCE_DIR = PROJECT_DIR / "docs" / "source"

    fmt = dict(
        PKG_DIR=PKG_DIR,
        SOURCE_DIR=SOURCE_DIR,
        BUILD_DIR = SOURCE_DIR.parent / "build",
    )

    # import pdb; pdb.set_trace()

    HTML_CMD = "sphinx-build -M html \"{SOURCE_DIR}\" \"{BUILD_DIR}\""
    CMD = HTML_CMD.format(**fmt)
    execute(CMD)
    webbrowser.open('file://%s' % (fmt['BUILD_DIR']/"html"/"index.html"))




if __name__ == "__main__":
    PROJECT_DIR = sys.argv[1]
    SRC_NAME = sys.argv[2]
    main(PROJECT_DIR, SRC_NAME)
