"""Base API Class for Helium Blockchain API."""
from .client import Client


class API:
    """API Base class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/challenges
    """

    base_path = None
    _client: Client = None

    @property
    def client(self):
        """Return a client singleton per API."""
        if self._client is None:
            self._client = Client(base_path=self.base_path)
        return self._client
