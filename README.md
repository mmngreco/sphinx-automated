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

Ver carpeta `examples`, alli se encuentra el fichero `programmatically.py`
con un ejemplo de uso.

Concretamente hay que editar `programmatically.py`:

```python
import sphinx_automated as sa

# ============================================================================
# EDIT THIS
PRJ_DIR = "path"
PRJ_NAME = "pkg_name"
AUTHOR = "autor"
# ============================================================================

try:
    sa.remove_doc_structure.main(PRJ_DIR)
except:
    pass

sa.make_doc_structure.main(PRJ_DIR, PRJ_NAME, AUTHOR)
sa.customize_conf.main(PRJ_DIR)
sa.generate_rst.main(PRJ_DIR)
sa.process_templates.main(PRJ_DIR)
sa.update_index.main(PRJ_DIR)
sa.generate_html.main(PRJ_DIR)

```

Una vez editado solo hay que lanzar la siguiente linea:

```bash
python examples/programmatically.py
```

