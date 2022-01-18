"""Tests for DCBurns client."""
from datetime import datetime, timedelta

from helium_py import DCBurns


def test_dc_burns():
    """Initial integration tests for dc_burns.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    dc_burns = DCBurns()
    assert 1 == len(list(dc_burns.get_total(min_time=datetime.now() - timedelta(days=1), bucket='day')))

    stats = dc_burns.get_stats()
    assert 'meta' in stats and 'data' in stats

    events = next(dc_burns.all())
    assert 'block' in events and 'type' in events and 'amount' in events
