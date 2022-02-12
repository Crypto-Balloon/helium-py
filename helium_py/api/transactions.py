"""Transactions client for Helium Blockchain API."""
from .api import API


class Transactions(API):
    """Transactions client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/transactions/
    """

    base_path = 'transactions'

    def get_transaction(self, transaction_hash: str) -> dict:
        """Return transaction details for a particular hash.

        Args:
            transaction_hash: The transaction hash to fetch transaction details.
        """
        return self.client.get(path=f'/{transaction_hash}')
