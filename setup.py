import os
from setuptools import setup, find_packages

setup(
    name='test',
    version='0.0.0',

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        "pyyaml==5.1.2",
        "boto3==1.9.234",
        "jsonschema",
        "simplejson",
        "SQLAlchemy==1.3.11",
        "PyMySQL==0.9.3"
    ]
)
