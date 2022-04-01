"""Base API Class for Helium Blockchain API."""
from typing import Optional

from .client import Client


class API:
    """Base API class for Helium Blockchain API.

    https://docs.helium.com/api/
    """

    host: Optional[str] = None
    port: Optional[int] = None
    user_agent: Optional[str] = None
    base_path: Optional[str] = None
    _client: Optional[Client] = None

    def __init__(self, host=None, port=None, user_agent=None, base_path=None):
        """Allow for overriding API details at instantiation."""
        self.host = host if host else self.host
        self.port = port if port else self.port
        self.user_agent = user_agent if user_agent else self.user_agent
        self.base_path = base_path if base_path else self.base_path

    @property
    def client(self) -> Client:
        """Return a client singleton per API."""
        if self._client is None:
            self._client = Client(
                host=self.host,
                port=self.port,
                user_agent=self.user_agent,
                base_path=self.base_path,
            )
        return self._client
