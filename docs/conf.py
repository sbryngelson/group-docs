# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Computational Physics @ GT Group Documentation'
copyright = '2023, Computational Physics @ GT'
author = 'Computational Physics @ GT'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx_markdown_tables',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Add custom CSS file
html_css_files = [
    'custom.css',
]

# -- MyST Parser configuration -----------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]

# Enable anchor links for headers
myst_heading_anchors = 3

# Source file extensions
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master document
master_doc = 'index'

# Don't include source links
html_show_sourcelink = False

# ReadTheDocs specific settings
html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False,
    'collapse_navigation': False,
}

# Use index.html as default suffix
html_file_suffix = None

# Ensure .md files are processed correctly
source_parsers = {
    '.md': 'myst_parser.sphinx_',
}

# Configure URLs
html_baseurl = '/'
html_secnumber_suffix = '. '

# Configure MyST parser for links
myst_url_schemes = ('http', 'https', 'mailto', 'ftp', '')
myst_ref_domains = [] 