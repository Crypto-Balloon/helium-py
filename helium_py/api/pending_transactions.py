"""Pending Transactions client for Helium Blockchain API."""
from .api import API
from .constants import VALID_TRANSACTION_TYPES


class PendingTransactions(API):
    """Pending Transactions client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/pending-transactions
    """

    base_path = 'pending_transactions'

    def get_status(self, transaction_hash: str) -> dict:
        """Yield transaction status details for a particular hash.

        Args:
            transaction_hash: The transaction hash to fetch pending transaction details.
        """
        return self.client.get(path=f'/{transaction_hash}')

    def submit_transaction(self, transaction_hash: str, txn: str) -> dict:
        """Submit a transaction to the Helium Blockchain API.

        Args:
            transaction_hash: The transaction hash for transaction being submitted.
            txn: The base64 encoded transaction data.
        """
        if txn not in VALID_TRANSACTION_TYPES:
            raise ValueError(f"Transaction {txn} is not a valid transaction")
        return self.client.post(path=f'/{transaction_hash}', json={'txn': txn})
