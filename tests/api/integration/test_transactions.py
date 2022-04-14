"""Tests for Transactions client."""

import logging

import pytest

from helium_py.api import Transactions

logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_transactions():
    """Initial integration tests for transactions.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    transactions = Transactions()

    expected = {
        'type': 'payment_v2',
        'time': 1595980494,
        'payments':
            [{
                'payee': '13FkKYnwHPoa6F7K23jJ7j2WNg9cMPsznJ7i4c9ysCwLoS8vx3E',
                'amount': 100000000
            }],
        'payer': '14h5MCATzJAB88gGBph8YtPM9539FdyBnMdTt7sYxg4Ts1D1aW3',
        'nonce': 6,
        'height': 435251,
        'hash': 'bUc6-LQXdR6zOBaR_8TPWlf3THCpb4wI6WPXJHJfnYw',
        'fee': 35000
    }

    assert expected == transactions.get_transaction('bUc6-LQXdR6zOBaR_8TPWlf3THCpb4wI6WPXJHJfnYw')
