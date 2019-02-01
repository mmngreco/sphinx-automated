from pathlib import Path
import sys


def main(PRJ_DIR):
    if not isinstance(PRJ_DIR, Path):
        PRJ_DIR = Path(PRJ_DIR)
    CONFPY_DIR = PRJ_DIR / "docs" / "source" / "conf.py"

    # __import__('pdb').set_trace()

    FILE_TO_APPEND = Path(__file__).absolute().resolve().parents[1] / "templates" / "append_conf.py"

    with FILE_TO_APPEND.open("r") as f:
        CODE_TO_APPEND = f.readlines()

    # __import__('pdb').set_trace()

    with CONFPY_DIR.open("a") as f:
        f.writelines(CODE_TO_APPEND)


if __name__ == "__main__":
    args = sys.argv
    PRJ_DIR = Path(args[1]).absolute().resolve()
    main(PRJ_DIR)
