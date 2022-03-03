"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.transactions import TransferValidatorStakeV1
from helium_py.crypto.utils import EMPTY_SIGNATURE

TransferValidatorStakeV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def transfer_validator_stake(users):
    """Replace Placeholder Docstring."""
    return TransferValidatorStakeV1(
        old_address=users.bob.keypair.address,
        new_address=users.alice.keypair.address,
        old_owner=users.bob.keypair.address,
        new_owner=users.alice.keypair.address,
        stake_amount=10,
        payment_amount=20,
    )


def test_create_transfer_validator_stake_transaction(transfer_validator_stake, users):
    """Replace Placeholder Docstring."""
    assert transfer_validator_stake.old_address.b58 == users.bob.b58
    assert transfer_validator_stake.new_address.b58 == users.alice.b58
    assert transfer_validator_stake.old_owner.b58 == users.bob.b58
    assert transfer_validator_stake.new_owner.b58 == users.alice.b58
    assert transfer_validator_stake.stake_amount == 10
    assert transfer_validator_stake.payment_amount == 20
    assert transfer_validator_stake.fee == 60000
    assert transfer_validator_stake.type == 'transfer_validator_stake_v1'


def test_serialize_returns_value(transfer_validator_stake):
    """Replace Placeholder Docstring."""
    assert len(transfer_validator_stake.serialize()) > 0


def test_serialize_to_base64(transfer_validator_stake):
    """Replace Placeholder Docstring."""
    assert TransferValidatorStakeV1.from_b64(transfer_validator_stake.to_b64()).stake_amount == 10
    assert proto.BlockchainTxn.FromString(
        transfer_validator_stake.serialize(),
    ).transfer_val_stake.stake_amount == 10


def test_deserializes_from_base64_string(transfer_validator_stake):
    """Replace Placeholder Docstring."""
    # helium-js mutates the instance when adding empty signatures to calculate payment
    # and this is a reference b64 representation
    transfer_validator_stake.old_owner_signature = EMPTY_SIGNATURE
    transfer_validator_stake.new_owner_signature = EMPTY_SIGNATURE
    serialized = transfer_validator_stake.to_b64()

    # TODO repr from helium-js
    assert serialized == (
        b'8gGYAgohATUaccIv7+wiMZNq0oJrIX7OOdn3f8bEljmSYpnDhpKVEiEBnGWdcjzB6BCnLnj33q9HNqh/EO+Pz8gBA'
        b'LUzJ+fuSaQaIQE1GnHCL+/sIjGTatKCayF+zjnZ93/GxJY5kmKZw4aSlSIhAZxlnXI8wegQpy54996vRzaofxDvj8/IAQC1Myfn7km'
        b'kKkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        b'MkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOODUA0AKSBQ='
    )
    deserialized = TransferValidatorStakeV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.old_address.b58 == transfer_validator_stake.old_address.b58
    assert deserialized.new_address.b58 == transfer_validator_stake.new_address.b58
    assert deserialized.old_owner.b58 == transfer_validator_stake.old_owner.b58
    assert deserialized.new_owner.b58 == transfer_validator_stake.new_owner.b58
    assert deserialized.stake_amount == transfer_validator_stake.stake_amount
    assert deserialized.payment_amount == transfer_validator_stake.payment_amount
    assert deserialized.old_owner_signature == transfer_validator_stake.old_owner_signature
    assert deserialized.new_owner_signature == transfer_validator_stake.new_owner_signature


def test_signing_adds_signature(transfer_validator_stake, users):
    """Replace Placeholder Docstring."""
    signed_transaction = transfer_validator_stake.sign(old_owner=users.bob.keypair)
    assert signed_transaction.old_owner_signature is not None
    assert len(signed_transaction.old_owner_signature) == 64


def test_does_not_calculate_fees_if_provided(users):
    """Replace Placeholder Docstring."""
    transfer_validator_stake = TransferValidatorStakeV1(
        address=users.bob.keypair.address,
        owner=users.alice.keypair.address,
        stake=10,
        fee=70000,
    )
    assert transfer_validator_stake.fee == 70000
