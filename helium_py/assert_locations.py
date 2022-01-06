"""Chain Variables client for Helium Blockchain API."""

import datetime as dt
from typing import Optional

from .client import Client


class AssertLocations(Client):
    """Assert Locations client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/assert-locations
    """

    base_path = 'assert_locations'

    def all(
        self,
        min_time: Optional[dt.datetime] = None,
        max_time: Optional[dt.datetime] = None,
        limit: Optional[int] = None,
        **kwargs,
    ):
        """Yield all cities.

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
        return super().all(params=params if params else None, **kwargs)
