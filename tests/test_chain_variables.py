"""Tests for ChainVariables client."""

from helium_py import ChainVariables


def test_chain_variables():
    """Initial integration tests for chain variables.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    chain_vars = ChainVariables()

    assert 'poc_version' in chain_vars.get_all()['data']

    assert type(chain_vars.get_by_name('staking_fee_txn_oui_v1_per_address')['data']) is int

    activity = chain_vars.all_activity()
    assert next(activity)['nonce'] > next(activity)['nonce']
