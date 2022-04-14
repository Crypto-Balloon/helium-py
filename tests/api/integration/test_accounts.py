"""Tests for Accounts client."""
import pytest

from helium_py.api import Accounts


@pytest.mark.integration
def test_accounts():
    """Initial integration tests for accounts.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    accounts = Accounts()
    random_account = '13E5hct3JbobrikGyo6FiUdhusYVZ2c8EQhoCZdw6m5DoS3aWs7'
    random_validator_account = '13bNBZAxmhwzrLySVH7pwzXQGJodPLhXEV4kKAC6yQ1PX6FbDEs'
    random_oui_account = '13i2S7ieX6BCgsBVJADyWtdAVoNPZbgpz5JxUpmPSUiAvstGrrr'
    assert 'balance' in next(accounts.all())
    assert 'balance' in accounts.richest()[0]
    assert 'balance' in accounts.account_for_address(random_account)
    assert 'block_added' in next(accounts.hotspots_for_account(random_account))
    assert 'block_added' in next(accounts.validators_for_account(random_validator_account))
    assert 'oui' in next(accounts.ouis_for_account(random_oui_account))
    assert 'type' in next(accounts.get_account_activity(random_account))
    assert 'add_gateway_v1' in accounts.get_account_activity_counts(random_account)
    assert accounts.get_account_elections(random_account) == []
    assert 'hash' in next(accounts.pending_transactions_for_account(random_account))
    # TODO:  Rewards issues make these fail somewhat regularly
    # assert 'amount' in next(accounts.get_account_rewards(
    #     random_account, min_time=datetime.now() - timedelta(days=1)))
    # assert 'avg' in accounts.get_account_rewards_total(
    #     random_account, min_time=datetime.now() - timedelta(days=1))
    assert 'balance' in accounts.get_stats_for_account(random_account)['last_day'][0]
    assert 'challenger' in next(accounts.challenges_for_account(random_account))

    # TODO: This lookup tends to be very slow, and often 500s
    # assert 'hash' in next(accounts.get_account_activity(random_account))
