"""Cities client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import filter_modes_api


class Cities(API):
    """Cities client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/cities
    """

    base_path = 'cities'

    def all(self, search: Optional[str] = None) -> Generator[dict, None, None]:
        """Yield all cities.

        Args:
            search: Search term.

        Returns:
            All cities found by calling the api.
        """
        return self.client.fetch_all(params={'search': search} if search else None)

    @filter_modes_api
    def hotspots_for_id(self, city_id: str, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield hotspots for provided city_id.

        Args:
            city_id: The id for a city in the API.
            params: Params for filter_modes_api decorator
        """
        return self.client.fetch_all(
            path=f'/{city_id}/hotspots',
            params=params if params else None
        )

    def get_by_id(self, city_id: str) -> dict:
        """Return city identified by provided city_id.

        Args:
            city_id: The id for a city in the API.
        """
        return self.client.get(path=f'/{city_id}')
