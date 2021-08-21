import os
from typing import List, Optional
from pydantic import BaseSettings
from pydantic.main import BaseModel


class Settings(BaseSettings):
    ETHPLORER_KEY: str = os.getenv("ETHPLORER_KEY", "freekey")
    ETHERSCAN_KEY: str = os.getenv("ETHERSCAN_KEY", "freekey")
    OPENSEA_KEY: str = os.getenv("OPENSEA_KEY", "freekey")
    COVALENT_KEY: str = os.getenv("COVALENT_KEY", "freekey")
    RARIBLE_KEY: str = os.getenv("RARIBLE_KEY", "freekey")
    BITSKI_CLIENT_ID: str = os.getenv("BITSKI_CLIENT_ID", "freekey")
    BITSKI_CLIENT_SECRET: str = os.getenv("BITSKI_CLIENT_SECRET", "freekey")


class Network(BaseSettings):
    network_name: str
    network_id: int
    rpc_endpoint: str
    wss_endpoint: str
    primary_provider: str


class Provider(BaseSettings):
    """
    These are the 3rd Party Indexing Provider Bitski Leverages
    """

    provider_name: str
    provider_Id: str
    url: str = Optional[str]
    active_network: int
    network_options: List[Network] = None
    api_key: str = None
    evm_based: bool = True


settings = Settings()
