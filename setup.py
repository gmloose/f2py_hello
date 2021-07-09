import os
from setuptools import find_packages
import numpy
from numpy.distutils.core import setup, Extension


packages = find_packages()
print("package={}".format(packages))

ext_modules = [
    Extension(
        "hello._hello",
        sources=["hello/hello.pyf", "hello/hello.f"],
        include_dirs=[numpy.get_include()],
    ),
]

setup(
    name="hello",
    version="0.0.1",
    url="https://github.com/someproject/hello",
    author="Marcel Loose",
    author_email="loose@astron.nl",
    description="Hello World",
    ext_modules=ext_modules,
    packages=packages,
    install_requires=["numpy"],
    package_data={
#        "hello": ["hello.pyf"],
    },
)
