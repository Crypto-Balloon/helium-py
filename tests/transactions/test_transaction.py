"""Replace placeholder docstrings."""
from copy import copy

from helium_py.transactions.transaction import Transaction, ChainVars


def test_config_default_values():
    """Replace placeholder docstrings."""
    assert Transaction.transaction_fee_multiplier == 0
    assert Transaction.dc_payload_size == 24
    assert Transaction.staking_fee_txn_add_gateway_v1 == 1
    assert Transaction.staking_fee_txn_assert_location_v1 == 1


def test_config_uses_chain_vars():
    """Replace placeholder docstrings."""
    chain_vars = ChainVars(
        transaction_fee_multiplier=100,
        dc_payload_size=48,
        staking_fee_txn_add_gateway_v1=1000,
        staking_fee_txn_assert_location_v1=2000
    )
    old_vars = copy(Transaction.config())
    Transaction.config(chain_vars)
    assert Transaction.transaction_fee_multiplier == 100
    assert Transaction.dc_payload_size == 48
    assert Transaction.staking_fee_txn_add_gateway_v1 == 1000
    assert Transaction.staking_fee_txn_assert_location_v1 == 2000
    Transaction.config(old_vars)


def test_config_without_chain_vars():
    """Replace placeholder docstrings."""
    Transaction.config()
    assert Transaction.transaction_fee_multiplier == 0


def test_string_type():
    """Replace placeholder docstrings."""
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
