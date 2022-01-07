"""OUIs client for Helium Blockchain API."""
from .api import API


class OUIs(API):
    """OUIs client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/ouis/
    """

    base_path = 'ouis'

    def all(self):
        """Yield all price data."""
        return self.client.fetch_all()

    def get_oui(self, oui: int):
        """Yield all activity for specific oracle.

        Args:
            oui: The oracle addres to fetch activity for.
        """
        return list(self.client.fetch_all(path=f'/{oui}'))[0]

    def get_last(self):
        """Get price stats."""
        return list(self.client.fetch_all(path='/last'))[0]

    def get_stats(self):
        """Get price stats."""
        return list(self.client.fetch_all(path='/stats'))[0]
