"""Tests for decorators."""

import pytest

from helium_py.api.decorators import (
    bucket_api,
    filter_modes_api,
    filter_transaction_types_api,
)


def test_bucket_api_raises_on_invalid_bucket_type():
    """Test that an unexpected bucket types raises an exception."""
    @bucket_api
    def foo(obj, params, bucket):
        pass

    with pytest.raises(ValueError):
        foo(None, bucket='foo')


def test_filter_modes_api_raises_on_invalid_filter_mode():
    """Test that an unexpected filter mode raises an exception."""
    @filter_modes_api
    def foo(obj, params, filter_modes):
        pass

    with pytest.raises(ValueError):
        foo(None, filter_modes='foo')


def test_filter_modes_api_parses_filter_mode():
    """Test that @filter_modes_api parses valid filter_mode."""
    @filter_modes_api
    def foo(obj, params):
        assert params['filter_modes'] == 'full'

    foo(None, filter_modes='full')


def test_filter_transaction_types_api_raises_on_invalid_filter_type():
    """Test that an unexpected filter type raises an exception."""
    @filter_transaction_types_api
    def foo(obj, params, filter_types):
        pass

    with pytest.raises(ValueError):
        foo(None, filter_types='foo')


def test_filter_modes_api_parses_filter_type():
    """Test that @filter_transaction_types_api parses valid filter_type."""
    @filter_transaction_types_api
    def foo(obj, params):
        assert params['filter_types'] == 'add_gateway'

    foo(None, filter_types='add_gateway')
