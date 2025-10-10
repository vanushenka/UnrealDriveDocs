# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'UnrealDrive'
copyright = '2025, Ivan Zhukov'
author = 'Ivan Zhukov'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    #'logo_only': True,
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

html_logo = "logo_256x256.png"

#html_favicon = 'img/favicon.ico'

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/overrides.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

