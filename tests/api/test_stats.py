"""Tests for Client."""
from unittest import mock

import pytest
from requests import Response, Session

from helium_py.api import HELIUM_API_DEFAULT_HOST, Stats

tx_instance = Stats()
base_path = Stats.base_path


@mock.patch.object(Session, 'get')
def test_get_all(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': {'some': 'data'}}
    mock_get.return_value = mock_response
    response = tx_instance.get_all()
    assert response == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/', params={})


@mock.patch.object(Session, 'get')
def test_get_token_supply(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': {'some': 'data'}}
    mock_get.return_value = mock_response
    response = tx_instance.get_token_supply()
    assert response == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/token_supply/', params={})


@mock.patch.object(Session, 'get')
def test_get_token_supply_invalid_format(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': {'some': 'data'}}
    mock_get.return_value = mock_response
    with pytest.raises(ValueError):
        tx_instance.get_token_supply('bad_format')
