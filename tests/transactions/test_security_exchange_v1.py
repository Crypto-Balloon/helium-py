"""Tests for SecurityExchangeV1."""
import pytest

from helium_py import proto
from helium_py.crypto.utils import EMPTY_SIGNATURE
from helium_py.transactions import SecurityExchangeV1

SecurityExchangeV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def security_exchange(users):
    """Fixture for Transaction class."""
    return SecurityExchangeV1(
        payer=users.bob.keypair.address,
        payee=users.alice.keypair.address,
        amount=10,
        nonce=1,
    )


def test_create_security_exchange_transaction(security_exchange, users):
    """Test create transaction."""
    assert security_exchange.payer.b58 == users.bob.b58
    assert security_exchange.payee.b58 == users.alice.b58
    assert security_exchange.amount == 10
    assert security_exchange.nonce == 1
    assert security_exchange.fee == 30000
    assert security_exchange.type == 'security_exchange_v1'


def test_serialize_returns_value(security_exchange):
    """Test serialize transaction."""
    assert len(security_exchange.serialize()) > 0


def test_serialize_to_base64(security_exchange):
    """Test serialize transaction to base64 and deserialize transaction."""
    assert SecurityExchangeV1.from_b64(security_exchange.to_b64()).fee == 30000
    assert proto.BlockchainTxn.FromString(security_exchange.serialize()).security_exchange.fee == 30000


def test_deserializes_from_base64_string(security_exchange):
    """Test deserialize transaction from base64."""
    # helium-js mutates the instance when adding empty signatures to calculate payment
    # and this is a reference b64 representation
    security_exchange.signature = EMPTY_SIGNATURE
    serialized = security_exchange.to_b64()
    assert serialized == b'cpABCiEBNRpxwi/v7CIxk2rSgmshfs452fd/xsSWOZJimcOGkpUSIQGcZZ1yPMHoEKcuePfer0c2qH8Q74' \
                         b'/PyAEAtTMn5+5JpBgKILDqASgBMkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
                         b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

    deserialized = SecurityExchangeV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.payer.b58 == security_exchange.payer.b58
    assert deserialized.payee.b58 == security_exchange.payee.b58
    assert deserialized.amount == 10
    assert deserialized.nonce == 1
    assert deserialized.fee == security_exchange.fee
    assert deserialized.signature == security_exchange.signature


def test_deserializes_from_base64_string_with_signatures(security_exchange):
    """Test deserialize transaction from base64 with signatures."""
    deserialized = SecurityExchangeV1.from_b64(security_exchange.to_b64())
    deserialized.calculate_fee()
    assert deserialized.payer.b58 == security_exchange.payer.b58
    assert deserialized.payee.b58 == security_exchange.payee.b58
    assert deserialized.amount == 10
    assert deserialized.nonce == 1
    assert deserialized.fee == security_exchange.fee
    assert deserialized.signature == security_exchange.signature


def test_signing_adds_signature(security_exchange, users):
    """Test signing adds signature."""
    signed_transaction = security_exchange.sign(payer=users.bob.keypair)
    assert signed_transaction.signature is not None
    assert len(signed_transaction.signature) == 64


def test_does_not_calculate_fees_if_provided(users):
    """Test fee not calculated if provided."""
    security_exchange = SecurityExchangeV1(
        payer=users.bob.keypair.address,
        payee=users.alice.keypair.address,
        amount=10,
        nonce=1,
        fee=12345,
    )
    assert security_exchange.fee == 12345
