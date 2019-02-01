import sys
from pathlib import Path
from subprocess import Popen, PIPE

ARGS = sys.argv
PROJECT_DIR = ARGS[1]  # PROJECT DIRECTORY same level than setup.py
PROJECT_NAME = ARGS[2]  # PROJECT NAME like : numpy
AUTHOR = ARGS[3]  # AUTHOR NAME like : numpy-dev
SUFFIX = ARGS[4]  # SUFFIX like : .rst or .md
# PROJECT_DIR = ARGS[4]
# print(PROJECT, AUTHOR,  SUFFIX,  PROJECT_DIR, DOC_DIR)
# Make doc folder
# DOC_DIR = PROJECT_DIR / "docs"


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
    "{DOC_DIR}"
]

EXTENSIONS = ",".join(EXTENSION_LST)

PROJECT_DIR = Path(PROJECT_DIR).absolute().resolve()

fmt = dict(
    PROJECT_NAME=PROJECT_NAME,
    PROJECT_DIR=PROJECT_DIR,
    EXTENSIONS=EXTENSIONS,
    AUTHOR=AUTHOR,
    SUFFIX=SUFFIX,
    DOC_DIR=PROJECT_DIR / "docs"
)

try:
    fmt['DOC_DIR'].mkdir()
except FileExistsError:
    pass

CMD = " ".join(CMD_LST).format(**fmt)


def main(CMD):
    import pdb;pdb.set_trace()
    out = Popen(CMD, stdout=PIPE, stderr=PIPE, shell=True)
    return out


if __name__ == "__main__":
    main(CMD)

