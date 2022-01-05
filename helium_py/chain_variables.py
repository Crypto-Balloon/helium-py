"""Chain Variables client for Helium Blockchain API."""

import datetime as dt
from typing import Optional

from .client import Client


class ChainVariables(Client):
    """Chain Variables client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/chain-variables
    """

    base_path = 'vars'

    def get_all(
        self,
        min_time: Optional[dt.datetime] = None,
        max_time: Optional[dt.datetime] = None,
        limit: Optional[int] = None,
        **kwargs,
    ):
        """Yield all chain variables.

        Args:
            min_time: The earliest time to return values for.
            max_time: The latest time to return values for.
            limit: The max number of results to return.
        """
        params = {}
        if min_time:
            params['min_time'] = min_time.isoformat()
        if max_time:
            params['max_time'] = max_time.isoformat()
        if limit:
            params['limit'] = str(limit)
        return list(super().all(params=params if params else None, **kwargs))[0]

    def get_by_name(self, var_name: str):
        """Return a var identified by var_name.

        Args:
            var_name: The name of a chain variable.
        """
        return list(self.all(path=f'/{var_name}'))[0]

    def all_activity(self, **kwargs):
        """Yield all chain variable activity."""
        return super().all(path='/activity', **kwargs)
