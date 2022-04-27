"""Tests for Client."""
from unittest import mock

from requests import Response, Session

from helium_py.api import HELIUM_API_DEFAULT_HOST, Validators

tx_instance = Validators()
base_path = Validators .base_path


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
def test_validator_for_address(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.validator_for_address('some_address')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_address/', params={})


@mock.patch.object(Session, 'get')
def test_validators_for_name(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.validators_for_name('some-validator-name')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/name/some-validator-name/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_validators_for_name_with_spaces(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.validators_for_name('some validator name')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/name/some-validator-name/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_validators_search_by_name(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.validators_search_by_name('some validator name')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/name/',
                                     params={'search': 'some validator name'})


@mock.patch.object(Session, 'get')
def test_get_roles(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_roles('some_address')
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_address/roles/',
                                     params={})


@mock.patch.object(Session, 'get')
def test_get_roles_counts(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_roles_counts('some_address')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/some_address/roles/count/',
                                     params={})


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
def test_get_currently_elected_validators(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_currently_elected_validators()
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/elected/', params={})


@mock.patch.object(Session, 'get')
def test_get_elected_validators_by_height(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_elected_validators_by_height(1)
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/elected/1/', params={})


@mock.patch.object(Session, 'get')
def test_get_elected_validators_by_election(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_elected_validators_by_election('election_hash')
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/'
                                     f'elected/hash/election_hash/', params={})


@mock.patch.object(Session, 'get')
def test_get_validator_rewards(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_validator_rewards(1)
    assert next(response) == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/1/rewards/', params={})


@mock.patch.object(Session, 'get')
def test_get_validator_rewards_total(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_validator_rewards_total(1)
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/1/rewards/sum/', params={})


@mock.patch.object(Session, 'get')
def test_get_all_validator_rewards_total(mock_get):
    """Test that client allows custom port."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': [{'some': 'data'}]}
    mock_get.return_value = mock_response
    response = tx_instance.get_all_validator_rewards_total()
    assert response[0] == {'some': 'data'}
    mock_get.assert_called_once_with(f'https://{HELIUM_API_DEFAULT_HOST}:443/v1/{base_path}/rewards/sum/', params={})
