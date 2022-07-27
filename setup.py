#               This file is part of the QuDiet package.
#              https://github.com/LegacYFTw/qubit-qudit-sim
#
#                      Copyright (c) 2022.
#                      --.- ..- -.. .. . -
#
# Turbasu Chatterjee, Subhayu Kumar Bala, Arnav Das
# Dr. Amit Saha, Prof. Anupam Chattopadhyay, Prof. Amlan Chakrabarti
#
#
# SPDX-License-Identifier: AGPL-3.0
#
#  This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
import warnings

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PY_VERSION = (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)

CUDA_HOME = any(
    [
        os.environ.get("CUDA_HOME"),
        os.environ.get("CUDA_PATH"),
        os.environ.get("CUDA_VERSION"),
        os.environ.get("CUDNN_VERSION"),
        os.environ.get("COLAB_GPU"),
    ]
)

install_requires = [
    "numpy",
    "scipy",
    # "numba",
    "pytest",
]

if PY_VERSION <= (3, 7):
    install_requires += ["typing-extensions"]

if CUDA_HOME:
    install_requires += ["cupy-cuda100"]
else:
    warnings.warn("CUDA not found. CUDA backends will be disabled.")

setup(
    name="QuDiet",
    version="0.1.0a0",
    description="A package to perform quantum circuit calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LegacYFTw/qubit-qudit-sim",
    keywords="quantum sdk",
    license="LGPLv3",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_requires,
    classifiers=[
        # License
        "License :: OSI Approved :: GNU Affero General Public License v3",
        # Project Maturity
        "Development Status :: 1 - Planning",
        # Topic
        "Topic :: Scientific/Engineering :: Physics",
        # Intended Audience
        "Intended Audience :: Science/Research",
        # Compatibility
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        # Python Version
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
