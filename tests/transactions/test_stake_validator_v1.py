"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.transactions import StakeValidatorV1
from helium_py.transactions.utils import EMPTY_SIGNATURE

StakeValidatorV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def stake_validator(users):
    """Replace Placeholder Docstring."""
    return StakeValidatorV1(
        address=users.bob.keypair.address,
        owner=users.alice.keypair.address,
        stake=10,
    )


def test_create_stake_validator_transaction(stake_validator, users):
    """Replace Placeholder Docstring."""
    assert stake_validator.address.b58 == users.bob.b58
    assert stake_validator.owner.b58 == users.alice.b58
    assert stake_validator.stake == 10
    assert stake_validator.fee == 30000
    assert stake_validator.type == 'stake_validator_v1'


def test_serialize_returns_value(stake_validator):
    """Replace Placeholder Docstring."""
    assert len(stake_validator.serialize()) > 0


def test_serialize_to_base64(stake_validator):
    """Replace Placeholder Docstring."""
    assert StakeValidatorV1.from_b64(stake_validator.to_b64()).fee == 30000
    assert proto.BlockchainTxn.FromString(stake_validator.serialize()).stake_validator.fee == 30000


def test_deserializes_from_base64_string(stake_validator):
    """Replace Placeholder Docstring."""
    stake_validator.owner_signature = EMPTY_SIGNATURE
    serialized = stake_validator.to_b64()
    assert serialized == b'6gGOAQohATUaccIv7+wiMZNq0oJrIX7OOdn3f8bEljmSYpnDhpKVEiEBnGWdcjzB6BCnLnj33q9HNqh/EO+Pz8g' \
                         b'BALUzJ+fuSaQYCiJAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
                         b'AAAAAAAAAAAAAAACiw6gE='

    deserialized = StakeValidatorV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.address.b58 == stake_validator.address.b58
    assert deserialized.owner.b58 == stake_validator.owner.b58
    assert deserialized.stake == 10
    assert deserialized.fee == stake_validator.fee
    assert deserialized.owner_signature == stake_validator.owner_signature


def test_deserializes_from_base64_string_with_signatures(stake_validator):
    """Replace Placeholder Docstring."""
    deserialized = StakeValidatorV1.from_b64(stake_validator.to_b64())
    deserialized.calculate_fee()
    assert deserialized.address.b58 == stake_validator.address.b58
    assert deserialized.owner.b58 == stake_validator.owner.b58
    assert deserialized.stake == 10
    assert deserialized.fee == stake_validator.fee
    assert deserialized.owner_signature == stake_validator.owner_signature


def test_signing_adds_signature(stake_validator, users):
    """Replace Placeholder Docstring."""
    signed_transaction = stake_validator.sign(owner=users.bob.keypair)
    assert signed_transaction.owner_signature is not None
    assert len(signed_transaction.owner_signature) == 64


def test_does_not_calculate_fees_if_provided(users):
    """Replace Placeholder Docstring."""
    stake_validator = StakeValidatorV1(
        address=users.bob.keypair.address,
        owner=users.alice.keypair.address,
        stake=10,
        fee=70000,
    )
    assert stake_validator.fee == 70000
