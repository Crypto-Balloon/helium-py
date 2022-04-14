"""Tests for Elections client."""
import pytest

from helium_py.api import Elections


@pytest.mark.integration
def test_elections():
    """Initial integration tests for elections.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    elections = Elections()

    assert 'consensus_group_v1' == next(elections.all(limit=1))['type']
