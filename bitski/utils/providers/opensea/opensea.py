import logging
import httpx
import requests

import asyncio
from typing import List, Optional

from src.schemas.token_schemas import NftToken
from pydantic import BaseModel, parse_obj_as
from src.utils.settings import settings
from ..base_provider import BaseProvider
import requests

logger = logging.getLogger(
    __name__
)  # the __name__ resolve to "main" since we are at the root of the project.


logger.debug(settings)


class TokenMeta(BaseModel):
    """
    OpenSea supports metadata that is structured according to the official
    ERC721 metadata standard or the Enjin Metadata suggestions.

    - https://docs.opensea.io/docs/metadata-standards

    {
        "title": "Token Metadata",
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Identifies the asset to which this token represents"
            },
            "decimals": {
                "type": "integer",
                "description": "The number of decimal places that the token amount should display - e.g. 18, means to divide the token amount by 1000000000000000000 to get its user representation."
            },
            "description": {
                "type": "string",
                "description": "Describes the asset to which this token represents"
            },
            "image": {
                "type": "string",
                "description": "A URI pointing to a resource with mime type image/* representing the asset to which this token represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive."
            },
            "properties": {
                "type": "object",
                "description": "Arbitrary properties. Values may be strings, numbers, object or arrays."
            }
        }
    }
    - https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1155.md#erc-1155-metadata-uri-json-schema

    """

    # "Identifies the asset to which this token represents"
    name: str
    # "The number of decimal places that the token amount should display - e.g. 18, means to divide the token amount by 1000000000000000000 to get its user representation."
    decimals: int
    # "Describes the asset to which this token represents"
    description: str
    # "A URI pointing to a resource with mime type image/* representing the asset to which this token represents. Consider making any images at a width between 320 and 1080 pixels and aspect ratio between 1.91:1 and 4:5 inclusive."
    image: str
    # "Arbitrary properties. Values may be strings, numbers, object or arrays."
    properties: dict


class OpenSeaAsset(BaseModel):
    # "The token ID of the ERC721 asset"
    token_id: int
    # "An image for the item"
    image_url: str
    # The background color to be displayed with the item
    background_color: str
    # "Name of the item"
    name: str
    # External link to the original website for the item
    external_link: str
    # Dictionary of data on the contract itself (see asset contract section)
    asset_contract: dict
    # Dictionary of data on the owner (see account section)
    owner: dict
    # A list of traits associated with the item (see traits section)
    traits: list
    # When this item was last sold (null if there was no last sale)
    last_sale: Optional[str]


