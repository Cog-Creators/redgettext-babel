#!/usr/bin/env python3
from setuptools import setup

setup(
    name="redgettext-babel-testproj",
    version="0.1.0",
    install_requires=["pip @ file://../.."],
    py_modules=["testproj"],
    message_extractors={"testproj.py": [("**.py", "red", None)]},
)
