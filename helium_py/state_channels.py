"""State Channels client for Helium Blockchain API."""

import datetime as dt
from typing import Optional

from .client import Client


class StateChannels(Client):
    """Stats client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/state-channels
    """

    base_path = 'state_channels'

    def all(
        self,
        min_time: Optional[dt.datetime] = None,
        max_time: Optional[dt.datetime] = None,
        limit: Optional[int] = None,
        **kwargs,
    ):
        """Yield all state_channels.

        Args:
            search: Search term.
        """
        params = {}
        if min_time:
            params['min_time'] = min_time.isoformat()
        if max_time:
            params['max_time'] = max_time.isoformat()
        if limit:
            params['limit'] = str(limit)
        return super().all(params=params if params else None, **kwargs)
