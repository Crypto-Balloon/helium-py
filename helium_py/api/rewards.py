"""Rewards client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import bucket_api, time_filterable_api


class Rewards(API):
    """Rewards client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/rewards
    """

    base_path = 'rewards'

    @bucket_api
    @time_filterable_api
    def get_total(self, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield total network rewards for given bucket and time params."""
        return self.client.fetch_all(path='/sum', params=params)
