from pathlib import Path

from . import *


def main(PRJ_DIR, SRC_NAME, PRJ_NAME, AUTHOR):
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
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--config-file", help="Path to config.ini file.",
                        default="~/.sphinx_automated.conf")

    parser.add_argument("--prj-dir")
    parser.add_argument("--src-name")
    parser.add_argument("--prj-name")
    parser.add_argument("--author")

    args = parser.parse_args()

    try:
        config = utils.read_config(args.config_file)
        PRJ_DIR = config["DEFAULT"]["prj_dir"]
        SRC_NAME = config["DEFAULT"]["src_name"]
        PRJ_NAME = config["DEFAULT"]["prj_name"]
        AUTHOR = config["DEFAULT"]["author"]
    except KeyError:
        PRJ_DIR = args.prj_dir
        SRC_NAME = args.src_name
        PRJ_NAME = args.prj_name
        AUTHOR = args.author
    __import__('pdb').set_trace()
    main(PRJ_DIR, SRC_NAME, PRJ_NAME, AUTHOR)
