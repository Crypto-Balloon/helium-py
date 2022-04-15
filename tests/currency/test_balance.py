"""Tests for Balance class."""
from unittest import mock

from helium_py.currency.balance import Balance, DC_TO_USD_MULTIPLIER
from helium_py.currency.exceptions import UnsupportedCurrencyError, MixedCurrencyTypeError, \
    UnsupportedCurrencyConversionError
from helium_py.currency.types import (
    DATA_CREDITS,
    NETWORK_TOKENS,
    TEST_NETWORK_TOKENS,
    US_DOLLARS,
    SECURITY_TOKENS,
)

FIVE_USD = Balance(5, US_DOLLARS)


def test_balance_class():
    """Tests for Balance class."""
    assert FIVE_USD.balance_in_currency == 5
    assert FIVE_USD.currency_type == US_DOLLARS


def test_balance_class_invalid_currency():
    """Test for invalid currency."""
    try:
        Balance(5, 'NOTACURR')
    except UnsupportedCurrencyError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyError for test.')


def test_balance_class_plus():
    """Test for invalid currency arithmatic."""
    assert Balance(10, US_DOLLARS) == FIVE_USD.plus(FIVE_USD)


def test_balance_class_invalid_plus_mixed_currency():
    """Test for invalid currency arithmatic."""
    try:
        FIVE_USD.plus(Balance(5, NETWORK_TOKENS))
    except MixedCurrencyTypeError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyError for test.')


def test_balance_class_minus():
    """Test for invalid currency arithmatic."""
    assert FIVE_USD == Balance(10, US_DOLLARS).minus(FIVE_USD)


def test_balance_class_invalid_minus_mixed_currency():
    """Test for invalid currency arithmatic."""
    try:
        FIVE_USD.minus(Balance(5, NETWORK_TOKENS))
    except MixedCurrencyTypeError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyError for test.')


def test_balance_class_times():
    """Test for invalid currency arithmatic."""
    assert Balance(25, US_DOLLARS) == FIVE_USD.times(FIVE_USD)


def test_balance_class_invalid_times_mixed_currency():
    """Test for invalid currency arithmatic."""
    try:
        FIVE_USD.times(Balance(5, NETWORK_TOKENS))
    except MixedCurrencyTypeError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyError for test.')


def test_balance_class_divided_by():
    """Test for invalid currency arithmatic."""
    assert FIVE_USD == Balance(25, US_DOLLARS).divided_by(FIVE_USD)


def test_balance_class_invalid_divided_by_mixed_currency():
    """Test for invalid currency arithmatic."""
    try:
        FIVE_USD.divided_by(Balance(5, NETWORK_TOKENS))
    except MixedCurrencyTypeError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyError for test.')


def test_balance_class_usd_to_network_tokens():
    """Tests for Balance class to network tokens."""
    to_network_tokens = FIVE_USD.to_network_tokens(oracle_price=FIVE_USD)
    assert to_network_tokens.balance_in_currency == 1
    assert to_network_tokens.currency_type == NETWORK_TOKENS


@mock.patch('helium_py.currency.balance.OraclePrices.get_current', mock.Mock(return_value={'price': 5}))
def test_balance_class_usd_to_network_tokens_using_api():
    """Tests for Balance class to us dollars."""
    to_network_tokens = FIVE_USD.to_network_tokens()
    assert to_network_tokens.balance_in_currency == 1


def test_balance_class_usd_to_test_network_tokens():
    """Tests for Balance class to test network tokens."""
    to_test_network_tokens = FIVE_USD.to_test_network_tokens(oracle_price=Balance(10, US_DOLLARS))
    assert to_test_network_tokens.balance_in_currency == 0.5
    assert to_test_network_tokens.currency_type == TEST_NETWORK_TOKENS


@mock.patch('helium_py.currency.balance.OraclePrices.get_current', mock.Mock(return_value={'price': 5}))
def test_balance_class_usd_to_test_network_tokens_using_api():
    """Tests for Balance class to us dollars."""
    to_network_tokens = FIVE_USD.to_test_network_tokens()
    assert to_network_tokens.balance_in_currency == 1


def test_balance_class_usd_to_data_credits():
    """Tests for Balance class to data credits."""
    to_data_credits = FIVE_USD.to_data_credits()
    assert to_data_credits.balance_in_currency == 500000
    assert to_data_credits.currency_type == DATA_CREDITS


