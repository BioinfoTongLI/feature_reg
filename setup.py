#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 Tong LI <tongli.bioinfo@protonmail.com>
#
# Distributed under terms of the BSD-3 license.

"""

"""
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="featureReg",
    version="2.0.0",
    description="Feature based registration for fluorescence microscopy images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vasyl Vaskivskyi and Tong LI",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="microscope registration DAPI fluorescence microscopy whole-slide-imaging",
    packages=find_packages(),
    python_requires=">=3.0.*",
    install_requires=["numpy", "tifffile", "opencv-contrib-python", "dask", "scikit-learn"],
    entry_points={  # Optional
       'console_scripts': ['featReg = feature_based_registration.__main__:main'],
    },
    project_urls={  # Optional
       'Bug Reports': 'https://github.com/BayraktarLab/feature_reg/issues',
       # 'Say Thanks!': 'http://saythanks.io/to/example',
       'Source': 'https://github.com/BayraktarLab/feature_reg/',
    },
)
