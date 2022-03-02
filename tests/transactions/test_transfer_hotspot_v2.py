"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.transactions import TransferHotspotV2

TransferHotspotV2.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def transfer(users):
    """Replace Placeholder Docstring."""
    txn = TransferHotspotV2(
        gateway=users.alice.keypair.address,
        new_owner=users.bob.keypair.address,
        owner=users.alice.keypair.address,
        nonce=1,
    )
    txn.sign(owner=users.alice.keypair)
    return txn


def test_create_payment_transaction(transfer, users):
    """Replace Placeholder Docstring."""
    assert transfer.gateway.b58 == users.alice.b58
    assert transfer.new_owner.b58 == users.bob.b58
    assert transfer.owner.b58 == users.alice.b58
    assert transfer.nonce == 1
    assert transfer.fee == 40000
    assert transfer.type == 'transfer_hotspot_v2'


def test_serialize_returns_value(transfer):
    """Replace Placeholder Docstring."""
    assert len(transfer.serialize()) > 0


def test_serialize_to_base64(transfer):
    """Replace Placeholder Docstring."""
    assert TransferHotspotV2.from_b64(transfer.to_b64()).nonce == 1
    assert proto.BlockchainTxn.FromString(transfer.serialize()).transfer_hotspot_v2.nonce == 1


def test_deserializes_from_base64_string(transfer):
    """Replace Placeholder Docstring."""
    serialized = transfer.to_b64()

    # TODO repr from helium-js
    # assert serialized == b'QpABCiEBNRpxwi/v7CIxk2rSgmshfs452fd/xsSWOZJimcOGkpUSIQGcZZ1yPMHoEKcuePfer0c2qH8Q74' \
    #                      b'/PyAEAtTMn5+5JpBgKILDqASgBMkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
    #                      b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    deserialized = TransferHotspotV2.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.gateway.b58 == transfer.gateway.b58
    assert deserialized.new_owner.b58 == transfer.new_owner.b58
    assert deserialized.owner.b58 == transfer.owner.b58
    assert deserialized.nonce == 1
    assert deserialized.fee == transfer.fee
    assert deserialized.owner_signature == transfer.owner_signature


def test_signing_adds_signature(transfer, users):
    """Replace Placeholder Docstring."""
    signed_transaction = transfer.sign(owner=users.alice.keypair)
    assert signed_transaction.owner_signature is not None
    assert len(signed_transaction.owner_signature) == 64
