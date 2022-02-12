"""Locations client for Helium Blockchain API."""
from .api import API


class Locations(API):
    """Locations client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/locations/
    """

    base_path = 'locations'

    def get_location(self, h3_index: str) -> dict:
        """Return location details for a provided h3 hex index.

        Args:
            h3_index: The h3 hex index to fetch location details.
        """
        return self.client.get(path=f'/{h3_index}')