@mock.patch('helium_py.currency.balance.OraclePrices.get_current', mock.Mock(return_value={'price': 5}))
def test_balance_class_usd_to_data_credits_using_api():
    """Tests for Balance class to data credits."""
    to_data_credits = Balance(1, NETWORK_TOKENS).to_data_credits()
    assert to_data_credits.balance_in_currency == 500000
    assert to_data_credits.currency_type == DATA_CREDITS


def test_balance_class_network_tokens_to_us_dollar():
    """Tests for Balance class to us dollars."""
    to_network_tokens = FIVE_USD.to_network_tokens(oracle_price=FIVE_USD)
    to_usd = to_network_tokens.to_usd(oracle_price=FIVE_USD)
    assert to_usd.balance_in_currency == 5
    assert to_usd.currency_type == US_DOLLARS
    assert Balance(5.512525251252, US_DOLLARS).to_string() == '5.512525251252 USD'
    assert Balance(5.512525251252, US_DOLLARS).to_string(max_decimal_places=2) == '5.51 USD'
    assert Balance(55125252.52512, US_DOLLARS).to_string() == '55,125,252.52512 USD'
    # TODO: Rounds up - desired?
    assert Balance(55125252.52512, US_DOLLARS).to_string(max_decimal_places=2) == '55,125,252.53 USD'


def test_balance_class_test_network_tokens_to_us_dollar():
    """Tests for Balance class to us dollars."""
    to_test_network_tokens = FIVE_USD.to_test_network_tokens(oracle_price=Balance(10, US_DOLLARS))
    to_usd = to_test_network_tokens.to_usd(oracle_price=Balance(10, US_DOLLARS))
    assert to_usd.balance_in_currency == 5


def test_balance_class_data_credits_to_us_dollar():
    """Tests for Balance class to us dollars."""
    to_data_credits = FIVE_USD.to_data_credits()
    to_usd = to_data_credits.to_usd(oracle_price=FIVE_USD)
    assert to_usd.balance_in_currency == 5


def test_balance_invalid_currency_to_us_dollar():
    """Tests for Balance class to us dollars."""
    st_bal = Balance(5, SECURITY_TOKENS)
    try:
        st_bal.to_usd(oracle_price=FIVE_USD)
    except UnsupportedCurrencyConversionError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyConversionError for test')


def test_balance_invalid_currency_to_data_credit():
    """Tests for Balance class to us dollars."""
    st_bal = Balance(5, SECURITY_TOKENS)
    try:
        st_bal.to_data_credits(oracle_price=FIVE_USD)
    except UnsupportedCurrencyConversionError:
        pass
    else:
        raise Exception('Expected UnsupportedCurrencyConversionError for test')


def test_balance_network_tokens_to_network_tokens():
    """Tests for Balance class to us dollars."""
    token_balance = Balance(5, NETWORK_TOKENS)
    assert token_balance == token_balance.to_network_tokens()


def test_balance_test_network_tokens_to_test_network_tokens():
    """Tests for Balance class to us dollars."""
    token_balance = Balance(5, TEST_NETWORK_TOKENS)
    assert token_balance == token_balance.to_test_network_tokens()


def test_balance_data_credits_to_data_credits():
    """Tests for Balance class to us dollars."""
    token_balance = Balance(5, DATA_CREDITS)
    assert token_balance == token_balance.to_data_credits()


def test_balance_network_tokens_to_data_credits():
    """Tests for Balance class to us dollars."""
    token_balance = Balance(1, NETWORK_TOKENS)
    dc_balance = token_balance.to_data_credits(oracle_price=FIVE_USD)
    assert dc_balance.balance_in_currency * DC_TO_USD_MULTIPLIER == \
           token_balance.to_usd(oracle_price=FIVE_USD).balance_in_currency


@mock.patch('helium_py.currency.balance.OraclePrices.get_current', mock.Mock(return_value={'price': 5}))
def test_balance_class_to_us_dollar_using_api():
    """Tests for Balance class to us dollars."""
    to_network_tokens = FIVE_USD.to_network_tokens(oracle_price=FIVE_USD)
    to_usd = to_network_tokens.to_usd()
    assert to_usd.balance_in_currency == 5
