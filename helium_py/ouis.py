"""OUIs client for Helium Blockchain API."""
from .api import API


class OUIs(API):
    """OUIs client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/ouis/
    """

    base_path = 'ouis'

    def all(self):
        """Yield all ouis."""
        return self.client.fetch_all()

    def get_oui(self, address: int):
        """Return information for a specific OUI.

        Args:
            address: The oui address to fetch information for.
        """
        return self.client.get(path=f'/{address}')

    def get_last(self):
        """Return the last assigned OUI transaction."""
        return self.client.get(path='/last')

    def get_stats(self):
        """Return stats for the registered OUIs."""
        return self.client.get(path='/stats')
