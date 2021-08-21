import logging
import httpx

from src.utils.settings import settings

# get root logger
logger = logging.getLogger(__name__)

logger.debug(settings)


class BaseProvider(object):
    def __init__(self, network) -> None:
        super().__init__()
        self.network = network
        self.network_id = network.network_id
        self.provider_options = []
        self.default_provider = None

    async def http_client(self):
        async with httpx.AsyncClient() as client:
            return client
