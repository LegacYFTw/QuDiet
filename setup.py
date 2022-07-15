from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Framework",
    version="0.1.0a",
    description="A package to perform quantum circuit calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LegacYFTw/qubit-qudit-sim",
    keywords="quantum sdk",
    license="LGPLv3",
    package_dir={ "": "src" }, 
    packages=find_packages(where="src"),
    install_requires=[
        "numpy",
        "scipy",
        "numba",
        "pytest",
    ],
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