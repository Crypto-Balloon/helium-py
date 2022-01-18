"""Elections client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import limit_api, time_filterable_api


class Elections(API):
    """Elections client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/elections
    """

    base_path = 'elections'

    @limit_api
    @time_filterable_api
    def all(self, params: Optional[dict], **kwargs):
        """Yield all consensus_group transactions."""
        return self.client.fetch_all(params=params, **kwargs)
