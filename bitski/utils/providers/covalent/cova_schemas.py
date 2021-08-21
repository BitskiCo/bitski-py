from typing import List, Optional
from pydantic import BaseModel


class CovaNFTMeta(BaseModel):
    name: str = None
    description: str = None
    image: str = None
    animation_url: None
    external_url: str = None
    attributes: dict = None
    owner: str = None


class CovaNFT(BaseModel):
    token_id: str
    token_balance: Optional[str] = None
    token_url: Optional[str] = None
    supports_erc: Optional[list] = None
    token_price_wei: Optional[float] = None
    token_quote_rate_eth: Optional[float] = None
    original_owner: str
    external_data: Optional[CovaNFTMeta] = None

    """
    class Config:
        schema_extra = {
            "token_id": "4351",
            "token_balance": "1",
            "token_url": "https://pixelmint.mypinata.cloud/ipfs/QmR5cQaji6zpXEndfoi3wNCqbi653xgNRy3nw1ynRcLjaK/data/4351.json",
            "supports_erc": ["erc20", "erc721"],
            "token_price_wei": None,
            "token_quote_rate_eth": None,
            "original_owner": "0xf873bebdd61ab385d6b24c135baf36c729ce8824",
            "external_data": {
                "name": "NFT  Bubble #4351",
                "description": "Tired of always missing the latest project? Never having enough ETH? Listening to mega-rich collectors cry about pickles? Show them how you really feel with NFT fuck-bubbles. Visit https://fuckbubbles.wtf to mint.",
                "image": "https://pixelmint.mypinata.cloud/ipfs/QmaMTrfaPkHrD3RsoN7VECBn8Wea6pBg175GCWFNbQRK6R/cusses/cyrptovoxels_crap_left.gif",
                "animation_url": None,
                "external_url": "http://www.bubbles.wtf",
                "attributes": [...],
                "owner": None,
            },
            "owner": "0x1847582c385be3166210a82abe79372c36ba335f",
            "owner_address": None,
            "burned": None,
        }
    """


class CovaResponse(BaseModel):
    contract_decimals: int  # "Smart contract decimals."
    contract_ticker_symbol: str  # "Smart contract ticker symbol."
    contract_address: str  # "Smart contract address."
    logo_url: Optional[str] = None  # "Smart contract URL."
    balance: int  # "Current balance."
    quote: Optional[
        float
    ] = None  # "The current balance converted to fiat in quote-currency."
    quote_rate: Optional[float] = None
    nft_data: Optional[List[CovaNFT]] = None
    type: Optional[str] = None


class CovalentItem(BaseModel):
    contract_decimals: int
    contract_name: Optional[str] = None
    contract_ticker_symbol: Optional[str] = None
    contract_address: Optional[str] = None
    supports_erc: Optional[list] = None
    logo_url: Optional[str] = None
    asset_type: Optional[str] = None
    balance: Optional[str] = None
    balance_24h: Optional[str] = None
    quote_rate: Optional[float] = None
    quote_rate_24: Optional[float] = None
    quote: Optional[float] = None
    quote_24h: Optional[float] = None
    nft_data: Optional[dict] = None

    class Config:
        schema_extra = {
            "contract_decimals": 18,
            "contract_name": "Ether",
            "contract_ticker_symbol": "ETH",
            "contract_address": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "supports_erc": None,
            "logo_url": "https://logos.covalenthq.com/tokens/0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.png",
            "type": "cryptocurrency",
            "balance": "10000000000000000",
            "balance_24h": None,
            "quote_rate": 2958.4822,
            "quote_rate_24h": None,
            "quote": 316.40726,
            "quote_24h": None,
            "nft_data": None,
        }
