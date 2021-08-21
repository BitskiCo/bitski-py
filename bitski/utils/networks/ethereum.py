from typing import Callable


class Ethereum:

    """
    Public RPCs may have traffic or rate-limits depending on usage.
    You can sign up for a dedicated free RPC URL at the following:
        - Infura
        - Alchemy
        - Chainstack
        - MaticVigil
        - QuickNode
        - Ankr
    """

    MAINNET_RPC = [
        "https://rpc-mainnet.matic.network",
        "https://matic-mainnet.chainstacklabs.com",
    ]
    MAINNET_ALT_RPC = [
        "https://rpc-mainnet.maticvigil.com",
        "https://rpc-mainnet.matic.quiknode.pro",
        "https://matic-mainnet-full-rpc.bwarelabs.com",
        "https://matic-mainnet-archive-rpc.bwarelabs.com",
    ]

    BLOCK_EXPLORERS = [
        "https://polygon-explorer-mainnet.chainstacklabs.com",
        "https://explorer-mainnet.maticvigil.com",
        "https://explorer.matic.network",
        "https://backup-explorer.matic.network",
        "https://polygonscan.com/",
    ]
    WEBSOCKETS_URL = ["wss://rpc-mainnet.matic.network"]
    CHAIN_ID = 1
    CURRENCY = "ETH"

    """
    RINKEBY TESTNET SETTINGS
    """
    TESTNET_CHAIN_ID = 4
    TESTNET_PARENT_CHAIN = "Kovan"
    """
    KOVAN TESTNET SETTINGS
    """
    TESTNET_CHAIN_ID = 42
    TESTNET_PARENT_CHAIN = "Kovan"

    TESTNET_RPC = [
        "https://rpc-mumbai.matic.today",
        "https://matic-mumbai.chainstacklabs.com",
        "https://rpc-mumbai.maticvigil.com",
        "https://matic-testnet-archive-rpc.bwarelabs.com",
    ]
    TESTNET_BLOCK_EXPLORERS = [
        "https://polygon-explorer-mumbai.chainstacklabs.com/",
        "https://backup-explorer.matic.network",
    ]
    TESTNET_WEBSOCKETS_URL = [
        "wss://rpc-mumbai.matic.today",
        "wss://ws-matic-mumbai.chainstacklabs.com",
    ]
    TESTNET_DAGGER_WSS = ["wss://mumbai-dagger.matic.today"]
    TESTNET_DAGGER_RPC = ["https://mumbai-dagger.matic.today"]
    """
    ROPSTEN TESTNET SETTINGS
    """
    ROPSTEN_CHAIN_ID = 3
    ROPSTEN_PARENT_CHAIN = "Ropsten"

    def __init__(self, network_id: str) -> Callable:
        eth_class = self.configure_network(network_id)
        return eth_class
