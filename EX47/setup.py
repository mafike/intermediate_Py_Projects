try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project.',
    'author': 'Mafike.',
    'url': 'URL to get it at.',
    'download_url': 'where to download it.',
    'author_email': 'mafgenes@yahoo.com.',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'projectname'
}
setup(**config)
