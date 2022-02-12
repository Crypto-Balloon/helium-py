"""Base API Class for Helium Blockchain API."""
from typing import Optional

from .client import Client


class API:
    """Base API class for Helium Blockchain API.

    https://docs.helium.com/api/
    """

    base_path: Optional[str] = None
    _client: Optional[Client] = None

    @property
    def client(self) -> Client:
        """Return a client singleton per API."""
        if self._client is None:
            self._client = Client(base_path=self.base_path)
        return self._client
