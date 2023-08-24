try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My Project',
    'author': 'jack',
    'url': 'url not set yet',
    'download_url': 'not set yet',
    'author_email':'not set yet',
    'version': '0.1',
    'install_requires':['nose'],
    'packages':['find'],
    'scripts':[],
    'name':'myProject'
}

setup(**config)
