from os import name
from decimal import Decimal
from typing import List, Optional, Union

# import babel.numbers as bn
from pydantic import BaseModel, root_validator, Field, validator
from pydantic.errors import DateTimeError

CURRENCIES = "a"  # bn.list_currencies()
CURRENCY_VALUE_ERROR = ValueError(
    "Invalid currency code submitted. "
    f"Value must be one of the following {', '.join(CURRENCIES)}."
)


class AuthToken(BaseModel):
    status: str
    message: str
    auth_token: str


class NftToken(BaseModel):
    name: Optional[str]
    token_id: int
    opensea_id: Optional[str]
    description: Optional[str]
    image_url: Optional[str]

    @validator("token_id")
    def positive_token_id(cls: BaseModel, v: Decimal):
        if v <= 0:
            raise ValueError("NFT Token Id must be a positive number.")
        return v


class CurrencyTokenIn(BaseModel):
    name: Optional[str]
    symbol: Optional[str]
    tokenInfo: Optional[dict]
    balance: Optional[Decimal]

    @root_validator
    def validate_token_info(cls, values):
        try:
            tk_info = values.get("tokenInfo")
            values["name"] = tk_info["name"]
            values["symbol"] = tk_info["symbol"]
            return values
        except:
            return values

    @validator("balance")
    def positive_balance(cls: BaseModel, v: Decimal):
        if v < 0:
            raise ValueError("Balance must be a positive number.")
        return v

    @validator("symbol")
    def find_balance(cls: BaseModel, v: str):
        if not v:
            raise ValueError("Symbol must be a positive number.")
        return v


class RinkToken(BaseModel):
    name: Optional[str] = "rinkeby"
    symbol: Optional[str] = "ETH"
    balance: Optional[Decimal]
    contract_decimals: Optional[str] = "18"
    contract_ticker_symbol: Optional[str] = "ETH"
    contract_address: Optional[str] = ("0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",)
    type: Optional[str] = "cryptocurrency"

    @validator("balance")
    def positive_balance(cls: BaseModel, v):
        if v < 0:
            raise ValueError("Balance must be a positive number.")
        return v


class CurrencyToken(BaseModel):
    name: Optional[str]
    symbol: Optional[str]
    balance: Optional[Decimal]
    tokenInfo: Optional[dict]

    @root_validator
    def validate_token_info(cls, values):
        try:
            tk_info = values.get("tokenInfo")
            values["name"] = tk_info["name"]
            values["symbol"] = tk_info["symbol"]
            values["tokenInfo"] = {"address": tk_info["address"]}
            return values
        except:
            if values.get("name") == "ethereum":
                return values
            elif values.get("tokenInfo") == None:
                pass
            else:
                return values

    @validator("balance")
    def positive_balance(cls: BaseModel, v):
        if v < 0:
            raise ValueError("Balance must be a positive number.")
        return v

    @validator("symbol")
    def find_balance(cls: BaseModel, v: str):
        if not v:
            raise ValueError("Symbol must be a positive number.")
        return v


class EthResolver(BaseModel):
    name: Optional[str]
    symbol: Optional[str]
    balance: Optional[Decimal]

    @validator("balance")
    def positive_balance(cls: BaseModel, v: Decimal):
        if v < 0:
            raise ValueError("Balance must be a positive number.")
        return v

    @validator("symbol")
    def find_balance(cls: BaseModel, v: str):
        if not v:
            raise ValueError("Symbol must be a positive number.")
        return v


class Currencies(BaseModel):
    currencies: Optional[List[CurrencyToken]]


class TokensResponse(BaseModel):
    currencies: Optional[List[CurrencyToken]]
    nfts: Optional[List[NftToken]]
