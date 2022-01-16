"""DC Burn client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import bucket_api, time_filterable_api


class DCBurns(API):
    """Rewards client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/dc-burns
    """

    base_path = 'dc_burns'

    def all(self, **kwargs):
        """Yield all data credits burned."""
        return self.client.fetch_all(**kwargs)

    @bucket_api
    @time_filterable_api
    def get_total(self, params: Optional[dict], **kwargs):
        """Yield total data credits burned for given params."""
        return self.client.fetch_all(path='/sum', params=params, **kwargs)

    def get_stats(self):
        """Return current statistics for Data Credits burned."""
        return self.client.get(path='/stats')
