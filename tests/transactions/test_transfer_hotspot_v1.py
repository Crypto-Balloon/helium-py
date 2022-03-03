"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.transactions import TransferHotspotV1
from helium_py.crypto.utils import EMPTY_SIGNATURE

TransferHotspotV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def transfer(users):
    """Replace Placeholder Docstring."""
    return TransferHotspotV1(
        gateway=users.alice.keypair.address,
        buyer=users.bob.keypair.address,
        seller=users.alice.keypair.address,
        amount_to_seller=10,
        buyer_nonce=1,
    )


def test_create_transfer_transaction(transfer, users):
    """Replace Placeholder Docstring."""
    assert transfer.gateway.b58 == users.alice.b58
    assert transfer.buyer.b58 == users.bob.b58
    assert transfer.seller.b58 == users.alice.b58
    assert transfer.amount_to_seller == 10
    assert transfer.buyer_nonce == 1
    assert transfer.fee == 55000
    assert transfer.type == 'transfer_hotspot_v1'


def test_serialize_returns_value(transfer):
    """Replace Placeholder Docstring."""
    assert len(transfer.serialize()) > 0


def test_serialize_to_base64(transfer):
    """Replace Placeholder Docstring."""
    assert TransferHotspotV1.from_b64(transfer.to_b64()).amount_to_seller == 10
    assert proto.BlockchainTxn.FromString(transfer.serialize()).transfer_hotspot.amount_to_seller == 10


def test_deserializes_from_base64_string(transfer):
    """Replace Placeholder Docstring."""
    # helium-js mutates the instance when adding empty signatures to calculate payment
    # and this is a reference b64 representation
    transfer.seller_signature = EMPTY_SIGNATURE
    transfer.buyer_signature = EMPTY_SIGNATURE
    serialized = transfer.to_b64()

    # TODO repr from helium-js
    # assert serialized == b'QpABCiEBNRpxwi/v7CIxk2rSgmshfs452fd/xsSWOZJimcOGkpUSIQGcZZ1yPMHoEKcuePfer0c2qH8Q74' \
    #                      b'/PyAEAtTMn5+5JpBgKILDqASgBMkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
    #                      b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    deserialized = TransferHotspotV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.gateway.b58 == transfer.gateway.b58
    assert deserialized.buyer.b58 == transfer.buyer.b58
    assert deserialized.seller.b58 == transfer.seller.b58
    assert deserialized.amount_to_seller == 10
    assert deserialized.buyer_nonce == 1
    assert deserialized.fee == transfer.fee
    assert deserialized.seller_signature == transfer.seller_signature
    assert deserialized.buyer_signature == transfer.buyer_signature


def test_signing_adds_signature(transfer, users):
    """Replace Placeholder Docstring."""
    signed_transaction = transfer.sign(buyer=users.bob.keypair)
    assert signed_transaction.buyer_signature is not None
    assert len(signed_transaction.buyer_signature) == 64
