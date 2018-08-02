# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='name-of-library',
    version='0.0.1',
    description=('short description of library'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/agilgur5/name-of-library',
    author='Anton Gilgur',
    license='Apache-2.0',
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',

        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
    ],
    keywords=('keywords go here'),
    # Use packages instead if many files / modules
    # https://docs.python.org/3/distutils/examples.html
    py_modules=['single-file-of-code'],
    python_requires='>=2.7, <4',
    project_urls={  # Optional
        'Source': 'https://github.com/agilgur5/name-of-library/',
        'Tracker': 'https://github.com/agilgur5/name-of-library', # noqa
    },
)
