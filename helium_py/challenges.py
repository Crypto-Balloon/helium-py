"""Challenges client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class Challenges(Client):
    """Challenges client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/challenges
    """

    base_path = 'challenges'

    @time_filterable_api
    def all(self, params: Optional[dict], **kwargs):
        """Yield all challenge_receipts transactions."""
        return super().all(params=params, **kwargs)
