import pydantic
from setuptools import setup, find_packages

setup(
    name='bitski',
    version='0.0.1',
    description='A python SDK for accessing Bitski wallets',
    license='MIT',
    packages=find_packages(),
    author='Patrick Tescher',
    author_email='patrick@bitski.com',
    keywords=['web3'],
    url='https://github.com/BitskiCo/bitski-py',
    install_requires=[
        "oauth2-client",
        "web3",
        "pydantic",
        "httpx"
        
    ]
)
