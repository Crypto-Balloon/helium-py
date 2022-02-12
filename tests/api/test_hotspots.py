"""Tests for Hotspots client."""
from helium_py.api import Hotspots


def test_hotspots():
    """Initial integration tests for hotspots.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    hotspots = Hotspots()
    oversaturated_hex_id = '8829a1d62dfffff'
    exotic_green_gazelle = '11GsHnL2T2XMV2XnwoH3gcbwwGgGTsxa6xcwxK4rnscg4oE1iEP'

    assert 'block_added' in next(hotspots.all())
    # TODO: Enable when filter_modes ain't broken
    # assert 'block_added' in next(hotspots.all(filter_modes='full'))
    assert 'block_added' in hotspots.hotspot_for_address(exotic_green_gazelle)
    assert 'block_added' in hotspots.hotspots_for_name('Exotic Green Gazelle')[0]
    assert 'block_added' in hotspots.hotspots_search_by_name('Exotic Green Gaz')[0]
    assert 'block_added' in hotspots.hotspots_search_by_geo(
        swlat=38.0795392, swlon=-122.5671627, nelat=38.1588012, nelon=-122.5046937)[0]
    assert 'block_added' in hotspots.hotspots_by_hex(oversaturated_hex_id)[0]
    assert 'hash' in next(hotspots.get_hotspot_activity(exotic_green_gazelle))
    assert 'add_gateway_v1' in hotspots.get_hotspot_activity_counts(exotic_green_gazelle)
    assert 'challenger' in next(hotspots.get_hotspot_challenges(exotic_green_gazelle))
    # Uncomment once more consistent
    # assert 'amount' in next(hotspots.get_hotspot_rewards(
    #     exotic_green_gazelle, min_time=datetime.now() - timedelta(days=5)))
    # assert 'avg' in hotspots.get_hotspot_rewards_total(
    #     exotic_green_gazelle, min_time=datetime.now() - timedelta(days=5))
    # assert 'block_added' in hotspots.get_hotspot_witnesses(exotic_green_gazelle)[0]
    # assert 'block_added' in hotspots.get_hotspot_witnessed(exotic_green_gazelle)[0]
