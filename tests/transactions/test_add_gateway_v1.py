"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.transactions.add_gateway_v1 import AddGatewayV1
from helium_py.transactions.transaction import ChainVars

AddGatewayV1.config(ChainVars(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
))


@pytest.fixture
def add_gateway(users):
    """Replace Placeholder Docstring."""
    return AddGatewayV1(
        owner=users.bob.keypair.address,
        gateway=users.alice.keypair.address,
        payer=users.bob.keypair.address,
    )


@pytest.fixture
def add_gateway_no_payer(users):
    """Replace Placeholder Docstring."""
    return AddGatewayV1(
        owner=users.bob.keypair.address,
        gateway=users.alice.keypair.address,
        payer=None,
    )


def test_create_add_gateway_transaction(add_gateway_no_payer, users):
    """Replace Placeholder Docstring."""
    assert add_gateway_no_payer.owner.b58 == users.bob.b58
    assert add_gateway_no_payer.gateway.b58 == users.alice.b58
    assert add_gateway_no_payer.fee == 45000
    assert add_gateway_no_payer.staking_fee == 4000000
    assert add_gateway_no_payer.type == 'add_gateway_v1'


def test_create_add_gateway_transaction_with_payer(add_gateway, users):
    """Replace Placeholder Docstring."""
    assert add_gateway.owner.b58 == users.bob.b58
    assert add_gateway.gateway.b58 == users.alice.b58
    assert add_gateway.payer.b58 == users.bob.b58
    assert add_gateway.fee == 65000
    assert add_gateway.staking_fee == 4000000
    assert add_gateway.type == 'add_gateway_v1'


def test_serialize_returns_value(add_gateway):
    """Replace Placeholder Docstring."""
    assert len(add_gateway.serialize()) > 0


def test_serialize_to_base64(add_gateway_no_payer):
    """Replace Placeholder Docstring."""
    assert AddGatewayV1.from_b64(add_gateway_no_payer.to_b64()).fee == 45000
    assert proto.BlockchainTxnAddGatewayV1.FromString(add_gateway_no_payer.serialize()).fee == 45000


def test_deserializes_from_base64_string(add_gateway):
    """Replace Placeholder Docstring."""
    serialized = add_gateway.to_b64()
    assert serialized == b'CiEBNRpxwi/v7CIxk2rSgmshfs452fd/xsSWOZJimcOGkpUSIQGcZZ1yPMHoEKcuePfer0c2qH8Q74/PyAEAtTMn5' \
                         b'+5JpCohATUaccIv7+wiMZNq0oJrIX7OOdn3f8bEljmSYpnDhpKVOICS9AFA6PsD'
    deserialized = AddGatewayV1.from_b64(serialized)
    assert deserialized.owner.b58 == add_gateway.owner.b58
    assert deserialized.payer.b58 == add_gateway.payer.b58
    assert deserialized.gateway.b58 == add_gateway.gateway.b58
    assert deserialized.fee == add_gateway.fee
    assert deserialized.staking_fee == add_gateway.staking_fee
    assert deserialized.owner_signature == add_gateway.owner_signature
    assert deserialized.payer_signature == add_gateway.payer_signature
    assert deserialized.gateway_signature == add_gateway.gateway_signature


def test_deserializes_from_base64_string_with_signatures(add_gateway):
    """Replace Placeholder Docstring."""
    deserialized = AddGatewayV1.from_b64(add_gateway.to_b64())
    assert deserialized.owner.b58 == add_gateway.owner.b58
    assert deserialized.payer.b58 == add_gateway.payer.b58
    assert deserialized.gateway.b58 == add_gateway.gateway.b58
    assert deserialized.fee == add_gateway.fee
    assert deserialized.staking_fee == add_gateway.staking_fee
    assert deserialized.owner_signature == add_gateway.owner_signature
    assert deserialized.payer_signature == add_gateway.payer_signature
    assert deserialized.gateway_signature == add_gateway.gateway_signature


def test_deserializes_empty_string():
    """Replace Placeholder Docstring."""
    deserialized = AddGatewayV1.from_b64(b'')
    assert deserialized.owner is None
    assert deserialized.payer is None
    assert deserialized.gateway is None
    assert deserialized.fee == 0
    assert deserialized.staking_fee == 0
    assert deserialized.owner_signature is None
    assert deserialized.payer_signature is None
    assert deserialized.gateway_signature is None


def test_signing_adds_owner_signature(add_gateway_no_payer, users):
    """Replace Placeholder Docstring."""
    signed_transaction = add_gateway_no_payer.sign(owner=users.bob.keypair)
    assert signed_transaction.owner_signature is not None
    assert len(signed_transaction.owner_signature) == 64


def test_signing_adds_gateway_signature(add_gateway_no_payer, users):
    """Replace Placeholder Docstring."""
    signed_transaction = add_gateway_no_payer.sign(gateway=users.alice.keypair)
    assert signed_transaction.gateway_signature is not None
    assert len(signed_transaction.gateway_signature) == 64


def test_signing_adds_the_payer_signature(add_gateway, users):
    """Replace Placeholder Docstring."""
    signed_transaction = add_gateway.sign(payer=users.alice.keypair)
    assert signed_transaction.payer_signature is not None
    assert len(signed_transaction.payer_signature) == 64
