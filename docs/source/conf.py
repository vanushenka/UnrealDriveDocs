# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MetaRoad'
copyright = '2026, Ivan Zhukov'
author = 'Ivan Zhukov'

release = '3.2'
version = '3.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinxcontrib.mermaid',
]

# Consistent, doc-friendly look for all Mermaid diagrams (grayscale, renders client-side).
mermaid_light_theme = 'neutral'
# securityLevel 'loose' lets node labels use inline HTML (bigger/bolder title + smaller/dimmer subtitle).
# Keep startOnLoad False — the extension runs mermaid itself.
mermaid_init_config = {"startOnLoad": False, "securityLevel": "loose"}

# Auto-generate slug anchors for headings (h1..h4) so in-page cross-links like
# `[text](/section/Page.md#some-heading)` resolve. Without this, MyST does not emit
# implicit heading targets and every #anchor cross-reference warns.
myst_heading_anchors = 4

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    #'display_version': True,
    #'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    ### Toc options
    'collapse_navigation': False,
    #'sticky_navigation': False,
    #'navigation_depth': 3,
    #'includehidden': True,
    #'titles_only': False
    'analytics_id': 'UA-283663249-1',  #  Provided by Google in your dashboard
}

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

html_logo = "_static/logo_small.png"

#html_favicon = 'img/favicon.ico'

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/overrides.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

