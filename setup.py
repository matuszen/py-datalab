import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    sys.exit("Sorry, Python < 3.6 is not supported")

setup(
    name="py-datalab",
    version="0.1.0",
    author="Mateusz Nowak",
    author_email="mateusz.nowak.pol@gmail.com",
    description="This project provides classes for working with data in python. Actually there are two classes: Matrix and Vector.",
    url="https://github.com/matuszen/Python-DataLab",
    packages=find_packages(where="datalab"),
    package_dir={"": "datalab"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
)
