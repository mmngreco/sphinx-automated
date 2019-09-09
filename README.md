Useful collection of Python scripts to quickly put up the `Sphinx` documentation skeleton. 
Three basic inputs are required:
1. Project path
1. Visible name of the project
1. Author name

It is always possible to change any of the previous in the future. 

The project folder must have the following Python standard structure:  

```
pkg_a
├── pkg_a
│   ├── awesome.py
│   └── __init__.py
├── README.md
└── setup.py
```

`sphinx-automated` will launch `sphinx-quickstart` with the user arguments,
modify accordingly the `conf.py` and `index.rst` files. The file `api.rst` is 
created too. To get a more detailed description, see the folder `templates`, where
the necessary files are stored. 

# Installation

The installation will collect the `Sphinx` dependencies.
    
1. Direct install with pip from Github:

    ```bash
    pip install git+git@github.com:mmngreco/sphinx-automated.git
    ```

# Quickstart

1. Edit the `run.py` script:

    ```python
    from pathlib import Path

    from . import *

    # ========================================================================
    # EDIT THIS
    PRJ_DIR = "repos/sphinx-automated"
    SRC_NAME = "sphinx_automated"
    PRJ_NAME = "pkg_name"
    AUTHOR = "author"
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

    ```

1. Launch the following line in the terminal:

    ```bash
    python -m sphinx_automated.run
    ```
    
Once the process is over, a new folder will have appeared in `PRJ_DIR`:

```
pkg_a  (PRJ_DIR)
├── pkg_a  (SRC_NAME)
│   ├── awesome.py
│   └── __init__.py
├── docs  (New folder!)
│   ├── build
│   │  └── html (index.html!)
│   └── source
├── README.md
└── setup.py

```
