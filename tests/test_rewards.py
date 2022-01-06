"""Tests for Rewards client."""
from datetime import timedelta, datetime

from helium_py import Rewards


def test_rewards():
    """Initial integration tests for rewards.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    rewards = Rewards()
    assert 1 == len(list(rewards.all(min_time=datetime.now() - timedelta(days=1), bucket='day')))
