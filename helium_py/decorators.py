"""helium_py decorators module."""

import datetime as dt
from functools import wraps
from typing import Optional

from helium_py.constants import VALID_BUCKETS, VALID_FILTER_MODES, VALID_FILTER_TYPES


def time_filterable_api(f):
    """Decorate Client methods for API endpoints that support time-filtering."""
    @wraps(f)
    def wrapper(
        obj,
        *args,
        params: Optional[dict] = None,
        min_time: Optional[dt.datetime] = None,
        max_time: Optional[dt.datetime] = None,
        **kwargs,
    ):
        """Parse params common to API endpoints that allow time and limit querying.

        Args:
            params: Params dict pass through for decorators.
            min_time: The earliest time to return values for.
            max_time: The latest time to return values for.
            limit: The max number of results to return.
            bucket: The bucket to group results by.
        """
        if params is None:
            params = {}
        if min_time:
            params['min_time'] = min_time.isoformat()
        if max_time:
            params['max_time'] = max_time.isoformat()
        return f(obj, *args, params=params if params else None, **kwargs)
    return wrapper


def limit_api(f):
    """Decorate Client methods for API endpoints that support time-filtering."""
    @wraps(f)
    def wrapper(obj, *args, params: Optional[dict] = None, limit: Optional[int] = None, **kwargs):
        """Parse params common to API endpoints that allow time and limit querying.

        Args:
            params: Params dict pass through for decorators.
            limit: Limit number of results.
        """
        if params is None:
            params = {}
        if limit:
            params['limit'] = str(limit)
        return f(obj, *args, params=params if params else None, **kwargs)
    return wrapper


def bucket_api(f):
    """Decorate Client methods for API endpoints that support time-filtering."""
    @wraps(f)
    def wrapper(obj, *args, params: Optional[dict] = None, bucket: Optional[str] = None, **kwargs):
        """Parse params common to API endpoints that allow time and limit querying.

        Args:
            params: Params dict pass through for decorators.
            bucket: Bucket to group results.
        """
        if params is None:
            params = {}
        if bucket:
            if bucket not in VALID_BUCKETS:
                raise ValueError(f'{bucket} not a valid option in {VALID_BUCKETS}')
            params['bucket'] = bucket
        return f(obj, *args, params=params if params else None, **kwargs)
    return wrapper


def filter_modes_api(f):
    """Decorate Client methods for API endpoints that support time-filtering."""
    @wraps(f)
    def wrapper(obj, *args, params: Optional[dict] = None,  filter_modes: Optional[str] = None, **kwargs):
        """Parse params common to API endpoints that allow time and limit querying.

        Args:
            params: Params dict pass through for decorators.
            filter_modes: The earliest time to return values for.
        """
        if params is None:
            params = {}
        if filter_modes:
            if not all([mode in VALID_FILTER_MODES for mode in filter_modes.split(',')]):
                raise ValueError(f'One or more of {filter_modes} not in {VALID_FILTER_MODES}')
            params['filter_modes'] = filter_modes

        return f(obj, *args, params=params if params else None, **kwargs)
    return wrapper


def filter_transaction_types_api(f):
    """Decorate Client methods for API endpoints that support time-filtering."""
    @wraps(f)
    def wrapper(obj, *args, params: Optional[dict] = None,  filter_types: Optional[str] = None, **kwargs):
        """Parse params common to API endpoints that allow time and limit querying.

        Args:
            params: Params dict pass through for decorators.
            filter_modes: The earliest time to return values for.
        """
        if params is None:
            params = {}
        if filter_types:
            if not all([mode in VALID_FILTER_TYPES for mode in filter_types.split(',')]):
                raise ValueError(f'One or more of {filter_types} not in {VALID_FILTER_TYPES}')
            params['filter_types'] = filter_types

        return f(obj, *args, params=params if params else None, **kwargs)
    return wrapper
