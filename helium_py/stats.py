"""Stats client for Helium Blockchain API."""

from typing import Dict, Optional, Union

from .api import API


class Stats(API):
    """Stats client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/stats
    """

    base_path = 'stats'
    VALID_FORMAT = 'raw'

    def get_all(self):
        """Get all stats."""
        return list(self.client.fetch_all())[0]

    def get_token_supply(self, format: Optional[str] = None) -> Union[float, Dict]:
        """Retrieve the Helium token supply.

        Args:
            format: specify 'raw' to get a raw number, otherwise returns json.
        """
        if format and not format == self.VALID_FORMAT:
            raise ValueError(f'{format} not {self.VALID_FORMAT}')
        return list(self.client.fetch_all(
            path='/token_supply',
            params={'format': format} if format else None),
        )[0]
