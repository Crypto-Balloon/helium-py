"""Tests for PendingTransactions client."""

import logging

from helium_py import PendingTransactions

logger = logging.getLogger(__name__)


def test_transactions():
    """Initial integration tests for transactions.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    pending_transactions = PendingTransactions()

    assert 'data' in pending_transactions.get_status('q7pnrm2LvPoZKclF4f2BB6AmcnD0SORECgq9VbNLir4')
