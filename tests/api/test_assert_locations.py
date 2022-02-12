"""Tests for AssertLocations client."""

from helium_py.api import AssertLocations


def test_assert_locations():
    """Initial integration tests for assert locations.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    assert_locations = AssertLocations()

    assert 'assert_location_v2' == next(assert_locations.all(limit=1))['type']
