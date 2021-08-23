import time
import cova_client
from cova_client.api import class_a_api
from cova_client.model.balance_response_type import BalanceResponseType
from pprint import pprint
# Defining the host is optional and defaults to https://api.covalenthq.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cova_client.Configuration(
    host = "https://api.covalenthq.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyQueryAuth
configuration.api_key['ApiKeyQueryAuth'] = 'ckey_5ae4558f74344e02a51b463466f'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQueryAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cova_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = class_a_api.ClassAApi(api_client)
    chain_id = "1" # str | Chain ID of the Blockchain being queried. Currently supports `1` for Ethereum Mainnet, `137` for Polygon/Matic Mainnet, `80001` for Polygon/Matic Mumbai Testnet, `56` for Binance Smart Chain, `43114` for Avalanche C-Chain Mainnet, `43113` for Fuji C-Chain Testnet, and `250` for Fantom Opera Mainnet.
    address = "0x1847582C385be3166210A82ABE79372c36ba335f" # str | Passing in an `ENS` resolves automatically.
    nft = True # bool | Set to `true` to return ERC721 and ERC1155 assets. Defaults to `false`. (optional)
    no_nft_fetch = True # bool | Set to `true` to skip fetching NFT metadata, which can result in faster responses. Defaults to `false` and only applies when `nft=true`. (optional)
    quote_currency = "quote-currency_example" # str | The requested fiat currency. (optional)
    format = "format_example" # str | If `format=csv`, return a flat CSV instead of JSON responses. (optional)
    primer = "primer_example" # str | Records enter a multi-stage pipeline that transforms the records into aggregated results. Supports $group and Aggregation operators. (optional)
    match = "match_example" # str | Filters the records to pass only the documents that match the specified condition(s). (optional)
    group = "group_example" # str | Groups input elements by the specified id expression and for each distinct grouping, outputs an element. Grouping by _date operators is also possible. (optional)
    sort = "sort_example" # str | Sorts all input records and returns them in ascending or descending sorted order. (optional)
    skip = 1 # int | Skips over the specified number of records. (optional)
    limit = 1 # int | Limits the number of records. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get token balances for address <span id=\"refresh-rate\" class=\"label label-primary label-xsmall\" style=\"vertical-align:super; font-size:x-small; background-color:#0098db;\">real-time</span>
        api_response = api_instance.get_v1_with_chain_id_address_with_address_balances_v2(chain_id, address)
        pprint(api_response)
    except cova_client.ApiException as e:
        print("Exception when calling ClassAApi->get_v1_with_chain_id_address_with_address_balances_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get token balances for address <span id=\"refresh-rate\" class=\"label label-primary label-xsmall\" style=\"vertical-align:super; font-size:x-small; background-color:#0098db;\">real-time</span>
        api_response = api_instance.get_v1_with_chain_id_address_with_address_balances_v2(chain_id, address, nft=nft, no_nft_fetch=no_nft_fetch, quote_currency=quote_currency, format=format, primer=primer, match=match, group=group, sort=sort, skip=skip, limit=limit)
        pprint(api_response)
    except cova_client.ApiException as e:
        print("Exception when calling ClassAApi->get_v1_with_chain_id_address_with_address_balances_v2: %s\n" % e)