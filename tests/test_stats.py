"""Tests for Stats client."""

import pytest

from helium_py import Stats


def test_stats():
    """Initial integration tests for stats.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    stats = Stats()

    assert 'block_times' in stats.get_all()

    assert 'token_supply' in stats.get_token_supply()

    assert type(stats.get_token_supply(format='raw')) is float

    with pytest.raises(ValueError):
        stats.get_token_supply(format='foo')
