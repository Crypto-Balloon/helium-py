"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.crypto.utils import EMPTY_SIGNATURE
from helium_py.transactions import AssertLocationV1

AssertLocationV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,

)


@pytest.fixture
def assert_location(users):
    """Replace Placeholder Docstring."""
    return AssertLocationV1(
        owner=users.bob.keypair.address,
        gateway=users.alice.keypair.address,
        payer=users.bob.keypair.address,
        location='8c383092841a7ff',
        nonce=1,
    )


@pytest.fixture
def assert_location_no_payer(users):
    """Replace Placeholder Docstring."""
    return AssertLocationV1(
        owner=users.bob.keypair.address,
        gateway=users.alice.keypair.address,
        payer=None,
        location='8c383092841a7ff',
        nonce=1,
    )


def test_create_assert_location_transaction(assert_location_no_payer, users):
    """Replace Placeholder Docstring."""
    assert_location_no_payer.calculate_fee()
    assert assert_location_no_payer.owner.b58 == users.bob.b58
    assert assert_location_no_payer.gateway.b58 == users.alice.b58
    assert assert_location_no_payer.location == '8c383092841a7ff'
    assert assert_location_no_payer.nonce == 1
    assert assert_location_no_payer.fee == 50000
    assert assert_location_no_payer.staking_fee == 1000000
    assert assert_location_no_payer.type == 'assert_location_v1'


def test_create_assert_location_transaction_with_payer(assert_location, users):
    """Replace Placeholder Docstring."""
    assert assert_location.owner.b58 == users.bob.b58
    assert assert_location.gateway.b58 == users.alice.b58
    assert assert_location.location == '8c383092841a7ff'
    assert assert_location.nonce == 1
    assert assert_location.fee == 70000
    assert assert_location.staking_fee == 1000000
    assert assert_location.type == 'assert_location_v1'


def test_serialize_returns_value(assert_location):
    """Replace Placeholder Docstring."""
    assert len(assert_location.serialize()) > 0


def test_serialize_to_base64(assert_location_no_payer):
    """Replace Placeholder Docstring."""
    assert AssertLocationV1.from_b64(assert_location_no_payer.to_b64()).fee == 50000
    assert proto.BlockchainTxn.FromString(assert_location_no_payer.serialize()).assert_location.fee == 50000


def test_deserializes_from_base64_string(assert_location):
    """Replace Placeholder Docstring."""
    # helium-js mutates the instance when adding empty signatures to calculate payment
    # and this is a reference b64 representation
    assert_location.owner_signature = EMPTY_SIGNATURE
    assert_location.gateway_signature = EMPTY_SIGNATURE
    assert_location.payer_signature = EMPTY_SIGNATURE
    serialized = assert_location.to_b64()
    assert serialized == b'EsoCCiEBnGWdcjzB6BCnLnj33q9HNqh/EO+Pz8gBALUzJ+fuSaQSIQE1GnHCL+/sIjGTatKCayF+zjnZ93' \
                         b'/GxJY5kmKZw4aSlRohATUaccIv7+wiMZNq0oJrIX7OOdn3f8bEljmSYpnDhpKVIkAAAAAAAAAAAAAAAAAA' \
                         b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKkAAAAAAAAAAAA' \
                         b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMkAAAAAA' \
                         b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOg' \
                         b'84YzM4MzA5Mjg0MWE3ZmZAAUjAhD1Q8KIE'
    deserialized = AssertLocationV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.owner.b58 == assert_location.owner.b58
    assert deserialized.payer.b58 == assert_location.payer.b58
    assert deserialized.gateway.b58 == assert_location.gateway.b58
    assert deserialized.location == '8c383092841a7ff'
    assert deserialized.nonce == 1
    assert deserialized.fee == assert_location.fee
    assert deserialized.staking_fee == assert_location.staking_fee
    assert deserialized.owner_signature == assert_location.owner_signature
    assert deserialized.payer_signature == assert_location.payer_signature
    assert deserialized.gateway_signature == assert_location.gateway_signature


def test_deserializes_from_base64_string_with_signatures(assert_location):
    """Replace Placeholder Docstring."""
    deserialized = AssertLocationV1.from_b64(assert_location.to_b64())
    deserialized.calculate_fee()
    assert deserialized.owner.b58 == assert_location.owner.b58
    assert deserialized.payer.b58 == assert_location.payer.b58
    assert deserialized.gateway.b58 == assert_location.gateway.b58
    assert deserialized.location == '8c383092841a7ff'
    assert deserialized.nonce == 1
    assert deserialized.fee == assert_location.fee
    assert deserialized.staking_fee == assert_location.staking_fee
    assert deserialized.owner_signature == assert_location.owner_signature
    assert deserialized.payer_signature == assert_location.payer_signature
    assert deserialized.gateway_signature == assert_location.gateway_signature


def test_signing_adds_owner_signature(assert_location_no_payer, users):
    """Replace Placeholder Docstring."""
    signed_transaction = assert_location_no_payer.sign(owner=users.bob.keypair)
    assert signed_transaction.owner_signature is not None
    assert len(signed_transaction.owner_signature) == 64


def test_signing_adds_gateway_signature(assert_location_no_payer, users):
    """Replace Placeholder Docstring."""
    signed_transaction = assert_location_no_payer.sign(gateway=users.alice.keypair)
    assert signed_transaction.gateway_signature is not None
    assert len(signed_transaction.gateway_signature) == 64


def test_signing_adds_the_payer_signature(assert_location, users):
    """Replace Placeholder Docstring."""
    signed_transaction = assert_location.sign(payer=users.alice.keypair)
    assert signed_transaction.payer_signature is not None
    assert len(signed_transaction.payer_signature) == 64
