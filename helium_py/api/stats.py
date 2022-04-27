"""Stats client for Helium Blockchain API."""

from typing import Optional

from .api import API


class Stats(API):
    """Stats client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/stats
    """

    base_path = 'stats'
    VALID_FORMAT = 'raw'

    def get_all(self) -> dict:
        """Get all stats."""
        return self.client.get()

    def get_token_supply(self, fmt: Optional[str] = None) -> dict:
        """Retrieve the Helium token supply.

        Args:
            fmt: Specify 'raw' to get a raw number, otherwise returns json.
        """
        if fmt and not fmt == self.VALID_FORMAT:
            raise ValueError(f'{fmt} not {self.VALID_FORMAT}')
        return self.client.get(path='/token_supply', params={'format': fmt} if fmt else None)
