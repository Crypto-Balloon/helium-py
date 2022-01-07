"""Tests for Locations client."""

import logging

from helium_py import Locations

logger = logging.getLogger(__name__)


def test_locations():
    """Initial integration tests for locations.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    locations = Locations()

    expected = {
        'data': {
            'short_street': 'Weyburn Ln',
            'short_state': 'CA',
            'short_country': 'US',
            'short_city': 'San Jose',
            'long_street': 'Weyburn Lane',
            'long_state': 'California',
            'long_country': 'United States',
            'long_city': 'San Jose',
            'location': '8c28347213117ff',
            'city_id': 'c2FuIGpvc2VjYWxpZm9ybmlhdW5pdGVkIHN0YXRlcw'
        }
    }

    assert expected == locations.get_location('8c28347213117ff')
