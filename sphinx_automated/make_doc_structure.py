import sys
from pathlib import Path
from .utils import execute

EXTENSION_LST = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax"
]


CMD_LST = [
        "sphinx-quickstart",
        "--quiet",
        "--sep",
        "--project='{PROJECT_NAME}'",
        "--author='{AUTHOR}'",
        "--suffix='{SUFFIX}'",
        "--extensions={EXTENSIONS}",
        "--makefile",
        "--batchfile",
        "\"{DOC_DIR}\""
    ]

EXTENSIONS = ",".join(EXTENSION_LST)

def main(PROJECT_DIR, PROJECT_NAME, AUTHOR):
    if not isinstance(PROJECT_DIR, Path):
        PROJECT_DIR = Path(PROJECT_DIR)

    PROJECT_DIR = PROJECT_DIR.absolute().resolve()

    fmt = dict(
        PROJECT_NAME=PROJECT_NAME,
        PROJECT_DIR=PROJECT_DIR,
        EXTENSIONS=EXTENSIONS,
        AUTHOR=AUTHOR,
        SUFFIX=".rst",
        DOC_DIR=PROJECT_DIR / "docs"
    )

    try:
        fmt['DOC_DIR'].mkdir()
    except FileExistsError:
        pass

    CMD = " ".join(CMD_LST).format(**fmt)
    execute(CMD)



if __name__ == "__main__":
    ARGS = sys.argv
    PROJECT_DIR = ARGS[1]  # PROJECT DIRECTORY same level than setup.py
    PROJECT_NAME = ARGS[2]  # PROJECT NAME like : numpy
    AUTHOR = ARGS[3]  # AUTHOR NAME like : numpy-dev
    main(PROJECT_DIR, PROJECT_NAME, AUTHOR)

