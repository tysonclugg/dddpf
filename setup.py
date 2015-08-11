#!/usr/bin/env python
"""Django DDP Presentation Project."""
import os.path
from setuptools import setup, find_packages

setup(
    name='dddppp',
    version='0.0.1',
    description=__doc__,
    long_description=open('README.rst').read(),
    author='Tyson Clugg',
    author_email='tyson@clugg.net',
    url='https://github.com/tysonclugg/dddppp',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.8.3',
        'django-ddp>=0.10.0',
        'django-mptt>=0.7.4',
        'django-mptt-admin>=0.2.1',
        'django-orderable>=3.1.0',
        'pybars3>=0.9.1',
        'whitenoise>=2.0',
    ],
    scripts=[
        'manage.py',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
