"""Tests for Balance class."""
from helium_py.currency.balance import Balance
from helium_py.currency.types import US_DOLLARS


def test_currency_types():
    """Tests for Balance class."""
    bal = Balance(5, US_DOLLARS)
    assert bal.balance_in_currency == 5
    assert bal.currency_type == US_DOLLARS
    assert bal.to_network_tokens(oracle_price=Balance(5, US_DOLLARS)).balance_in_currency == 1
