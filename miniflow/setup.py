#!/usr/bin/env python

# -*- coding: utf-8 -*-

#///////////////////////////////////////////////////////////
#-----------------------------------------------------------
# File: setup.py
# Author: Andreas Ntalakas  https://github.com/antalakas
#-----------------------------------------------------------

#///////////////////////////////////////////////////////////
# Import a setup module
from setuptools import setup, find_packages

#///////////////////////////////////////////////////////////
# Import package
import miniflow

#///////////////////////////////////////////////////////////
# Basic setup
setup(

    # Package Details
    name='miniflow',
    version=miniflow.__version__,
    author=miniflow.__author__,
    url=miniflow.__url__,
    packages=find_packages(exclude=['tests','docs'],),
    include_package_data=True,

    # Disable for allowing copying files
    zip_safe=False,

    # Package Description
    description='miniflow is a (mini) neural network library.',
    long_description=miniflow.__description__,
    license='MIT',

    # Dependent Packages (if any)
    requires=['Sphinx',],

    install_requires=[
        "Sphinx>=1.3.1",
    ],
)
