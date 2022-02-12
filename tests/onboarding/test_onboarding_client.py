"""Tests for OnboardingClient."""
from helium_py.onboarding.client import OnboardingClient

some_hotspot = '11GsHnL2T2XMV2XnwoH3gcbwwGgGTsxa6xcwxK4rnscg4oE1iEP'


def test_client_integration():
    """Initial integration tests for Onboarding Client."""
    client = OnboardingClient()
    assert 'maker' in client.get_onboarding_record(some_hotspot)
    assert 'locationNonceLimit' in client.get_makers()[0]
    assert 'version' in client.get_firmware()
    # TODO: Test Payment Transaction
    # client.post_payment_transaction("some address", "some_txn_hash")
