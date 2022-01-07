"""Locations client for Helium Blockchain API."""
from .api import API


class Locations(API):
    """Locations client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/locations/
    """

    base_path = 'locations'

    def get_location(self, hex: str):
        """Yield location details for a particular h3 hex.

        Args:
            hex: The h3 hex location to fetch location details.
        """
        return self.client.get(path=f'/{hex}')
