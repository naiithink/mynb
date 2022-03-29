# -*- coding: utf-8 -*-

project = "mynb"
copyright = "2022, naiithink"
author = "naiithink"
version = "0.1.0-alpha"


templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
extensions = [
    "nbsphinx",
    "sphinx.ext.mathjax",
    "myst_parser"
]

# nbsphinx_execute = "never"

html_static_path = ["_static"]
html_theme = "furo"
# html_theme_options = {
#     "display_version": False,
#     "sticky_navigation": False
# }

source_suffix = [
    ".rst",
    ".txt",
    ".md",
]
source_parsers = {
    ".md": "recommonmark.parser.CommonMarkParser"
}