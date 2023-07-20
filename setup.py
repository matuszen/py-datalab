import sys
from setuptools import setup, find_packages
from Cython.Build import cythonize

if sys.version_info < (3, 10):
    sys.exit("Sorry, Python < 3.10 is not supported")

setup(
    name="py-datalab",
    version="0.2.4",
    author="Mateusz Nowak",
    author_email="mateusz.nowak.pol@gmail.com",
    description="This project provides classes for working with data in python. Actually there are two classes: Matrix and Vector.",
    url="https://github.com/matuszen/Python-DataLab",
    packages=find_packages(),
    ext_modules=cythonize("datalab/stat/func/basic.pyx"),
    install_requires=[
        "typing_extensions",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
)
