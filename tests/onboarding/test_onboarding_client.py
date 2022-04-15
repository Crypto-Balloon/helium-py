"""Tests for OnboardingClient."""
from unittest import mock

from helium_py.onboarding.client import OnboardingClient

some_hotspot = '11GsHnL2T2XMV2XnwoH3gcbwwGgGTsxa6xcwxK4rnscg4oE1iEP'


def test_client_integration():
    """Test basic client integration."""
    client = OnboardingClient()
    assert 'maker' in client.get_onboarding_record(some_hotspot)
    assert 'locationNonceLimit' in client.get_makers()[0]
    assert 'version' in client.get_firmware()


def test_client_integration_custom_host():
    """Test integration customizing hostname."""
    client = OnboardingClient(host='www.example.com')
    assert client.host == 'www.example.com'


def test_client_post_payment_transaction():
    """Test client posting payment transaction."""
    client = OnboardingClient()
    mock_client = mock.Mock()
    mock_client.post.return_value = 'hai'
    client._client = mock_client
    assert client.post_payment_transaction('some address', 'some_txn_hash') == 'hai'
