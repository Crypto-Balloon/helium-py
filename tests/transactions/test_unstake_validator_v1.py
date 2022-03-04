"""Tests for UnstakeValidatorV1."""
import pytest

from helium_py import proto
from helium_py.crypto.utils import EMPTY_SIGNATURE
from helium_py.transactions import UnstakeValidatorV1

UnstakeValidatorV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def unstake_validator(users):
    """Fixture for Transaction class."""
    return UnstakeValidatorV1(
        address=users.bob.keypair.address,
        owner=users.alice.keypair.address,
        stake_amount=10,
        stake_release_height=100,
    )


def test_create_unstake_validator_transaction(unstake_validator, users):
    """Test create transaction."""
    assert unstake_validator.address.b58 == users.bob.b58
    assert unstake_validator.owner.b58 == users.alice.b58
    assert unstake_validator.stake_amount == 10
    assert unstake_validator.fee == 30000
    assert unstake_validator.type == 'unstake_validator_v1'


def test_serialize_returns_value(unstake_validator):
    """Test serialize transaction."""
    assert len(unstake_validator.serialize()) > 0


def test_serialize_to_base64(unstake_validator):
    """Test serialize transaction to base64 and deserialize transaction."""
    assert UnstakeValidatorV1.from_b64(unstake_validator.to_b64()).stake_amount == 10
    assert proto.BlockchainTxn.FromString(unstake_validator.serialize()).unstake_validator.stake_amount == 10


def test_deserializes_from_base64_string(unstake_validator):
    """Test deserialize transaction from base64."""
    # helium-js mutates the instance when adding empty signatures to calculate payment
    # and this is a reference b64 representation
    unstake_validator.owner_signature = EMPTY_SIGNATURE
    serialized = unstake_validator.to_b64()

    # TODO repr from helium-js
    # assert serialized == b'6gGOAQohATUaccIv7+wiMZNq0oJrIX7OOdn3f8bEljmSYpnDhpKVEiEBnGWdcjzB6BCnLnj33q9HNqh/EO+Pz8g' \
    #                      b'BALUzJ+fuSaQYCiJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
    #                      b'AAAAAAAAAAAAAAACiw6gE='

    deserialized = UnstakeValidatorV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.address.b58 == unstake_validator.address.b58
    assert deserialized.owner.b58 == unstake_validator.owner.b58
    assert deserialized.stake_amount == unstake_validator.stake_amount
    assert deserialized.stake_release_height == unstake_validator.stake_release_height
    assert deserialized.owner_signature == unstake_validator.owner_signature


def test_signing_adds_signature(unstake_validator, users):
    """Test signing adds signature."""
    signed_transaction = unstake_validator.sign(owner=users.bob.keypair)
    assert signed_transaction.owner_signature is not None
    assert len(signed_transaction.owner_signature) == 64


def test_does_not_calculate_fees_if_provided(users):
    """Test fee not calculated if provided."""
    unstake_validator = UnstakeValidatorV1(
        address=users.bob.keypair.address,
        owner=users.alice.keypair.address,
        stake=10,
        fee=70000,
    )
    assert unstake_validator.fee == 70000
