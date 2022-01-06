"""Rewards client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class Rewards(Client):
    """Rewards client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/rewards
    """

    base_path = 'rewards'
    valid_buckets = ('hour', 'day', 'week')

    @time_filterable_api()
    def all(self, params: Optional[dict], bucket: Optional[str], **kwargs):
        """Yield all reward_receipts transactions."""
        if bucket:
            if bucket not in self.valid_buckets:
                raise ValueError(f'{bucket} not a valid option in {self.valid_buckets}')
            if not params:
                params = {}
            params['bucket'] = bucket
        return super().all(path='/sum', params=params, **kwargs)
