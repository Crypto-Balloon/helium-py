"""Challenges client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import time_filterable_api, limit_api


class Challenges(API):
    """Challenges client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/challenges
    """

    base_path = 'challenges'

    @limit_api
    @time_filterable_api
    def all(self, params: Optional[dict], **kwargs):
        """Yield all challenge_receipts transactions."""
        return self.client.fetch_all(params=params, **kwargs)