class OpenSea(BaseProvider):

    """
    OpenSea API Provider Class

    Rinkeby:
    The API is identical to the OpenSea mainnet API,
    except the base URL is https://rinkeby-api.opensea.io/api/v1/

    Polygon/Matic:

    """

    OPENSEA_DOMAIN = "https://api.opensea.io"
    MAINNET_URL = "https://api.opensea.io/api/v1/"
    TESTNET_URL = "https://rinkeby-api.opensea.io/api/v1/"
    TESTNETS = ["RINKEBY"]
    OPENSEA_KEY = settings.OPENSEA_KEY

    async def nft_details(self, assets):
        try:
            # items = parse_obj_as(List[NftToken.dict()], assets.get("assets"))
            tokens = assets.get("assets")
            tokens_list = [NftToken(**token) for token in tokens]
            return tokens_list
        except Exception as e:
            logger.info(f"nft_details exception: {e}")
            return e

    async def get_tokens(self, account, network):

        # Request URL: https://api.opensea.io/api/v1/assets/?owner={account}&limit=50&offset=0
        # owner: 0x1725202263b29d137eAA9C94752170e13F7dB258
        # limit: 50
        # offset: 0
        try:
            if self.network.network_id != 1:
                url = (
                    f"{self.TESTNET_URL}assets/?owner={account}&limit=50&offset=0"
                )
            else:
                url = (
                    f"{self.MAINNET_URL}assets/?owner={account}&limit=50&offset=0"
                )

            async with httpx.AsyncClient() as client:
                response = await client.get(url)

            packet = response.json()
            nfts = await self.nft_details(assets=packet)
            return nfts
        except Exception as e:
            excep = f"NFT Tokens Call Failure: {e}"
            logger.info(excep)
            return excep

    def get_assets(
        self,
        owner: str = None,
        token_ids: str = None,
        asset_contract_address: str = None,
        asset_contract_addresses: str = None,
        order_by: str = None,
        order_direction: str = "desc",
        limit: int = 300,
        offset: int = 0,
        collection: str = None,
    ):

        try:
            if self.network.network_id != 1:
                url = (
                    f"{self.TESTNET_URL}assets/?owner={owner}&limit=50&offset=0"
                )
            else:
                url = "https://api.opensea.io/api/v1/assets"


            url = "https://api.opensea.io/api/v1/assets"
            querystring = {"order_direction": "desc", "offset": "0", "limit": "20"}
            response = requests.request("GET", url, params=querystring)

            async with httpx.AsyncClient() as client:
                response = await client.get(url)

        packet = response.json()
        if response.status_code == 200:
            tokens_list = [OpenSeaAsset(**token) for token in packet]
            return tokens_list
        else:
            error = "OpenSea Retrive Assets call failure."
            return error 
        


    def get_bundles(
        self,
        on_sale: bool = False,
        owner: str = None,
        asset_contract_address: str = None,
        asset_contract_addresses: str = None,
        token_ids: str = None,
        limit: int = 300,
        offset: int = 0,
    ):

        url = "https://api.opensea.io/api/v1/bundles"
        querystring = {"limit": "20", "offset": "0"}
        response = requests.request("GET", url, params=querystring)
        print(response.text)

    def get_single_asset(self, asset_contract_address: str, token_id: str):

        url = "https://api.opensea.io/api/v1/asset/{asset_contract_address}/{token_id}/"
        response = requests.request("GET", url)
        print(response.text)

    def get_single_contract(self, asset_contract_address: str):
        url = "https://api.opensea.io/api/v1/asset_contract/{asset_contract_address}"
        response = requests.request("GET", url)
        print(response.text)

    def get_event(
        self,
        asset_contract_address: str = None,
        collection_slug: str = None,
        token_id: int = None,
        account_address: str = None,
        event_type: str = None,
        only_opensea: bool = None,
        auction_type: str = None,
        limit: int = 300,
        offset: int = 0,
        occurred_before=None,
        occurred_after=None,
    ):
        """
        https://docs.opensea.io/reference/retrieving-asset-events

        Endpoint: https://api.opensea.io/api/v1/events

        Query Params:
            asset_contract_address, string, The NFT contract address for the assets for which to show events

            collection_slug, string, Limit responses to events from a collection. Case sensitive and must match the collection slug exactly. Will return all assets from all contracts in a collection. For more information on collections, see our collections documentation.

            token_id, int32, The token's id to optionally filter by

            account_address, string, A user account's wallet address to filter for events on an account

            event_type, string, The event type to filter. Can be created for new auctions, successful for sales, cancelled, bid_entered, bid_withdrawn, transfer, or approve

            only_opensea, boolean, Restrict to events on OpenSea auctions. Can be true or false, false

            auction_type, string, Filter by an auction type. Can be english for English Auctions, dutch for fixed-price and declining-price sell orders (Dutch Auctions), or min-price for CryptoPunks bidding auctions.

            offset, int32, Offset for pagination, 0

            limit, string, Limit for pagination, 20

            occurred_before, date-time, Only show events listed before this timestamp. Seconds since the Unix epoch.

            occurred_after, date-time,  Only show events listed after this timestamp. Seconds since the Unix epoch.
        """

        url = "https://api.opensea.io/api/v1/events"
        querystring = {"only_opensea": "false", "offset": "0", "limit": "20"}
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)

    def get_collections(
        self, asset_owner: str = None, offset: int = 0, limit: int = 300
    ):

        url = "https://api.opensea.io/api/v1/collections"
        querystring = {"offset": "0", "limit": "300"}
        response = requests.request("GET", url, params=querystring)
        print(response.text)

    def get_orders(
        self,
        asset_contract_address: str = None,
        collection_slug: str = None,
        payment_token_address: str = None,
        maker: str = None, 
        taker: str = None, 
        owner: str = None,
        is_english: bool = False,
        bundled: bool = False,
        include_bundled: bool = False, 
        include_invalid: bool = False, 
        listed_after = None, 
        listed_before = None,
        token_id: int = None,
        token_ids: List[str] = None,
        side: int = None,
        sale_kind: int = None,
        limit: int = 300,
        offset: int = 0,
        order_by: str = None,
        order_direction: str = "desc",
    ):

        url = "https://api.opensea.io/wyvern/v1/orders"
        querystring = {"bundled":"false","include_bundled":"false","include_invalid":"false","limit":"20","offset":"0","order_by":"created_date","order_direction":"desc"}
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
