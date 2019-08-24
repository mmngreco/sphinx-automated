from pathlib import Path

from . import *

# ========================================================================
# EDIT THIS
PRJ_DIR = "/Users/mmngreco/Documents/github/mmngreco/sphinx-automated"
SRC_NAME = "sphinx_automated"
PRJ_NAME = "pkg_name"
AUTHOR = "autor"
# =========================================================================


def main(PRJ_DIR=PRJ_DIR, SRC_NAME=SRC_NAME, PRJ_NAME=PRJ_NAME, AUTHOR=AUTHOR):
    PRJ_DIR = Path(PRJ_DIR)
    SRC_DIR = Path(PRJ_DIR) / SRC_NAME
    assert PRJ_DIR.exists(), f"The PRJ_DIR={PRJ_DIR} is not a valid path."
    assert PRJ_DIR.exists(), f"The SRC_DIR={SRC_DIR} is not a valid path."

    PRJ_DIR = str(PRJ_DIR)

    try:
        remove_doc_structure.main(PRJ_DIR)
    except:
        pass

    make_doc_structure.main(PRJ_DIR, PRJ_NAME, AUTHOR)
    customize_conf.main(PRJ_DIR)
    generate_rst.main(PRJ_DIR, SRC_NAME)
    process_templates.main(PRJ_DIR, SRC_NAME)
    update_index.main(PRJ_DIR)
    generate_html.main(PRJ_DIR, SRC_NAME)

if __name__ == "__main__":
    main()
