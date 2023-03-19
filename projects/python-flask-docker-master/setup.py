from setuptools import setup, find_packages

setup(
    name='Devins_test',
    version='0.1.02',
    author='Devin Powers',
    author_email='Devinjpowers@gmail.com',
    description='A simple Python package for testing',
    packages=find_packages(),
    install_requires=[
        'flask',
        'numpy'
    ]
)
