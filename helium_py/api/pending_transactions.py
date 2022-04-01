"""Pending Transactions client for Helium Blockchain API."""
from typing import Union

from ..transactions.transaction import Transaction
from .api import API


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

    def submit_transaction(self, txn: Union[str, Transaction]) -> dict:
        """Submit a transaction to the Helium Blockchain API.

        Args:
            txn: The base64 encoded transaction data str or Transaction object.
        """
        if not isinstance(txn, str):
            txn = txn.to_b64().decode('ascii')
        return self.client.post(path='', json={'txn': txn})
