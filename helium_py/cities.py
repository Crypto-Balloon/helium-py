"""Cities client for Helium Blockchain API."""

from typing import Optional

from .client import Client


class Cities(Client):
    """Cities client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/cities
    """

    base_path = 'cities'
    VALID_FILTER_MODES = {
        'full',
        'dataonly',
        'light',
    }

    def all(self, search: Optional[str] = None, **kwargs):
        """Yield all cities.

        Args:
            search: Search term.
        """
        return super().all(params={'search': search} if search else None, **kwargs)

    def hotspots_for_id(self, city_id: str, filter_modes: Optional[str] = None, **kwargs):
        """Yield hotspots for a city."""
        if filter_modes and not all([mode in self.VALID_FILTER_MODES for mode in filter_modes.split(',')]):
            raise ValueError(f'One or more of {filter_modes} not in {self.VALID_FILTER_MODES}')
        return super().all(
            path=f'/{city_id}/hotspots',
            params={'filter_modes': filter_modes} if filter_modes else None,
            **kwargs
        )

    def get_by_id(self, city_id: str):
        """Return a city identified by city_id.

        Args:
            city_id: The id for a city in the API.
        """
        return list(self.all(path=f'/{city_id}'))[0]
