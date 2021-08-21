import logging
import os

from web3 import HTTPProvider as Web3HTTPProvider

from oauth2_client.credentials_manager import CredentialManager, ServiceInformation


class AppWalletProvider(Web3HTTPProvider):
    def __init__(self, client_id, client_secret, network_name):
        service_information = ServiceInformation(
            "https://account.bitski.com/oauth2/auth",
            "https://account.bitski.com/oauth2/token",
            client_id,
            client_secret,
            ["eth_sign"],
        )
        self.manager = CredentialManager(service_information)
        self.client_id = client_id
        super().__init__("https://api.bitski.com/v1/web3/" + network_name)

    def get_request_headers(self):
        # TODO: Cache this
        self.manager.init_with_client_credentials()

        headers = Web3HTTPProvider.get_request_headers(self)
        headers.update(
            {
                "Authorization": "Bearer " + self.manager._access_token,
                "X-API-Key": self.client_id,
                "X-Client-Id": self.client_id,
            }
        )

        return headers
