# -*- coding: utf-8 -*-
from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    install_requires=required
)
