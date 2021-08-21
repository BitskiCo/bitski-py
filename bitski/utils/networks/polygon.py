from typing import List
from pydantic.main import BaseModel
from utils.settings import Network


class PolygonNetwork(BaseModel):
    name: str
    network_id: int
    networks: List[Network]


class Polygon:

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
    CHAIN_ID = 137

    """
    TESTNET SETTINGS
    """

    TESTNET_CHAIN_ID = 80001
    TESTNET_PARENT_CHAIN = "Goërli"

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
    CURRENCY = "MATIC"

    def configure_network(self) -> Network:
        pass
