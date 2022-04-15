"""Balance class for converting between currency types."""
from decimal import Decimal
from typing import Optional, Union

from ..api import OraclePrices
from .exceptions import (
    MixedCurrencyTypeError,
    UnsupportedCurrencyConversionError,
    UnsupportedCurrencyError,
)
from .types import (
    ALL_CURRENCY_TYPES,
    DATA_CREDITS,
    NETWORK_TOKENS,
    TEST_NETWORK_TOKENS,
    US_DOLLARS,
)

DC_TO_USD_MULTIPLIER = Decimal('0.00001')


class Balance:
    """Represents a balance in a particular currency."""

    currency_type: str
    balance_in_currency: Decimal

    def __init__(self, balance_in_currency: Union[int, float, Decimal], currency_type: str):
        """Initialize balance with a currency type and amount."""
        if currency_type not in ALL_CURRENCY_TYPES:
            raise UnsupportedCurrencyError()
        if not isinstance(balance_in_currency, Decimal):
            balance_in_currency = Decimal(str(balance_in_currency))
        self.balance_in_currency = balance_in_currency
        self.currency_type = currency_type

    def __eq__(self, other):
        """Compare to see if two balances are equal."""
        return self.currency_type == other.currency_type and self.balance_in_currency == other.balance_in_currency

    def to_string(self, max_decimal_places: Optional[int] = None, show_ticker: Optional[bool] = True) -> str:
        """Convert Balance objects to a string."""
        number_string = f'{self.balance_in_currency:,.{max_decimal_places}f}' if max_decimal_places \
            else f'{self.balance_in_currency:,}'
        return ' '.join([number_string, self.currency_type]) if show_ticker else number_string

    def plus(self, balance: 'Balance') -> 'Balance':
        """Add two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError()
        return Balance((self.balance_in_currency + balance.balance_in_currency), self.currency_type)

    def minus(self, balance: 'Balance') -> 'Balance':
        """Subtract two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError()
        return Balance((self.balance_in_currency - balance.balance_in_currency), self.currency_type)

    def times(self, balance: 'Balance') -> 'Balance':
        """Multiply two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError()
        return Balance((self.balance_in_currency * balance.balance_in_currency), self.currency_type)

    def divided_by(self, balance: 'Balance') -> 'Balance':
        """Divide two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError()
        return Balance((self.balance_in_currency / balance.balance_in_currency), self.currency_type)

    def to_usd(self, oracle_price: Optional['Balance'] = None) -> 'Balance':
        """Convert a balance to US_DOLLARS."""
        if self.currency_type == US_DOLLARS:
            return self
        if oracle_price is None:
            oracle_price = Balance(OraclePrices().get_current()['price'], US_DOLLARS)
        if self.currency_type == DATA_CREDITS:
            return Balance(self.balance_in_currency * DC_TO_USD_MULTIPLIER, US_DOLLARS)
        if self.currency_type == NETWORK_TOKENS:
            return Balance(self.balance_in_currency * oracle_price.balance_in_currency, US_DOLLARS)
        if self.currency_type == TEST_NETWORK_TOKENS:
            return Balance(self.balance_in_currency * oracle_price.balance_in_currency, US_DOLLARS)
        raise UnsupportedCurrencyConversionError()

    def to_network_tokens(self, oracle_price: Optional['Balance'] = None) -> 'Balance':
        """Convert a balance to NETWORK_TOKENS."""
        if self.currency_type == NETWORK_TOKENS:
            return self
        if oracle_price is None:
            oracle_price = Balance(OraclePrices().get_current()['price'], US_DOLLARS)
        return Balance(self.to_usd(oracle_price).balance_in_currency / oracle_price.balance_in_currency, NETWORK_TOKENS)

    def to_test_network_tokens(self, oracle_price: Optional['Balance'] = None) -> 'Balance':
        """Convert a balance to TEST_NETWORK_TOKENS."""
        if self.currency_type == TEST_NETWORK_TOKENS:
            return self
        if oracle_price is None:
            # TODO: This should go to testnet
            oracle_price = Balance(OraclePrices().get_current()['price'], US_DOLLARS)
        return Balance(self.to_usd(
            oracle_price).balance_in_currency / oracle_price.balance_in_currency, TEST_NETWORK_TOKENS)

    def to_data_credits(self, oracle_price: Optional['Balance'] = None) -> 'Balance':
        """Convert a balance to DATA_CREDITS."""
        if self.currency_type == DATA_CREDITS:
            return self
        if self.currency_type == US_DOLLARS:
            return Balance(self.balance_in_currency / DC_TO_USD_MULTIPLIER, DATA_CREDITS)
        if oracle_price is None:
            oracle_price = Balance(OraclePrices().get_current()['price'], US_DOLLARS)
        if self.currency_type == NETWORK_TOKENS:
            return self.to_usd(oracle_price).to_data_credits(oracle_price)
        raise UnsupportedCurrencyConversionError()
