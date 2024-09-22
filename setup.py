'''
Installation du projet en une simple commande grace à un setup
'''
from setuptools import setup, find_packages

setup(
    name="pyScriptForHardisGroup",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[], # Rien ici car les dépendances sont dans requirements.txt
)
