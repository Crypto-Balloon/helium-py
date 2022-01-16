"""Tests for the Cities client."""

from helium_py import Cities


def test_cities():
    """Initial integration test for cities.

    This is only a proof-of-concept test and integration tests must be separated from unit tests.
    """
    cities = Cities()
    CHATTANOOGA = 'Chattanooga'
    search_cities = cities.all(search=CHATTANOOGA)
    chattanooga = next(search_cities)
    assert chattanooga['short_city'] == CHATTANOOGA
    assert cities.get_by_id(chattanooga['city_id'])['short_city'] == CHATTANOOGA
    assert 'status' in next(cities.hotspots_for_id(chattanooga['city_id']))
    # Only full hotspots in this city as off 2022-01-02
    assert len(list(cities.get_by_id(chattanooga['city_id']))) > 0
