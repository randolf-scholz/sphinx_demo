r"""Setup File.

We will move to pyproject.toml setup once PEP 660 is resolved and part of setuptools/poetry
"""

import io
import os
import re

import setuptools

NAME = "dummy_module"
VERSION = "0.0.0"

setuptools.setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    author="Randolf Scholz",
    author_email="scholz@ismll.uni-hildesheim.de",
    description="",
    long_description="",
    long_description_content_type="test/x-rst",
    packages=setuptools.find_packages(exclude=["test"]),  # include all packages in ...
    install_requires=[],
    # Files that listed in MANIFEST.in and also are in python packages,
    # i.e. contained in folders with and __init__.py, will be included.
    include_package_data=True,
    # ...but exclude virtualenv.yaml from all packages
    exclude_package_data={"": ["virtualenv.yaml"]},
)
