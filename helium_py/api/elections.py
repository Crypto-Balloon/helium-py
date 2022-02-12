"""Elections client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import limit_api, time_filterable_api


class Elections(API):
    """Elections client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/elections
    """

    base_path = 'elections'

    @limit_api
    @time_filterable_api
    def all(self, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all elections (consensus group transactions)."""
        return self.client.fetch_all(params=params)
