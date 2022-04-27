"""Tests for Client."""
from unittest import mock

from requests import Response, Session

from helium_py.api import HELIUM_API_DEFAULT_HOST, Locations

tx_instance = Locations()
base_path = Locations.base_path


@mock.patch.object(Session, 'get')
def test_all(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_location('some_h3_index')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_h3_index/', params={})
