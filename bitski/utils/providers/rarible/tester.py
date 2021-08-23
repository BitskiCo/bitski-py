import time
import openapi_client
from pprint import pprint
from openapi_client.api import erc20_balance_controller_api
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://ethereum-api.rarible.org"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = erc20_balance_controller_api.Erc20BalanceControllerApi(api_client)
    contract = "0x60f80121c31a0d46b5279700f9df786054aa5ee5" # str | 
    owner = "0x60f80121c31a0d46b5279700f9df786054aa5ee5" # str | 

    try:
        api_response = api_instance.get_erc20_balance(contract, owner)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling Erc20BalanceControllerApi->get_erc20_balance: %s\n" % e)