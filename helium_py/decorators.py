"""helium_py decorators module."""

import datetime as dt
from functools import wraps
from typing import Optional

from helium_py.constants import VALID_BUCKETS, VALID_FILTER_MODES


def time_filterable_api(has_limit=False, has_bucket=False, filter_by_mode=False):
    """Parameterize additional constraints for filtering APIs."""
    def decorator(f):
        """Decorate Client methods for API endpoints that support time-filtering."""
        @wraps(f)
        def wrapper(
            obj,
            *args,
            min_time: Optional[dt.datetime] = None,
            max_time: Optional[dt.datetime] = None,
            limit: Optional[int] = None,
            bucket: Optional[str] = None,
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
            if has_limit and limit:
                params['limit'] = str(limit)
            if has_bucket and bucket:
                if bucket not in VALID_BUCKETS:
                    raise ValueError(f'{bucket} not a valid option in {VALID_BUCKETS}')
                params['bucket'] = bucket

            return f(obj, *args, params=params if params else None, **kwargs)
        return wrapper

    if callable(has_limit):
        return decorator(has_limit)
    else:
        return decorator


def filter_modes_api(f):
    """Decorate Client methods for API endpoints that support time-filtering."""
    @wraps(f)
    def wrapper(
            obj,
            *args,
            filter_modes: Optional[str] = None,
            **kwargs,
    ):
        """Parse params common to API endpoints that allow time and limit querying.

        Args:
            filter_modes: The earliest time to return values for.
        """
        params = {}
        if filter_modes:
            if not all([mode in VALID_FILTER_MODES for mode in filter_modes.split(',')]):
                raise ValueError(f'One or more of {filter_modes} not in {VALID_FILTER_MODES}')
            params['filter_modes'] = filter_modes

        return f(obj, *args, params=params if params else None, **kwargs)
    return wrapper
