# -*- coding: utf-8 -*-

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "myst_parser",
    "nbsphinx"
]

# templates_path = ["assets/_templates"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown"
}
source_parsers = {
    ".md": "recommonmark.parser.CommonMarkParser"
}
nbsphinx_execute = "never"
# nbsphinx_allow_errors = True

root_doc = "index"

project = "mynb"
copyright = "2022, naiithink"
author = "naiithink"
version = "dne"

language = None

exclude_patterns = ["_build", "**.ipynb_checkpoints"]

pygments_style = "vs"

todo_include_todos = False

html_theme = "furo"
# html_theme_options = {
#     "display_version": False,
#     "sticky_navigation": False
# }
# html_theme_path = []
html_title = "mynb"
html_logo = None
html_favicon = None
# html_static_path = [
#     "assets/_static",
#     "assets/_static/css",
#     "assets/_static/boilerplates"
# ]
# html_css_files = ["mystyle.css"]
# html_js_files = []
# html_search_language = "en"
# html_search_options = {}

# rst_prolog = """"""
rst_epilog = """
.. |nbsp|           unicode:: U+0020 .. space
.. |tab|            unicode:: U+0009 .. tab
.. |BDG-TEMPLATE|   replace:: :bdg-secondary:`Template`
"""

# def setup(app):
#     app.add_css_file("mystyle.css")