"""Pending Transactions client for Helium Blockchain API."""
from .api import API


class PendingTransactions(API):
    """Pending Transactions client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/pending-transactions
    """

    base_path = 'pending_transactions'

    def get_status(self, transaction_hash: str):
        """Yield transaction status details for a particular hash.

        Args:
            transaction_hash: The transaction hash to fetch pending transaction details.
        """
        return self.client.get(path=f'/{transaction_hash}')

    def submit_transaction(self, transaction_hash: str, txn: str):
        """Submit a transaction.

        Args:
            txn: A base64 encoded transaction.
        """
        return self.client.post(path=f'/{transaction_hash}', json={'txn': txn})
