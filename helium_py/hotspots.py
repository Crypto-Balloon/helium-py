"""Hotspots client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import (
    filter_modes_api,
    filter_transaction_types_api,
    time_filterable_api,
)


class Hotspots(API):
    """Hotspots client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/hotspots
    """

    base_path = 'hotspots'

    @filter_modes_api
    def all(self, params: Optional[dict]):
        """Yield all hotspots.

        Args:
            params: Filter mode params.
        """
        return self.client.fetch_all(params=params if params else None)

    def hotspot_for_address(self, address: str):
        """Yield hotspots for a hotspot."""
        return self.client.get(path=f'/{address}')

    def hotspots_for_name(self, name: str):
        """Return a hotspot identified by hotspot_id."""
        if len(name.split(' ')) == 3:
            name = '-'.join(name.split(' ')).lower()
        return self.client.get(path=f'/name/{name}')

    def hotspots_search_by_name(self, name: str):
        """Return a hotspot identified by hotspot_id."""
        return self.client.get(path='/name', params={'search': name})

    def hotspots_search_by_geo(self, swlat: float, swlon: float, nelat: float, nelon: float):
        """Return a hotspot identified by hotspot_id."""
        return self.client.get(
            path='/location/box',
            params={
                'swlat': swlat,
                'swlon': swlon,
                'nelat': nelat,
                'nelon': nelon,
            })

    def hotspots_by_hex(self, h3_index: str):
        """Return a hotspot identified by hotspot_id."""
        return self.client.get(path=f'/hex/{h3_index}')

    def get_hotspot_activity(self, address: str):
        """Return a hotspot identified by hotspot_id."""
        return self.client.fetch_all(path=f'/{address}/activity')

    @filter_transaction_types_api
    def get_hotspot_activity_counts(self, address: str, params: Optional[dict]):
        """Return a hotspot identified by hotspot_id."""
        return self.client.get(path=f'/{address}/activity/count', params=params if params else None)

    @time_filterable_api
    def get_hotspot_challenges(self, address: str, params: Optional[dict]):
        """Return a hotspot identified by hotspot_id."""
        return self.client.fetch_all(path=f'/{address}/challenges', params=params if params else None)

    @time_filterable_api
    def get_hotspot_rewards(self, address: str, params: Optional[dict]):
        """Return a hotspot identified by hotspot_id."""
        return self.client.fetch_all(path=f'/{address}/rewards', params=params if params else None)

    @time_filterable_api
    def get_hotspot_rewards_total(self, address: str, params: Optional[dict]):
        """Return a hotspot identified by hotspot_id."""
        return self.client.get(path=f'/{address}/rewards/sum', params=params if params else None)

    def get_hotspot_witnesses(self, address: str):
        """Return a hotspot identified by hotspot_id."""
        return self.client.get(path=f'/{address}/witnesses')

    def get_hotspot_witnessed(self, address: str):
        """Return a hotspot identified by hotspot_id."""
        return self.client.get(path=f'/{address}/witnessed')
