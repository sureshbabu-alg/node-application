from setuptools import setup, find_packages

with open("requirements.txt", "r") as req:
    requirements = [line.strip() for line in req]

setup(
    name='test',
    version='0.0.0',
    packages=find_packages(),
    python_version='3.7',
    include_package_data=True,
    install_requires=requirements,
)
