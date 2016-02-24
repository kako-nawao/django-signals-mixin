"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
__author__ = 'kako'

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='django_signals_mixin',

    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.2',

    description='Use Django signals (almost) like JavaScript events',
    long_description=long_description,
    url='https://github.com/kako-nawao/django-signals-mixin',
    author='Claudio Omar Melendrez Baeza',
    author_email='claudio.melendrez@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
    ],

    keywords='django signals events models',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'django'
    ],
    extras_require={},
    package_data={},

    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={},
)

