"""Tests for Client."""
from unittest import mock

from requests import Session, Response

from helium_py.api import Accounts, HELIUM_API_DEFAULT_HOST

tx_instance = Accounts()
base_path = Accounts.base_path


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
def test_richest(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}, {'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.richest(limit=1)
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/rich/',
                                     params={'limit': '1'})


@mock.patch.object(Session, 'get')
def test_account_for_address(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.account_for_address('some_address')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_address/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_hotspots_for_account(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.hotspots_for_account('some_account')
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/hotspots/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_validators_for_account(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.validators_for_account('some_account')
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/validators/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_ouis_for_account(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.ouis_for_account('some_account')
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/ouis/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_get_roles(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_roles('some_account', limit=1)
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/roles/',
                                     params={'limit': '1'})


@mock.patch.object(Session, 'get')
def test_get_role_counts(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': {'some': 'data'}}
    mock_get.return_value = mock_response
    response = tx_instance.get_roles_counts('some_account')
    assert response == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/roles/count/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_get_account_elections(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_account_elections('some_account', limit=1)
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/elections/',
                                     params={'limit': '1'})


@mock.patch.object(Session, 'get')
def test_challenges_for_account(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.challenges_for_account('some_account', limit=1)
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/challenges/',
                                     params={'limit': '1'})


@mock.patch.object(Session, 'get')
def test_pending_transactions_for_account(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.pending_transactions_for_account('some_account')
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(
        f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/pending_transactions/', params={})


@mock.patch.object(Session, 'get')
def test_get_account_total(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_account_rewards('some_account')
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/rewards/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_get_account_rewards_total(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_account_rewards_total('some_account')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/rewards/sum/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_get_stats_for_account(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_stats_for_account('some_account')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_account/stats/',
                                     params={})
