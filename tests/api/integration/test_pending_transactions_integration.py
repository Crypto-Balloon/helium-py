"""Tests for PendingTransactions client."""

import logging

import pytest
from requests.exceptions import HTTPError

from helium_py.api import HELIUM_API_TESTNET_HOST, PendingTransactions

logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_transactions():
    """Initial integration tests for transactions.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    pending_transactions = PendingTransactions(host=HELIUM_API_TESTNET_HOST)

    assert pending_transactions.get_status('1USBZ2dUnxUT5pQ-mu4vYn-aDYurH0j0iHsBregQXJc')[0]['status'] == 'cleared'

    with pytest.raises(HTTPError):
        pending_transactions.submit_transaction(txn='bar')
