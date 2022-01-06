"""Challenges client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import time_filterable_api


class Challenges(API):
    """Challenges client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/challenges
    """

    base_path = 'challenges'

    @time_filterable_api(has_limit=True)
    def all(self, params: Optional[dict], **kwargs):
        """Yield all challenge_receipts transactions."""
        return self.client.fetch_all(params=params, **kwargs)
