"""Rewards client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import time_filterable_api


class Rewards(API):
    """Rewards client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/rewards
    """

    base_path = 'rewards'

    @time_filterable_api(has_bucket=True)
    def get_total(self, params: Optional[dict], **kwargs):
        """Yield total network rewards for given params."""
        return self.client.fetch_all(path='/sum', params=params, **kwargs)
