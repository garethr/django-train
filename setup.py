from setuptools import setup, find_packages

setup(
    name = "train",
    version = "0.1.2",
    
    packages = find_packages('src'),
    package_dir = {'':'src'},
)