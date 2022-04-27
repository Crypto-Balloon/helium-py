"""Tests for Client."""
from unittest import mock

from requests import Response, Session

from helium_py.api import HELIUM_API_DEFAULT_HOST, Transactions

tx_instance = Transactions()
base_path = Transactions .base_path


@mock.patch.object(Session, 'get')
def test_get_transaction(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_transaction('some_tx_hash')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_tx_hash/', params={})
