from pathlib import Path
import sys

CODE_TO_APPEND = """
# <<<  custom ----------------------------------------------------------------

import sys
import sphinx_rtd_theme
from pathlib import Path
sys.path.insert(0, Path(__file__).parent)
autosummary_generate = True
html_theme = 'sphinx_rtd_theme'
napoleon_use_param = False  # this does not seem to make much difference
napoleon_use_rtype = False  # show argument name and return type in the same line
napoleon_numpy_docstring = True  # the only allowed format for docstring is numpy style
napoleon_google_docstring = False  # google-style docstrings are not allowed
# napoleon_custom_sections = ['Characteristics', 'Indicators']
autodoc_member_order = 'alphabetical' # {'alphabetical','groupwise','bysource'}

# ---------------------------------------------------------------- custom >>>
"""


def main(pth, code):
    with pth.open("a") as f:
        f.write(code)


if __name__ == "__main__":
    args = sys.argv
    CONFPY_DIR = Path(args[1]).absolute() / "docs" / "source" / "conf.py"
    main(CONFPY_DIR, CODE_TO_APPEND)
