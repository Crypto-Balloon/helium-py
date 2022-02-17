"""Exceptions for Currency module."""


class UnsupportedCurrencyError(Exception):
    """Exception for unexpected conversion."""

    pass


class MixedCurrencyTypeError(Exception):
    """Exception for unexpected mixing of currency types."""

    pass


class UnsupportedCurrencyConversionError(Exception):
    """Exception for unexpected conversion."""

    pass
