"""Balance class for converting between currency types."""
from typing import Optional

from ..api import OraclePrices
from .exceptions import (
    MixedCurrencyTypeError,
    UnsupportedCurrencyConversionError,
)
from .types import (
    DATA_CREDITS,
    NETWORK_TOKENS,
    TEST_NETWORK_TOKENS,
    US_DOLLARS,
)

DC_TO_USD_MULTIPLIER = 0.00001


class Balance:
    """Represents a balance in a particular currency."""

    currency_type: str
    balance_in_currency: float

    def __init__(self, balance_in_currency: Optional[float], currency_type: str):
        """Initialize balance with a currency type and amount."""
        self.balance_in_currency = balance_in_currency or 0
        self.currency_type = currency_type

    # TODO: Finish the to_string method
    def to_string(self, max_decimal_places: Optional[int] = None, options: Optional[dict] = None) -> str:
        """Convert Balance objects to a string."""
        if not options:
            options = {}

        # TODO: Use Other Options
        # decimal_separator = options.get('decimal_separator', '.')
        # group_separator = options.get('group_separator', ',')
        show_ticker = options.get('show_ticker', True)

        number_string = f'{self.balance_in_currency}'

        return ' '.join([number_string, self.currency_type]) if show_ticker else number_string

    def plus(self, balance: 'Balance') -> 'Balance':
        """Add two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError
        return Balance((self.balance_in_currency + balance.balance_in_currency), self.currency_type)

    def minus(self, balance: 'Balance') -> 'Balance':
        """Subtract two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError
        return Balance((self.balance_in_currency - balance.balance_in_currency), self.currency_type)

    def times(self, balance: 'Balance') -> 'Balance':
        """Multiply two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError
        return Balance((self.balance_in_currency * balance.balance_in_currency), self.currency_type)

    def divided_by(self, balance: 'Balance') -> 'Balance':
        """Divide two Balances of the same type together."""
        if self.currency_type != balance.currency_type:
            raise MixedCurrencyTypeError
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
