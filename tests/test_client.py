"""Tests for Client."""

import pytest

from requests.exceptions import HTTPError

from helium_py import Client


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
