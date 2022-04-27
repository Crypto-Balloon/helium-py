"""Tests for Client."""
from datetime import datetime
from unittest import mock

from requests import Response, Session

from helium_py.api import HELIUM_API_DEFAULT_HOST, Blocks

tx_instance = Blocks()
base_path = Blocks.base_path


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
def test_get_height(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}, {'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_height(
        min_time=datetime(2021, 1, 1, 1, 0, 0, 0),
        max_time=datetime(2022, 1, 1, 1, 0, 0, 0)
    )
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/height/',
                                     params={
                                         'min_time': '2021-01-01T01:00:00',
                                         'max_time': '2022-01-01T01:00:00'
                                     })


@mock.patch.object(Session, 'get')
def test_get_stats(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_stats()
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/stats/', params={})


@mock.patch.object(Session, 'get')
def test_get_block_descriptor_for_height(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_block_descriptor_for_height(1)
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/1/', params={})


@mock.patch.object(Session, 'get')
def test_validators_for_account(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_transactions_for_height(1)
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/1/transactions/', params={})


@mock.patch.object(Session, 'get')
def test_get_block_descriptor_for_hash(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_block_descriptor_for_hash('some_hash')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/hash/some_hash/', params={})


@mock.patch.object(Session, 'get')
def test_get_transactions_for_hash(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_transactions_for_hash('some_hash')
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(
        f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/hash/some_hash/transactions/', params={})
