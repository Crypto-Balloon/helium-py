"""DC Burn client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class DCBurns(Client):
    """Rewards client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/rewards
    """

    base_path = 'dc_burns'

    @time_filterable_api(has_bucket=True)
    def get_total(self, params: Optional[dict], **kwargs):
        """Yield total data credits burned for given params."""
        return super().all(path='/sum', params=params, **kwargs)

    def get_stats(self):
        """Return current statistics for Data Credits burned."""
        return super().get(path='/stats')

    def all(self, **kwargs):
        """Yield all data credits burned."""
        return super().all(**kwargs)
