"""Tests for PendingTransactions client."""

import logging

import pytest
from requests.exceptions import HTTPError

from helium_py.api import PendingTransactions

logger = logging.getLogger(__name__)


def test_transactions():
    """Initial integration tests for transactions.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    pending_transactions = PendingTransactions()

    assert pending_transactions.get_status('1USBZ2dUnxUT5pQ-mu4vYn-aDYurH0j0iHsBregQXJc')['status'] == 'cleared'

    with pytest.raises(HTTPError):
        pending_transactions.submit_transaction(txn='bar')
