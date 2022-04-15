"""Tests for Balance class."""
from helium_py.currency.balance import Balance
from helium_py.currency.exceptions import UnsupportedCurrencyError
from helium_py.currency.types import (
    DATA_CREDITS,
    NETWORK_TOKENS,
    TEST_NETWORK_TOKENS,
    US_DOLLARS,
)


def test_balance_class():
    """Tests for Balance class."""
    bal = Balance(5, US_DOLLARS)
    assert bal.balance_in_currency == 5
    assert bal.currency_type == US_DOLLARS


def test_balance_class_invalid_currency():
    """Test for invalid currency."""
    try:
        Balance(5, 'NOTACURR')
    except UnsupportedCurrencyError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyError for test.')


def test_balance_class_to_network_tokens():
    """Tests for Balance class to network tokens."""
    bal = Balance(5, US_DOLLARS)
    to_network_tokens = bal.to_network_tokens(oracle_price=Balance(5, US_DOLLARS))
    assert to_network_tokens.balance_in_currency == 1
    assert to_network_tokens.currency_type == NETWORK_TOKENS


def test_balance_class_to_test_network_tokens():
    """Tests for Balance class to test network tokens."""
    bal = Balance(5, US_DOLLARS)
    to_test_network_tokens = bal.to_test_network_tokens(oracle_price=Balance(10, US_DOLLARS))
    assert to_test_network_tokens.balance_in_currency == 0.5
    assert to_test_network_tokens.currency_type == TEST_NETWORK_TOKENS


def test_balance_class_to_data_credits():
    """Tests for Balance class to data credits."""
    bal = Balance(5, US_DOLLARS)
    to_data_credits = bal.to_data_credits()
    assert to_data_credits.balance_in_currency == 500000
    assert to_data_credits.currency_type == DATA_CREDITS


def test_balance_class_to_us_dollar():
    """Tests for Balance class to us dollars."""
    bal = Balance(5, US_DOLLARS)
    to_network_tokens = bal.to_network_tokens(oracle_price=Balance(5, US_DOLLARS))
    to_usd = to_network_tokens.to_usd(oracle_price=Balance(5, US_DOLLARS))
    assert to_usd.balance_in_currency == 5
    assert to_usd.currency_type == US_DOLLARS
    assert Balance(5.512525251252, US_DOLLARS).to_string() == '5.512525251252 USD'
    assert Balance(5.512525251252, US_DOLLARS).to_string(max_decimal_places=2) == '5.51 USD'
    assert Balance(55125252.52512, US_DOLLARS).to_string() == '55,125,252.52512 USD'
    # TODO: Rounds up - desired?
    assert Balance(55125252.52512, US_DOLLARS).to_string(max_decimal_places=2) == '55,125,252.53 USD'
