import logging
import httpx
import asyncio
from typing import List

from schemas.token_schemas import RinkToken
from utils.settings import settings
from pydantic import parse_obj_as
from ..base_provider import BaseProvider
from etherscan import Etherscan as ethers

# get root logger
logger = logging.getLogger(
    __name__
)  # the __name__ resolve to "main" since we are at the root of the project.


logger.debug(settings)


class Etherscan(BaseProvider):
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
    ETHERSCAN_KEY = settings.ETHERSCAN_KEY

    async def currency_details(self, assets):
        try:
            if assets.get("status") == "1":
                bal = assets.get("result")
                rinkeby_asset = RinkToken(balance=float(bal))
            return rinkeby_asset

        except Exception as e:
            logger.info(f"currency_details exception: {e}")
            return e

    async def get_tokens(self, account, network):
        try:
            if network.network_id == 1:
                # eth = ethers(self.ETHERSCAN_KEY) # net name is case-insensitive, default is main
                callback_url = f"https://api-rinkeby.etherscan.io/api?module=account&action=balance&address={account}&tag=latest&apikey={self.ETHERSCAN_KEY}"
            else:
                callback_url = f"https://api-rinkeby.etherscan.io/api?module=account&action=balance&address={account}&tag=latest&apikey={self.ETHERSCAN_KEY}"
                # eth = ethers(self.ETHERSCAN_KEY, net=network.network_name) # net name is case-insensitive, default is main
                # eth.get_eth_balance(address=account)

            async with httpx.AsyncClient() as client:
                response = await client.get(callback_url)

            if response.status_code != 200:
                raise
            elif response.status_code == 200:
                packet = response.json()
            tokens = await self.currency_details(assets=packet)
            return tokens

        except Exception as e:
            excep = f"Currency Tokens Call Failure: {e}"
            logger.info(excep)
            return excep
