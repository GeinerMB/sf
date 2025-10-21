# lab4/setup.py
from setuptools import setup, find_packages

setup(
    name='lab_combat_system', # Nombre de tu paquete
    version='0.1.0',
    packages=find_packages(), # Esto encontrará las carpetas 'src' y 'tests'
)