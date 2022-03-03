"""Tests for PaymentV2."""
import pytest

from helium_py import proto
from helium_py.transactions import PaymentV2
from helium_py.transactions.payment import Payment

PaymentV2.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def payment(users):
    """Fixture for Transaction class."""
    return PaymentV2(
        payer=users.bob.keypair.address,
        payments=[
            Payment(
                payee=users.alice.keypair.address,
                amount=10,
                memo=b'mockmemo',
            ),
        ],
        nonce=1,
    )


def test_create_payment_transaction(payment, users):
    """Test create transaction."""
    assert payment.payer.b58 == users.bob.b58
    assert len(payment.payments) == 1
    assert payment.payments[0].payee.b58 == users.alice.b58
    assert payment.payments[0].amount == 10
    assert payment.payments[0].memo == b'mockmemo'
    assert payment.nonce == 1
    assert payment.fee == 35000
    assert payment.type == 'payment_v2'


def test_serialize_returns_value(payment):
    """Test serialize transaction."""
    assert len(payment.serialize()) > 0


def test_serialize_to_base64(payment):
    """Test serialize transaction to base64 and deserialize transaction."""
    assert PaymentV2.from_b64(payment.to_b64()).fee == 35000
    assert proto.BlockchainTxn.FromString(payment.serialize()).payment_v2.fee == 35000


def test_deserializes_from_base64_string(payment):
    """Test deserialize transaction from base64."""
    serialized = payment.to_b64()
    assert serialized == b'wgFaCiEBNRpxwi/v7CIxk2rSgmshfs452fd/xsSWOZJimcOGkpUSLwohAZxlnXI8wegQpy54996vRzaofxDvj8' \
                         b'/IAQC1Myfn7kmkEAoY7d6N29at2bZvGLiRAiAB'

    deserialized = PaymentV2.from_b64(serialized)
    assert deserialized.payer.b58 == payment.payer.b58
    assert deserialized.payments[0].payee.b58 == payment.payments[0].payee.b58
    assert deserialized.payments[0].amount == 10
    assert deserialized.nonce == 1
    assert deserialized.fee == payment.fee
    assert deserialized.signature == payment.signature


def test_deserializes_from_base64_string_with_signatures(payment):
    """Test deserialize transaction from base64 with signatures."""
    deserialized = PaymentV2.from_b64(payment.to_b64())
    assert deserialized.payer.b58 == payment.payer.b58
    assert deserialized.payments[0].payee.b58 == payment.payments[0].payee.b58
    assert deserialized.payments[0].amount == 10
    assert deserialized.nonce == 1
    assert deserialized.fee == payment.fee
    assert deserialized.signature == payment.signature


def test_signing_adds_signature(payment, users):
    """Test signing adds signature."""
    signed_transaction = payment.sign(payer=users.bob.keypair)
    assert signed_transaction.signature is not None
    assert len(signed_transaction.signature) == 64
