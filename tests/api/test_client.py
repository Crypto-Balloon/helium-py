"""Tests for Client."""
from unittest import mock

import pytest
from requests import Response, Session
from requests.exceptions import HTTPError

from helium_py.api import Client


def test_client_takes_custom_host():
    """Test client post method."""
    client = Client('test_host')
    assert client.host == 'test_host'


def test_client_takes_custom_port():
    """Test that client allows custom port."""
    client = Client(port=1234)
    assert client.port == 1234


def test_client_takes_custom_user_agent():
    """Test that client allows custom user agent."""
    client = Client(user_agent='test_agent')
    assert client.user_agent == 'test_agent'


@pytest.mark.integration
def test_client_cursor_cache():
    """Test that client cursor cache populated when moving across pages."""
    client = Client()
    cities = client.fetch_all('/cities')
    # This should get us onto other page(s)
    for i in range(250):
        next(cities)
    assert len(client._page_cache.keys()) > 0
    cities = client.fetch_all('/cities')
    for i in range(250):
        next(cities)


def test_client_post(mocker):
    """Test client post method."""
    client = Client()
    with pytest.raises(HTTPError):
        client.post(path='foo', json=None)

    mocker.patch('requests.Session')
    client = Client()

    # Does not raise
    assert client.post(path='foo', json=None)


def test_client_get_next_page_from_cache():
    """Test client fetching from cache."""
    client = Client()
    client._page_cache = {'some_cursor': {'some': 'data'}}
    next_page = client.get_next_page({'cursor': 'some_cursor'}, 'some_api_path', {'cursor': 'some_cursor'})
    assert next_page == {'some': 'data'}


@mock.patch.object(Session, 'get')
def test_client_get_paged_data_from_cache(mock_get):
    """Test client fetching paginated data from cache."""
    client = Client()
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}], 'cursor': '12345'}
    client._page_cache = {'12345': {'data': [{'some': 'data too'}]}}
    mock_get.return_value = mock_response
    response = client.fetch_all('some_path')

    assert next(response) == {'some': 'data'}
    assert next(response) == {'some': 'data too'}


@mock.patch.object(Session, 'get')
def test_client_get_paged_data_from_http(mock_get):
    """Test client paginated data from http (cache misses)."""
    client = Client()
    mock_response = mock.Mock(spec=Response)
    mock_response.json.side_effect = ({'data': [{'some': 'data'}], 'cursor': '12345'}, {'data': {'some': 'data too'}})
    mock_get.return_value = mock_response
    response = client.fetch_all('some_path')

    assert next(response) == {'some': 'data'}
    assert next(response) == {'some': 'data too'}
    with pytest.raises(StopIteration):
        next(response)
