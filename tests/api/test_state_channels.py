
"""Tests for StateChannels client."""

import datetime as dt

from helium_py.api import StateChannels


def test_state_channels():
    """Initial integration tests for state_channels.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    state_channels = StateChannels()

    data = state_channels.all()
    assert type(next(data)) is dict

    LIMIT = 5
    data_limit = state_channels.all(limit=LIMIT)
    assert len(list(data_limit)) == LIMIT

    stop = dt.datetime(2022, 1, 5, 14, 0, 0, 0)
    start = stop - dt.timedelta(hours=6)
    data_time_bounded = state_channels.all(min_time=start, max_time=stop)
    assert len([i['time'] for i in data_time_bounded]) == 11
