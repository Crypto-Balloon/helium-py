"""Blocks client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import time_filterable_api


class Blocks(API):
    """Blocks client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/blocks
    """

    base_path = 'blocks'

    def all(self) -> Generator[dict, None, None]:
        """Yield all block descriptions."""
        return self.client.fetch_all()

    @time_filterable_api
    def get_height(self, params: Optional[dict]) -> dict:
        """Return the current height of the blockchain."""
        return self.client.get(path='/height', params=params if params else None)

    def get_stats(self) -> dict:
        """Return stats for block production time."""
        return self.client.get(path='/stats')

    def get_block_descriptor_for_height(self, height: int) -> dict:
        """Return block descriptor for block at height."""
        return self.client.get(path=f'/{height}')

    def get_transactions_for_height(self, height: int) -> Generator[dict, None, None]:
        """Yield transactions for block at height."""
        return self.client.fetch_all(path=f'/{height}/transactions')

    def get_block_descriptor_for_hash(self, hash: str) -> dict:
        """Return block descriptor for block with provided hash."""
        return self.client.get(path=f'/hash/{hash}')

    def get_transactions_for_hash(self, hash: str) -> Generator[dict, None, None]:
        """Yield transactions for block with provided hash."""
        return self.client.fetch_all(path=f'/hash/{hash}/transactions')
