import logging
import httpx
import asyncio
from typing import List

from src.schemas.token_schemas import CurrencyToken
from src.utils.settings import settings
from pydantic import parse_obj_as
from ..base_provider import BaseProvider

# get root logger
logger = logging.getLogger(
    __name__
)  # the __name__ resolve to "main" since we are at the root of the project.


logger.debug(settings)


class Ethplorer(BaseProvider):
    """
    Ethplorer’s API is useful to get information about Ethereum tokens,
    balances, addresses, history of transactions, contracts, and custom structures.
    There is no warranty for provided data.

        - https://api.ethplorer.io/ for mainnet
        - https://kovan-api.ethplorer.io/ for testnet (Kovan)

    API Methods

        - [getAddressInfo]

        /getAddressInfo/{address}

        Additional params:
            token: show balances for specified token address only
            showETHTotals: request total incoming and outgoing ETH values [true/false, default = false]

        - getLastBlock
        - getTokenInfo
        - getTxInfo
        - getTokenHistory
        - getAddressHistory
        - getAddressTransactions
        - getTop
        - getTopTokens
        - getTopTokenHolders
        - getTokenHistoryGrouped
        - getTokenPriceHistoryGrouped

    - https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API

    Bulk Monitor for large pools of transactions
    Target domains:
        - https://api-mon.ethplorer.io/ for mainnet;
        - https://kovan-api-mon.ethplorer.io/ for testnet (Kovan).

    - https://docs.ethplorer.io/monitor?from=apiDocs

    """

    MAINNET_URL = "https://api.ethplorer.io/api"
    TESTNET_URL = "https://kovan-api.ethplorer.io/"
    TESTNETS = ["KOVAN"]
    ETHPLORER_KEY = settings.ETHPLORER_KEY

    async def currency_details(self, assets):
        try:

            ebalance = assets.get("ETH")["balance"]
            eth_asset = CurrencyToken(name="ethereum", balance=ebalance, symbol="ETH")
            items = parse_obj_as(List[CurrencyToken], assets.get("tokens"))
            items.append(eth_asset)
            return items

        except Exception as e:
            logger.info(f"currency_details exception: {e}")
            return e

    async def get_tokens(self, account, network):

        # Request URL: https://api.opensea.io/api/v1/assets/?owner={account}&limit=50&offset=0
        # owner: 0x1725202263b29d137eAA9C94752170e13F7dB258
        # limit: 50
        # offset: 0
        try:
            if network.network_id == 1:
                callback_url = f"{self.MAINNET_URL}/getAddressInfo/{account}?apiKey={self.ETHPLORER_KEY}"
            else:
                callback_url = f"https://api.ethplorer.io/getAddressInfo/{account}?apiKey={self.ETHPLORER_KEY}"

            client = await self.http_client()
            response = await client.get(callback_url)
            packet = response.json()
            return packet
        except Exception as e:
            excep = f"Currency Tokens Call Failure: {e}"
            logger.info(excep)
            return excep
