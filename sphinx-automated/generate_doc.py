from pathlib import Path
import webbrowser
from subprocess import Popen, PIPE
import sys


def main(args):
    PROJECT_DIR = args[1]
    PROJECT_DIR = Path(PROJECT_DIR).absolute().resolve()

    PKG_DIR = PROJECT_DIR / PROJECT_DIR.name
    SOURCE_DIR = PROJECT_DIR / "docs" / "source"

    RST_CMD = "sphinx-apidoc -M -T -f -e -o {SOURCE_DIR} {PKG_DIR}"

    fmt = dict(
        PKG_DIR=PKG_DIR,
        SOURCE_DIR=SOURCE_DIR,
        BUILD_DIR = SOURCE_DIR.parent / "build",
    )
    import pdb; pdb.set_trace()
    CMD = RST_CMD.format(**fmt)
    out = Popen(CMD, shell=True, stdout=PIPE, stderr=PIPE)

    std_out = out.stdout.readlines()
    print(std_out)

    std_err = out.stderr.readlines()
    print(std_err)
    HTML_CMD = "sphinx-build -M html {SOURCE_DIR} {BUILD_DIR}"
    CMD = HTML_CMD.format(**fmt)
    out = Popen(CMD, shell=True, stdout=PIPE, stderr=PIPE)

    std_out = out.stdout.readlines()
    print(std_out)

    std_err = out.stderr.readlines()
    print(std_err)
    webbrowser.open('file://%s' % (fmt['BUILD_DIR']/"html"/"index.html"))

if __name__ == "__main__":
    main(sys.argv)
