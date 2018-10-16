# Bitski Python SDK

Currently this can only be use with our app wallet:

## Example

```python
from bitski import AppWalletProvider
from web3 import Web3

provider = AppWalletProvider("<YOUR CLIENT ID>", "<YOUR CLIENT SECRET>", "rinkeby")
w3 = Web3(provider)

accounts = w3.eth.accounts

print("Got account(s) on Rinkeby:")
print(repr(accounts))
````
