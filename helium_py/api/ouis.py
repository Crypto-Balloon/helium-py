"""OUIs client for Helium Blockchain API."""
from typing import Generator

from .api import API


class OUIs(API):
    """OUIs client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/ouis/
    """

    base_path = 'ouis'

    def all(self) -> Generator[dict, None, None]:
        """Yield all ouis."""
        return self.client.fetch_all()

    def get_oui(self, address: int) -> dict:
        """Return information for a specific OUI.

        Args:
            address: The oui address to fetch information for.
        """
        return self.client.get(path=f'/{address}')

    def get_last(self) -> dict:
        """Return the last assigned OUI transaction."""
        return self.client.get(path='/last')

    def get_stats(self) -> dict:
        """Return stats for the registered OUIs."""
        return self.client.get(path='/stats')
