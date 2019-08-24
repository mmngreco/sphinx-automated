from . import customize_conf
from . import generate_rst
from . import generate_html
from . import make_doc_structure
from . import process_templates
from . import update_index
from . import utils
from . import remove_doc_structure

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
