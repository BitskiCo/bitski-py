import logging

from typing import List, Optional, Callable
from exceptions import BitskiException
from fastapi import HTTPException
from utils.networks import Ethereum, Polygon
from pydantic import BaseModel, networks, parse_obj_as
from pydantic import ValidationError, validator

logger = logging.getLogger(
    __name__
)  # the __name__ resolve to "main" since we are at the root of the project.

NETWORKS = {
    "1": {
        "network_name": "mainnet",
        "network_id": 1,
        "chain": "ethereum",
        "currency": "ETH",
        "network_class": Ethereum,
        "general_networks": False,
    },
    "4": {
        "network_name": "rinkeby",
        "network_id": 4,
        "chain": "ethereum",
        "currency": "ETH",
        "network_class": Ethereum,
        "general_networks": False,
    },
    "137": {
        "network_name": "mainnet",
        "network_id": 137,
        "chain": "polygon",
        "currency": "MATIC",
        "network_class": Polygon,
        "general_networks": False,
    },
    "80001": {
        "network_name": "mumbai",
        "network_id": 80001,
        "chain": "polygon",
        "currency": "MATIC",
        "network_class": Polygon,
        "general_networks": False,
    },
}


class Network(BaseModel):
    network_id: int = 1
    network_name: str = "mainnet"
    chain: str = "ethereum"
    currency: str = "ETH"
    general_networks: bool = False
    network_class: Optional[Callable]

    @validator("network_id")
    def network_match(cls, v):
        if v == 1:
            logger.info("Eth-Mainnet Network Chosen")
        elif v == 4:
            logger.info("Eth-Rinkeby Network Chosen")
        elif v == 137:
            logger.info("Matic-Mainnet Network Chosen")
        elif v == 80001:
            logger.info("Matic-Mumbai Network Chosen")
        else:
            raise ValueError("Unsupported Network Id")
        return v


class Networks(BaseModel):
    supported_networks: List[int] = [1, 4, 137, 80001, 0]
    ethereum: Optional[Network]
    polygon: Optional[Network]


class NetworkConfig:
    """
    Resolve Network Class from Network ID Query Param

    """

    def __init__(self, network_id: int = 0):

        self.general_networks = False
        self.network_id = network_id
        self.network_name: str = None
        self.chain: str = None
        self.currency: str = None
        self.networks = NETWORKS
        # self.network = self.network_resolver()

    def network_resolver(self):

        try:
            network = self.networks[self.network_id]
            network_asset = Network(**network)
            self.network_name = network_asset.network_name
            self.chain = network_asset.chain
            self.currency = network_asset.currency
            return network_asset
        except:
            message = "Invalid Network Id, Not supported"
            logging.info(message)
            return BitskiException(status_code=400, status="fail", message=message)

    def __call__(self, network_id: int = 0):

        self.general_networks = False
        available_nets = ["1", "4", "137", "80001"]

        if network_id == 0:
            self.network_id = "1"
            self.general_networks = True

        elif str(network_id) in available_nets:
            self.network_id = str(network_id)

        else:
            raise HTTPException(status_code=400, detail="Missing Network")

        net = self.network_resolver()

        if isinstance(net, Network):
            if self.general_networks:
                net.general_networks = True
            return net
        else:
            raise HTTPException(status_code=400, detail="Missing Network")
