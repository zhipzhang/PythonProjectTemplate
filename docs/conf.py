# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'example_package'
copyright = '2025, Zach Peng'
author = 'Zach Peng'
release = '0.0.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
# Let we can use markdown files
extensions = ['myst_parser', 'autoapi.extension', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

autoapi_dirs = ['../src']
autoapi_type = 'python'
html_theme = 'alabaster'
html_static_path = ['_static']
