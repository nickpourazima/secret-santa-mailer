from setuptools import setup, find_packages

setup(
    name='secret_santa',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "google-auth",
        "google-api-python-client",
        "pytest"
        ],
)
