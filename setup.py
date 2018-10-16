from setuptools import setup

setup(
    name='bitski',
    version='0.0.1',
    description='A python SDK for accessing Bitski wallets',
    license='MIT',
    packages=['bitski'],
    author='Patrick Tescher',
    author_email='patrick@bitski.com',
    keywords=['web3'],
    url='https://github.com/BitskiCo/bitski-py',
    install_requires=[
        "oauth2-client",
        "web3"
    ]
)
