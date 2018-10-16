import pkg_resources

from .providers import AppWalletProvider

__version__ = pkg_resources.get_distribution("bitski").version

__all__ = [
    "__version__",
    "AppWalletProvider",
]
