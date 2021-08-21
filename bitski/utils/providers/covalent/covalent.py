import logging
import httpx
import asyncio
from typing import List, Optional

from src.schemas.token_schemas import NftToken, CurrencyToken

from src.utils.settings import Network, settings
from ..base_provider import BaseProvider
from .cova_schemas import CovaResponse
from pydantic import BaseModel, parse_obj_as

# get root logger
logger = logging.getLogger(
    __name__
)  # the __name__ resolve to "main" since we are at the root of the project.


class CovalentResponse(BaseModel):
    data: dict
    error: bool
    error_message: str
    error_code: int


class Covalent(BaseProvider):

    """
    Covalent Indexing API
    - https://www.covalenthq.com/docs/api/#overview--introduction

    Welcome to the Covalent API! Covalent provides a unified
    API to all assets secured by a blockchain network.

    There are two classes of endpoints:

        Class A - endpoints that return enriched blockchain data
        applicable to all blockchain networks, eg: balances, transactions, log events, etc.

        Class B - endpoints that for a specific protocol on a blockchain,
        eg: AAVE is Ethereum-only and is not applicable to other blockchain networks.

    Some points to keep in mind:

        - All requests are done over HTTPS (calls over plain HTTP will fail.)
        - The current version of the API is version 1.
        - The return format for all endpoints is JSON.
        - All requests require authentication.

    Response Structure:

       {
        "data": {...},
        "error": false,
        "error_message": null,
        "error_code": null
        }

    Use CovalentResponse Data Model for Serialization

    """

    mainnet_chains = {
        "Ethereum": 1,
        "Polygon/Matic": 137,
        "Avalanche C-Chain": 43114,
        "Binance Smart Chain": 56,
        "Fantom Opera": 250,
        "RSK": 30,
        "Arbitrum": 42161,
        "Palm": 11297108109,
    }

    testnets_chains = {
        "Polygon/Matic Mumbai": 80001,
        "Fuji C-Chain": 43113,
        "Kovan": 42,
        "Binance Smart Chain": 97,
        "Moonbase Alpha": 1287,
        "Fantom": 4002,
        "RSK": 31,
        "Arbitrum": 421611,
        "Palm": 11297108099,
    }

    COVALENT_KEY = settings.COVALENT_KEY
    COVALENT_DOMAIN = "https://api.covalenthq.com/v1/"

    async def get_tokens(
        self, account, network: Network = None, nft_bool: bool = False
    ):
        try:
            # Doesn't support Rinkeby
            available_nets = ["1", "137", "80001"]

            if str(network.network_id) in available_nets:

                callback_url = f"https://api.covalenthq.com/v1/{network.network_id}/address/{account}/balances_v2/?nft={nft_bool}&key={self.COVALENT_KEY}"

            async with httpx.AsyncClient() as client:
                response = await client.get(callback_url)

            if response.status_code != 200:
                raise
            elif response.status_code == 200:
                packet = response.json()
                try:
                    tokens = await self.currency_details(packet)
                except:
                    raise "couldnt deserialize"

                return tokens

        except Exception as e:
            excep = f"Currency Tokens Call Failure: {e}"
            logger.info(excep)
            return excep

    async def currency_details(self, assets):
        try:

            tokens = assets.get("data")["items"]
            items = parse_obj_as(List[CovaResponse], tokens)
            return items

        except Exception as e:
            logger.info(f"currency_details exception: {e}")
            return e

    async def nft_details(self, assets):
        try:
            items = parse_obj_as(List[NftToken], assets.get("assets"))
            return items
        except Exception as e:
            logger.info(f"nft_details exception: {e}")
            return e
