"""Cities client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import filter_modes_api


class Cities(API):
    """Cities client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/cities
    """

    base_path = 'cities'
    VALID_FILTER_MODES = {
        'full',
        'dataonly',
        'light',
    }

    def all(self, search: Optional[str] = None):
        """Yield all cities.

        Args:
            search: Search term.
        """
        return self.client.fetch_all(params={'search': search} if search else None)

    @filter_modes_api
    def hotspots_for_id(self, city_id: str, params: Optional[dict]):
        """Yield hotspots for a city."""
        return self.client.fetch_all(
            path=f'/{city_id}/hotspots',
            params=params if params else None
        )

    def get_by_id(self, city_id: str):
        """Return a city identified by city_id.

        Args:
            city_id: The id for a city in the API.
        """
        return list(self.client.fetch_all(path=f'/{city_id}'))[0]
