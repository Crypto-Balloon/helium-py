"""Tests for Client."""
from unittest import mock

from requests import Response, Session

from helium_py.api import HELIUM_API_DEFAULT_HOST, PendingTransactions
from helium_py.transactions.transaction import Transaction

tx_instance = PendingTransactions()
base_path = PendingTransactions.base_path


@mock.patch.object(Session, 'get')
def test_get_status(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_status('some_tx_hash')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_tx_hash/', params={})


@mock.patch.object(Session, 'post')
def test_submit_transaction_with_string(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.submit_transaction('some_transaction_payload')
    assert response == [{'some': 'data'}]
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/',
                                     json={'txn': 'some_transaction_payload'})


@mock.patch.object(Session, 'post')
def test_submit_transaction_with_transaction(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    mock_transaction = mock.Mock(spec=Transaction)
    mock_transaction.to_b64.return_value = b'hello'
    response = tx_instance.submit_transaction(mock_transaction)
    assert response == [{'some': 'data'}]
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/',
                                     json={'txn': 'hello'})
