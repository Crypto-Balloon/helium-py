"""State Channels client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import limit_api, time_filterable_api


class StateChannels(API):
    """State Channels client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/state-channels
    """

    base_path = 'state_channels'

    @limit_api
    @time_filterable_api
    def all(self, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all state_channels."""
        return self.client.fetch_all(params=params if params else None)
