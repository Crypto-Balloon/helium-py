"""Tests for Client."""
from unittest import mock

from requests import Response, Session

from helium_py.api import HELIUM_API_DEFAULT_HOST, OUIs

tx_instance = OUIs()
base_path = OUIs.base_path


@mock.patch.object(Session, 'get')
def test_all(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.all()
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/', params={})


@mock.patch.object(Session, 'get')
def test_get_oui(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_oui(1)
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/1/', params={})


@mock.patch.object(Session, 'get')
def test_get_last(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_last()
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/last/', params={})


@mock.patch.object(Session, 'get')
def test_get_stats(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_stats()
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/stats/', params={})
