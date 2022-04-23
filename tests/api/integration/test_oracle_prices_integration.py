"""Tests for OraclePrices client."""

import logging

import pytest

from helium_py.api import OraclePrices

logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_oracle_prices():
    """Initial integration tests for oracle prices.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    oracle_prices = OraclePrices()

    assert 'price' in next(oracle_prices.all())

    assert 'price' in oracle_prices.get_current()

    oracle_address = '13CFFcmPtMvNQCpWQRXCTqXPnXtcsibDWVwiQRKpUCt4nqtF7RE'
    assert 'block_height' in next(oracle_prices.all_activity_for_oracle(address=oracle_address))

    assert 'type' in next(oracle_prices.all_activity())

    assert 'stddev' in oracle_prices.get_stats()

    try:
        assert all([key in next(oracle_prices.predictions()) for key in ('time', 'price')])
    except (IndexError, StopIteration):
        logger.info('No predictions returned')

    assert oracle_prices.get_price_at_block(1167890)['price'] == 3888590000
