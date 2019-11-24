import logging
import configparser

from pathlib import Path
from . import (
    customize_conf,
    generate_html,
    generate_rst,
    make_doc_structure,
    process_templates,
    remove_doc_structure,
    update_index,
    utils,
)

logging.basicConfig(level=logging.INFO)


def read_config_file(path=None):
    logging.info(f"{path}")
    config = configparser.ConfigParser()

    try:
        config.read(Path(path).absolute().expanduser())
    except:
        PRJ_DIR = input("Enter project dir: ")
        SRC_NAME = input("Enter a source folder name: ")
        PRJ_NAME = input("Enter a project name [%s]: " % SRC_NAME)
        AUTHOR = input("Enter author name: ")
        config["project"] = dict(
            PRJ_DIR=PRJ_DIR,
            SRC_NAME=SRC_NAME,
            PRJ_NAME=PRJ_NAME,
            AUTHOR=AUTHOR,
        )
    return config


def main(PRJ_DIR, SRC_NAME, PRJ_NAME, AUTHOR):
    PRJ_DIR = Path(PRJ_DIR)
    SRC_DIR = Path(PRJ_DIR) / SRC_NAME

    assert PRJ_DIR.exists(), f"The PRJ_DIR={PRJ_DIR} is not a valid path."
    assert PRJ_DIR.exists(), f"The SRC_DIR={SRC_DIR} is not a valid path."

    PRJ_DIR = str(PRJ_DIR)

    if clean:
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

    parser.add_argument(
        "-c",
        "--config-file",
        help="Path to config.ini file.",
        default="~/.sphinx_automated.conf",
    )
    parser.add_argument("--prj-dir")
    parser.add_argument("--src-name")
    parser.add_argument("--prj-name")
    parser.add_argument("--author")
    parser.add_argument(
        "--create-config-file",
        help="Create an example config file in the path passed.",
    )
    parser.add_argument(
        "--clean", help="Overwrites existing doc content.", default=False
    )

    args = parser.parse_args()

    if args.create_config_file is not None:
        utils.write_config(args.create_config_file)
    else:
        try:
            config = utils.read_config(args.config_file)
            PRJ_DIR = config["DEFAULT"]["prj_dir"]
            SRC_NAME = config["DEFAULT"]["src_dir"]
            PRJ_NAME = config["DEFAULT"]["prj_name"]
            AUTHOR = config["DEFAULT"]["author"]
        except KeyError:
            PRJ_DIR = args.prj_dir
            SRC_NAME = args.src_name
            PRJ_NAME = args.prj_name
            AUTHOR = args.author

        clean = args.clean
        main(PRJ_DIR, SRC_NAME, PRJ_NAME, AUTHOR, clean)
