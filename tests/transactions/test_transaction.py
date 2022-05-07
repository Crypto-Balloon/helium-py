"""Tests for Transaction class."""
from unittest import mock

from requests import Response, Session

from helium_py.transactions.transaction import Transaction


def test_config_default_values():
    """Test config defaults."""
    assert Transaction.transaction_fee_multiplier == 5000
    assert Transaction.dc_payload_size == 24
    assert Transaction.staking_fee_txn_assert_location_v1 == 1000000
    assert Transaction.staking_fee_txn_add_gateway_v1 == 4000000


def test_config_uses_chain_vars():
    """Test config uses provided chain variables."""
    old_vars = Transaction.config()
    Transaction.config(
        transaction_fee_multiplier=100,
        dc_payload_size=48,
        staking_fee_txn_add_gateway_v1=1000,
        staking_fee_txn_assert_location_v1=2000
    )
    assert Transaction.transaction_fee_multiplier == 100
    assert Transaction.dc_payload_size == 48
    assert Transaction.staking_fee_txn_add_gateway_v1 == 1000
    assert Transaction.staking_fee_txn_assert_location_v1 == 2000
    Transaction.config(**old_vars)


def test_config_without_chain_vars():
    """Test config without chain vars returns current config."""
    Transaction.config()
    assert Transaction.transaction_fee_multiplier == 5000


@mock.patch.object(Session, 'get')
def test_fetch_config_from_api(mock_get):
    """Test config without chain vars returns current config."""
    mock_response = mock.Mock(spec=Response)
    mock_response.json.return_value = {'data': {
            'txn_fee_multiplier': 1,
            'dc_payload_size': 2,
            'staking_fee_txn_assert_location_v1': 3,
            'staking_fee_txn_add_gateway_v1': 4
        }}
    mock_get.return_value = mock_response
    Transaction.fetch_config()
    assert Transaction.transaction_fee_multiplier == 1
    assert Transaction.dc_payload_size == 2
    assert Transaction.staking_fee_txn_assert_location_v1 == 3
    assert Transaction.staking_fee_txn_add_gateway_v1 == 4


def test_string_type():
    """Test that string type is deserialized properly."""
    serialized_add_gw_txn = 'CrMCCiEBHph7m4n8je5IHzLmg544qkxQb+K1g3efKHufp0dKURYSIQGySNPajUxhsIp5CIsV2et+Kx1Xw' \
                            'ECUOCUd4BBjekSeQxpAYCTigGLV8ch+5WmbbhO14L7mM2Djhidhl19b5zgE/Uo7T7j8OSa+Egir7oX3gkh' \
                            's8frsUT4uNDrfi48ezN3tAiJAAqe3gcYc5sj3XWl0oUyVbHFhZSRu8gDcXV5+IeN6jwK6amQNm4clp1wR/' \
                            'JprHbI3kYbinzEwWIqzQs6miKWiByohAS85rAe4whjJEsnzyByyxV8UPRHvjl74cMb1+LadnbUjMkAAAAA' \
                            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO' \
                            'MC4Ag=='
    serialized_assert_v2 = 'mgLQAQo0ATEzTThkVWJ4eW1FM3h0aUFYc3pSa0dNbWV6TWhCUzhMaTd3RXNNb2pMZGI0U2R4YzR3YxI0AT' \
                           'E0OGQ4S1RSY0tBNUpLUGVrQmNLRmQ0S2Z2cHJ2RlJwakd0aXZodG1SbW5aOE1GWW5QMxo0ATEzTThkVWJ4' \
                           'eW1FM3h0aUFYc3pSa0dNbWV6TWhCUzhMaTd3RXNNb2pMZGI0U2R4YzR3YyIJsomesignaturKg2yiZ6i2F' \
                           '6uyKCdq26tMghsb2NhdGlvbjgBQAJIA1AFWAQ='

    assert Transaction.string_type(serialized_add_gw_txn) == 'addGateway'
    assert Transaction.string_type(serialized_assert_v2) == 'assertLocationV2'


def test_orig_kwarg_gt0_or_none_gt0():
    """Test that orig_kwarg_gt0_or_none returns properly."""
    class TestTransaction(Transaction):
        fields = {
            'integers': ['key']
        }
        defaults = {}
    assert TestTransaction(key=1).orig_kwarg_gt0_or_none('key') == 1


def test_orig_kwarg_gt0_or_none_eq0():
    """Test that orig_kwarg_gt0_or_none returns properly."""
    class TestTransaction(Transaction):
        fields = {
            'integers': ['key']
        }
        defaults = {}
    assert TestTransaction(key=0).orig_kwarg_gt0_or_none('key') is None
