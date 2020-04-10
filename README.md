Useful collection of Python scripts to quickly put up the `Sphinx`
documentation skeleton.

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
created too. To get a more detailed description, see the folder `templates`,
where the necessary files are stored.

# Installation

The installation will collect the `Sphinx` dependencies.

1. Direct install with pip from Github:

    ```bash
    pip install git+git@github.com:mmngreco/sphinx-automated.git
    ```

# Quickstart

1. Create a `project.ini` followin this templete:
    ```
    [project]
    PRJ_DIR="/Users/mmngreco/Documents/github/mmngreco/sphinx-automated"
    SRC_NAME="sphinx_automated"
    PRJ_NAME="pkg_name"
    AUTHOR="autor"
    ```
1. Run `main.py -f project.ini`.

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
