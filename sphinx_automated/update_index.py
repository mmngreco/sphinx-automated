import sys
from pathlib import Path


def main(PRJ_DIR):
    if not isinstance(PRJ_DIR, Path):
        PRJ_DIR = Path(PRJ_DIR)

    PRJ_DIR = PRJ_DIR.absolute().resolve()
    SRC_DIR = PRJ_DIR / "docs" / "source"
    index_file = SRC_DIR / "index.rst"

    INCLUDE = ["install.rst", "quickstart.rst", "api.rst"]  # files to include in the index file.

    INSERT_AT = 12
    TAB = "   "
    RST_LST = []

    with index_file.open("r") as f:
        index_lines = f.readlines()

    for rst_file in INCLUDE:
        RST_LST.append("{TAB}{NAME}\n".format(TAB=TAB, NAME=rst_file))

    # __import__('pdb').set_trace()

    with index_file.open("w") as f:
        new_index_lines = index_lines[:INSERT_AT].copy()
        new_index_lines.extend(RST_LST)
        new_index_lines.extend(index_lines[INSERT_AT:])
        f.writelines(new_index_lines)


if __name__ == "__main__":
    PROJECT_DIR = sys.argv[1]
    main(PROJECT_DIR)
