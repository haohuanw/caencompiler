#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(fname):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), fname)
    if os.path.exists(path):
        return open(path).read
    return ""
# Package meta data
NAME = "caencompiler"
VERSION = "1.0" 
DESCRIPTION = "A easy way for code on UMich CAEN Environment"
AUTHOR = "Haohuan Wang"
AUTHOR_EMAIL = "haohuanw@umich.edu"
URL = "https://github.com/haohuanw/caencompiler"
KEYWORDS = ""
CLASSIFIERS = []

# Package contents
MODULES = []
PACKAGES = find_packages(exclude=["tests.*", "tests", "test.*", "test"])
ENTRY_POINTS = """
[console_scripts]
caenpp = caencompiler:main
"""

# Dependencies
INSTALL_REQUIRES = ['Fabric', 'PyYAML', 'docopt']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    keywords=KEYWORDS,
    classifiers = CLASSIFIERS,
    py_modules=MODULES,
    packages=PACKAGES,
    install_package_data=True,
    zip_safe=False,
    entry_points=ENTRY_POINTS,
    install_requires=INSTALL_REQUIRES,
)
