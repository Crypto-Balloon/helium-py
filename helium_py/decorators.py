"""helium_py decorators module."""

import datetime as dt
from functools import wraps
from typing import Optional


def time_filterable_api(f):
    """Decorate Client methods for API endpoints that support time-filtering."""
    @wraps(f)
    def wrapper(
        obj,
        min_time: Optional[dt.datetime] = None,
        max_time: Optional[dt.datetime] = None,
        limit: Optional[int] = None,
        **kwargs,
    ):
        """Parse params common to API endpoints that allow time and limit querying.

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

        return f(obj, params=params if params else None, **kwargs)
    return wrapper
