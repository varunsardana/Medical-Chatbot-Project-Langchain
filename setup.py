# We write setup.py as this makes your project installable as a python package

from setuptools import find_packages, setup # type: ignore

setup(
    name="medical_chatbot",
    version="0.1.0",
    author = "Varun Sardana",
    author_email = "varunsardana2006@gmail.com",
    packages = find_packages(),
    install_requires= []

)