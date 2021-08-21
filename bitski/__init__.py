import pkg_resources

from .utils.providers import AppWalletProvider, Covalent, OpenSea, Etherscan, Ethplorer, BaseProvider
from .utils.networks import Ethereum, Polygon, BaseNetwork, NetworkConfig, Network, NETWORKS

__version__ = pkg_resources.get_distribution("bitski").version

__all__ = [
    "__version__",
    "AppWalletProvider",
    "Covalent",
    "OpenSea",
    "Etherscan",
    "Ethplorer",
    "BaseProvider",
    "Ethereum",
    "Polygon",
    "BaseNetwork",
    "NetworkConfig",
    "Network",
    "NETWORKS"
]
