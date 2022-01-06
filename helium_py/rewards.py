"""Rewards client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class Rewards(Client):
    """Rewards client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/rewards
    """

    base_path = 'rewards'

    @time_filterable_api(has_bucket=True)
    def get_total(self, params: Optional[dict], **kwargs):
        """Yield total network rewards for given params."""
        return super().all(path='/sum', params=params, **kwargs)
