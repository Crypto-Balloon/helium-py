"""Elections client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class Elections(Client):
    """Elections client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/elections
    """

    base_path = 'elections'

    @time_filterable_api
    def all(self, params: Optional[dict], **kwargs):
        """Yield all consensus_group transactions."""
        return super().all(params=params, **kwargs)
