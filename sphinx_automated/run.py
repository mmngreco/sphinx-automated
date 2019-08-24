from pathlib import Path

from . import *

# ========================================================================
# EDIT THIS
PRJ_DIR = "/root/git/sphinx_automated"
PRJ_NAME = "pkg_name"
AUTHOR = "autor"
# =========================================================================

def main():

    PRJ_DIR = Path(PRJ_DIR)

    assert PRJ_DIR.exists(), "The PRJ_DIR is not a valid path."

    PRJ_DIR = str(PRJ_DIR)

    try:
        remove_doc_structure.main(PRJ_DIR)
    except:
        pass

    make_doc_structure.main(PRJ_DIR, PRJ_NAME, AUTHOR)
    customize_conf.main(PRJ_DIR)
    generate_rst.main(PRJ_DIR)
    process_templates.main(PRJ_DIR)
    update_index.main(PRJ_DIR)
    generate_html.main(PRJ_DIR)

if __name__ == "__main__":
    main()
