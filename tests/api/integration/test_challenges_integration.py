"""Tests for Challenges client."""
import pytest

from helium_py.api import Challenges


@pytest.mark.integration
def test_challenges():
    """Initial integration tests for challenges.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    challenges = Challenges()

    assert 'poc_receipts_v1' == next(challenges.all(limit=1))['type']
