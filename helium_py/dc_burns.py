"""DC Burns client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import bucket_api, time_filterable_api


class DCBurns(API):
    """DC Burns client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/dc-burns
    """

    base_path = 'dc_burns'

    def all(self) -> Generator[dict, None, None]:
        """Yield all data credits burn events."""
        return self.client.fetch_all()

    @bucket_api
    @time_filterable_api
    def get_total(self, params: Optional[dict]) -> dict:
        """Return total data credits burned for given params."""
        return self.client.get(path='/sum', params=params)

    def get_stats(self) -> dict:
        """Return current statistics for Data Credits burned."""
        return self.client.get(path='/stats')
