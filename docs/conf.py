project = 'Stockstir'
copyright = '2023, PatzEdi'
author = 'PatzEdi'

release = '2.0.0'
version = '2.0.0'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']



html_theme = 'sphinx_rtd_theme'


epub_show_urls = 'footnote'