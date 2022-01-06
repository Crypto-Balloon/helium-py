"""State Channels client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class StateChannels(Client):
    """Stats client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/state-channels
    """

    base_path = 'state_channels'

    @time_filterable_api(has_limit=True)
    def all(self, params: Optional[dict], **kwargs):
        """Yield all state_channels."""
        return super().all(params=params if params else None, **kwargs)
