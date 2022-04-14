"""Hotspots client for Helium Blockchain API."""

from typing import Generator, List, Optional

from .api import API
from .decorators import (
    filter_modes_api,
    filter_transaction_types_api,
    limit_api,
    time_filterable_api,
)


class Hotspots(API):
    """Hotspots client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/hotspots
    """

    base_path = 'hotspots'

    @filter_modes_api
    def all(self, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all hotspots.

        Args:
            params: Filter mode params.
        """
        return self.client.fetch_all(params=params if params else None)

    def hotspot_for_address(self, address: str) -> dict:
        """Return hotspot details for a hotspot with provided address."""
        return self.client.get(path=f'/{address}')

    def hotspots_for_name(self, name: str) -> List[dict]:
        """Return hotspot details for a hotspot with provided name."""
        if len(name.split(' ')) == 3:
            name = '-'.join(name.split(' ')).lower()
        return self.client.get(path=f'/name/{name}')

    def hotspots_search_by_name(self, name: str) -> List[dict]:
        """Return search results for provided hotspot name."""
        return self.client.get(path='/name', params={'search': name})

    def hotspots_search_by_location_distance(self, lat: float, lon: float, distance: int) -> List[dict]:
        """Return hotspots that are contained within `distance` meters of point coordinates."""
        return self.client.get(
            path='/location/distance',
            params={
                'lat': lat,
                'lon': lon,
                'distance': distance,
            })

    def hotspots_search_by_geo(self, swlat: float, swlon: float, nelat: float, nelon: float) -> List[dict]:
        """Return hotspots that are contained within the box coordinates."""
        return self.client.get(
            path='/location/box',
            params={
                'swlat': swlat,
                'swlon': swlon,
                'nelat': nelat,
                'nelon': nelon,
            })

    def hotspots_by_hex(self, h3_index: str) -> List[dict]:
        """Return hotspots located within hex provided by h3_index."""
        return self.client.get(path=f'/hex/{h3_index}')

    @limit_api
    @time_filterable_api
    @filter_transaction_types_api
    def get_roles(self, address: str, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all roles for provided address."""
        return self.client.fetch_all(path=f'/{address}/roles', params=params if params else None)

    @filter_transaction_types_api
    def get_roles_counts(self, address: str, params: Optional[dict]) -> dict:
        """Return account roles for provided address."""
        return self.client.get(path=f'/{address}/roles/count', params=params if params else None)

    @time_filterable_api
    def get_hotspot_challenges(self, address: str, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield hotspot challenges for provided address."""
        return self.client.fetch_all(path=f'/{address}/challenges', params=params if params else None)

    @time_filterable_api
    def get_hotspot_rewards(self, address: str, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield hotspot rewards for provided address."""
        return self.client.fetch_all(path=f'/{address}/rewards', params=params if params else None)

    @time_filterable_api
    def get_hotspot_rewards_total(self, address: str, params: Optional[dict]) -> dict:
        """Return hotspot rewards totals for provided address."""
        return self.client.get(path=f'/{address}/rewards/sum', params=params if params else None)

    def get_hotspot_witnesses(self, address: str) -> List[dict]:
        """Return list of witnesses for a hotspot with provided address."""
        return self.client.get(path=f'/{address}/witnesses')

    def get_hotspot_witnessed(self, address: str) -> List[dict]:
        """Return list of hotspots witnessed by hotspot with provided address."""
        return self.client.get(path=f'/{address}/witnessed')
