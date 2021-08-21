class BaseNetwork:

    PROVIDERS = ["covalent", "ethplorer", "etherscan", "opensea"]

    def __init__(self, network_id: str):
        self.network_id = network_id
        # self.configure_network(network_id)

    def init_mainnet(self):
        pass

    def init_testnet(self):
        pass

    def configure_network(self):
        pass

    def get_providers(self, provider):
        pass

    def get_latest_block(self):
        pass

    def get_nft_assets(self):
        pass

    def get_currency_assets(self):
        pass

    def get_stream_history(self):
        pass
