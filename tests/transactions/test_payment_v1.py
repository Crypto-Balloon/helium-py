"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.transactions import PaymentV1
from helium_py.crypto.utils import EMPTY_SIGNATURE

PaymentV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def payment(users):
    """Replace Placeholder Docstring."""
    return PaymentV1(
        payer=users.bob.keypair.address,
        payee=users.alice.keypair.address,
        amount=10,
        nonce=1,
    )


def test_create_payment_transaction(payment, users):
    """Replace Placeholder Docstring."""
    assert payment.payer.b58 == users.bob.b58
    assert payment.payee.b58 == users.alice.b58
    assert payment.amount == 10
    assert payment.nonce == 1
    assert payment.fee == 30000
    assert payment.type == 'payment_v1'


def test_serialize_returns_value(payment):
    """Replace Placeholder Docstring."""
    assert len(payment.serialize()) > 0


def test_serialize_to_base64(payment):
    """Replace Placeholder Docstring."""
    assert PaymentV1.from_b64(payment.to_b64()).fee == 30000
    assert proto.BlockchainTxn.FromString(payment.serialize()).payment.fee == 30000


def test_deserializes_from_base64_string(payment):
    """Replace Placeholder Docstring."""
    # helium-js mutates the instance when adding empty signatures to calculate payment
    # and this is a reference b64 representation
    payment.signature = EMPTY_SIGNATURE
    serialized = payment.to_b64()
    assert serialized == b'QpABCiEBNRpxwi/v7CIxk2rSgmshfs452fd/xsSWOZJimcOGkpUSIQGcZZ1yPMHoEKcuePfer0c2qH8Q74' \
                         b'/PyAEAtTMn5+5JpBgKILDqASgBMkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
                         b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    deserialized = PaymentV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.payer.b58 == payment.payer.b58
    assert deserialized.payee.b58 == payment.payee.b58
    assert deserialized.amount == 10
    assert deserialized.nonce == 1
    assert deserialized.fee == payment.fee
    assert deserialized.signature == payment.signature


def test_deserializes_from_base64_string_with_signatures(payment):
    """Replace Placeholder Docstring."""
    deserialized = PaymentV1.from_b64(payment.to_b64())
    deserialized.calculate_fee()
    assert deserialized.payer.b58 == payment.payer.b58
    assert deserialized.payee.b58 == payment.payee.b58
    assert deserialized.amount == 10
    assert deserialized.nonce == 1
    assert deserialized.fee == payment.fee
    assert deserialized.signature == payment.signature


def test_signing_adds_signature(payment, users):
    """Replace Placeholder Docstring."""
    signed_transaction = payment.sign(payer=users.bob.keypair)
    assert signed_transaction.signature is not None
    assert len(signed_transaction.signature) == 64
