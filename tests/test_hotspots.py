"""Tests for Hotspots client."""
from datetime import datetime, timedelta

from helium_py import Hotspots


def test_hotspots():
    """Initial integration tests for hotspots.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    hotspots = Hotspots()
    oversaturated_hex_id = '8829a1d62dfffff'
    fresh_cinnamon_duck = '112MWhDhXS8ZrP52K1tjds9HRvurqv2jkXm5kB5pozReC9AHbXo6'

    assert 'block_added' in next(hotspots.all())
    # TODO: Enable when filter_modes ain't broken
    # assert 'block_added' in next(hotspots.all(filter_modes='full'))
    assert 'block_added' in hotspots.hotspot_for_address(fresh_cinnamon_duck)
    assert 'block_added' in hotspots.hotspots_for_name('Fresh Cinnamon Duck')[0]
    assert 'block_added' in hotspots.hotspots_search_by_name('Fresh Cinnamon Du')[0]
    assert 'block_added' in hotspots.hotspots_search_by_geo(
        swlat=38.0795392, swlon=-122.5671627, nelat=38.1588012, nelon=-122.5046937)[0]
    assert 'block_added' in hotspots.hotspots_by_hex(oversaturated_hex_id)[0]
    assert 'hash' in next(hotspots.get_hotspot_activity(fresh_cinnamon_duck))
    assert 'add_gateway_v1' in hotspots.get_hotspot_activity_counts(fresh_cinnamon_duck)
    assert 'challenger' in next(hotspots.get_hotspot_challenges(fresh_cinnamon_duck))
    assert 'amount' in next(hotspots.get_hotspot_rewards(
        fresh_cinnamon_duck, min_time=datetime.now() - timedelta(days=1)))
    assert 'avg' in hotspots.get_hotspot_rewards_total(
        fresh_cinnamon_duck, min_time=datetime.now() - timedelta(days=1))
    assert 'block_added' in hotspots.get_hotspot_witnesses(fresh_cinnamon_duck)[0]
    assert 'block_added' in hotspots.get_hotspot_witnessed(fresh_cinnamon_duck)[0]
