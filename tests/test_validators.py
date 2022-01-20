"""Tests for Validators client."""
from datetime import datetime, timedelta

from helium_py import Validators


def test_validators():
    """Initial integration tests for validators.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    validators = Validators()

    low_seaweed_mandrill = '112QGCrTEzzVhZvFJ5eW83vWMZZSWPEx9AVQ7shpmFXfTeGLZkUb'
    some_random_election = '4iLXQC28me_s5m0Iph6zQUzuMjOCd_bVcxADN4QVNwA'

    assert 'block_added' in next(validators.all())
    # TODO: Enable when filter_modes ain't broken
    assert 'block_added' in validators.validator_for_address(low_seaweed_mandrill)['data']
    assert 'block_added' in validators.validators_for_name('Low Seaweed Mandrill')['data'][0]
    assert 'block_added' in validators.validators_search_by_name('Low Seaweed Man')['data'][0]

    assert 'hash' in next(validators.get_validator_activity(address=low_seaweed_mandrill))
    assert 'rewards' in next(validators.get_validator_activity(address=low_seaweed_mandrill, filter_types='rewards'))
    assert 'add_gateway_v1' in validators.get_validator_activity_counts(low_seaweed_mandrill)['data']
    # filter_types is documented but always returns an empty object as of 1-12-2022
    assert validators.get_validator_activity_counts(low_seaweed_mandrill,  filter_types='rewards')['data'] == {}

    assert 'unstaked' in validators.get_stats()['data']

    assert 'block_added' in validators.get_currently_elected_validators()['data'][0]
    assert 'block_added' in validators.get_elected_validators_by_height(1176943)['data'][0]
    assert 'block_added' in validators.get_elected_validators_by_election(some_random_election)['data'][0]

    assert 'amount' in next(validators.get_validator_rewards(
        low_seaweed_mandrill, min_time=datetime.now() - timedelta(days=30)))
    assert 'avg' in validators.get_validator_rewards_total(
        low_seaweed_mandrill, min_time=datetime.now() - timedelta(days=30))['data']
    assert 'avg' in validators.get_all_validator_rewards_total()['data']
