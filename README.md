Este proyecto no es mas que un conjunto de scripts python que ayudan a generar
una primera versión de la documentación, partiendo de solo tres datos: ruta del
proyecto, nombre visible del proyecto y nombre del autor. Siempre es posible
cambiar cualquier dato en el futuro.

El correcto uso de este proyecto está supeditado a tener un proyecto con la
estructura estándar de python.

```
pkg_a
├── pkg_a
│   ├── awesome.py
│   └── __init__.py
├── README.md
└── setup.py

```

Lo que hace `sphinx-automated` es lanzar el `sphinx-quickstart` con los
argumentos, modificar el `conf.py` y el modificar `index.rst` y  se añade el
fichero `api.rst` que es la API reference. Para ver mas detalles sobre esto ver
la carpeta `templates` que contiene los ficheros necesarios para esta tarea.

# Instalación

```bash
pip install git+git@github.com:mmngreco/sphinx-automated.git
```

# Uso

1. Concretamente hay que editar `run.py`:

    ```python
    from pathlib import Path

    from . import *

    # ========================================================================
    # EDIT THIS
    PRJ_DIR = "repos/sphinx-automated"
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

    ```

1. Una vez editado solo hay que lanzar la siguiente linea:

    ```bash
    python -m sphinx_automated.run
    ```

Una vez haya termiando tendremos una nueva carpeta en `PRJ_DIR`:


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
