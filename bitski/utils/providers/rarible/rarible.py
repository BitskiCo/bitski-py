import logging
import httpx
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


class RaribleItem(BaseModel):
    """
    Rarible supports metadata that is structured according to the official
    ERC721 metadata standard or the Enjin Metadata suggestions.

    {
        "total": 8,
        "continuation": "1573162953000_0xdceaf1652a131f32a821468dc03a92df0edd86ea:0x00000000000000000000000000000000000000000000000000000000009ba72b",
        "items": [
            {
                "id": "0x4dd3b03e3319ff443bcf20c9f09e51a6151a9233:206801668565619436875250563623505898869",
                "contract": "0x4dd3b03e3319ff443bcf20c9f09e51a6151a9233",
                "tokenId": "206801668565619436875250563623505898869",
                "creators": [
                    {
                        "account": "0xf020b2ae0995acedff07f9fc8298681f5461278a",
                        "value": 10000,
                    }
                ],
                "supply": "1",
                "lazySupply": "0",
                "owners": ["0xf020b2ae0995acedff07f9fc8298681f5461278a"],
                "royalties": [],
                "date": "2021-03-05T20:51:15Z",
                "pending": [],
                "deleted": false,
            },
            {
                "id": "0xdceaf1652a131f32a821468dc03a92df0edd86ea:10200875",
                "contract": "0xdceaf1652a131f32a821468dc03a92df0edd86ea",
                "tokenId": "10200875",
                "creators": [
                    {
                        "account": "0x7afe77c963aa230aa832e01577963739347d94ce",
                        "value": 10000,
                    }
                ],
                "supply": "1",
                "lazySupply": "0",
                "owners": ["0xf020b2ae0995acedff07f9fc8298681f5461278a"],
                "royalties": [],
                "date": "2019-11-07T21:42:33Z",
                "pending": [],
                "deleted": false,
            },
        ],
    }

    """

    id: str = "0xdceaf1652a131f32a821468dc03a92df0edd86ea:10200875"
    contract: str = "0xdceaf1652a131f32a821468dc03a92df0edd86ea"
    tokenId: str = "10200875"
    creators: list = [
        {
            "account": "0x7afe77c963aa230aa832e01577963739347d94ce",
            "value": 10000,
        }
    ]
    supply: str = "1"
    lazySupply: str = "0"
    owners: list = ["0xf020b2ae0995acedff07f9fc8298681f5461278a"]
    royalties: list = []
    date: str = "2019-11-07T21:42:33Z"
    pending: list = []
    deleted: bool = False


class RaribleResponse(BaseModel):
    total: int = 0
    continuation: str = "1573162953000_0xdceaf1652a131f32a821468dc03a92df0edd86ea:0x00000000000000000000000000000000000000000000000000000000009ba72b"
    items: List[RaribleItem] = None


class RaribleAsset(BaseModel):
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


class Rarible(BaseProvider):

    """
    Rarible API Provider Class

    Rinkeby:
    The API is identical to the Rarible mainnet API,
    except the base URL is https://ethereum-api.rarible.org/v0.1/doc

    """

    OPENSEA_DOMAIN = "https://api.opensea.io"
    MAINNET_URL = "https://api.opensea.io/api/v1/"
    TESTNET_URL = "https://rinkeby-api.opensea.io/api/v1/"
    TESTNETS = ["RINKEBY", "ROPSTEN"]
    OPENSEA_KEY = settings.OPENSEA_KEY

    def assets(self):
        url = "https://api.opensea.io/api/v1/assets"

        querystring = {"order_direction": "desc", "offset": "0", "limit": "20"}

        response = requests.request("GET", url, params=querystring)

        print(response.text)

    async def nft_details(self, assets):
        try:
            items = parse_obj_as(List[NftToken], assets.get("assets"))
            return items
        except Exception as e:
            logger.info(f"nft_details exception: {e}")
            return e

    async def get_tokens(self, account, network):

        # Request URL: https://api.opensea.io/api/v1/assets/?owner={account}&limit=50&offset=0
        # owner: 0x1725202263b29d137eAA9C94752170e13F7dB258
        # limit: 50
        # offset: 0
        try:
            if network.network_id != 1:
                callback_url = (
                    f"{self.TESTNET_URL}/assets/?owner={account}&limit=50&offset=0"
                )
            else:
                callback_url = (
                    f"{self.MAINNET_URL}/assets/?owner={account}&limit=50&offset=0"
                )

            async with httpx.AsyncClient() as client:
                response = await client.get(callback_url)

            packet = response.json()
            return packet
        except Exception as e:
            excep = f"NFT Tokens Call Failure: {e}"
            logger.info(excep)
            return excep
