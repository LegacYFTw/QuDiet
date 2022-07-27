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

import nox

PYTHON_ENV = python = ["3.6", "3.7", "3.8", "3.9", "3.10"]

SOURCE_FILES = (
    "setup.py",
    "noxfile.py",
    "src/qudiet/",
    "test/",
    "scripts/license-headers.py",
)


@nox.session(python=PYTHON_ENV)
def tests(session):
    """Run the test suite."""
    session.install("black")
    session.install("pytest")
    session.install(".")
    session.run("pytest")


@nox.session(python=PYTHON_ENV)
def lint(session):
    """Run the lint suite."""

    session.install("flake8", "black", "mypy", "isort", "types-requests")

    session.run("isort", "--check", "--profile=black", *SOURCE_FILES)
    session.run("black", "--target-version=py39", "--check", *SOURCE_FILES)
    session.run("python", "scripts/license-headers.py", "check", *SOURCE_FILES)


@nox.session(python=PYTHON_ENV)
def formatting(session):
    """Run the formatter suite."""
    session.install(
        "black", "isort", "autopep8", "flake8-black", "flake8-bugbear", "flake8-bandit"
    )

    session.run("isort", "--profile=black", *SOURCE_FILES)
    session.run("black", "--target-version=py39", *SOURCE_FILES)
    session.run("stubgen", "-p", "framework", external=True)
    session.run("python", "scripts/license-headers.py", "fix", *SOURCE_FILES)
