"""Replace Placeholder Docstring."""

import pytest

from helium_py.transactions.add_gateway_v1 import AddGatewayV1
from helium_py.transactions.transaction import ChainVars
from helium_py.transactions.utils import EMPTY_SIGNATURE

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


def test_serialize_to_base64(add_gateway):
    """Replace Placeholder Docstring."""
    assert AddGatewayV1.from_string(add_gateway.serialize()).fee == 45000
    # TODO: There's some bug in FromString betterproto
    # assert proto.BlockchainTxnAddGatewayV1.FromString(add_gateway.to_bytes_string()).fee == 45000


def test_deserializes_from_base64_string(add_gateway):
    """Replace Placeholder Docstring."""
    deserialized = AddGatewayV1.from_string(add_gateway.to_bytes_string())
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
    deserialized = AddGatewayV1.from_string(add_gateway.to_bytes_string())
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
    deserialized = AddGatewayV1.from_string(b'')
    assert deserialized.owner.b58 is None
    assert deserialized.payer.b58 is None
    assert deserialized.gateway.b58 is None
    assert deserialized.fee == 30000
    assert deserialized.staking_fee == 4000000
    assert deserialized.owner_signature == EMPTY_SIGNATURE
    assert deserialized.payer_signature == EMPTY_SIGNATURE
    assert deserialized.gateway_signature == EMPTY_SIGNATURE

#
# describe('sign', () => {
#   it('adds the owner signature', async () => {
#     const { bob, alice } = await usersFixture()
#     const payment = new AddGatewayV1({
#       owner: bob.address,
#       gateway: alice.address,
#     })
#
#     const signedTxn = await payment.sign({ owner: bob })
#
#     if (!signedTxn.ownerSignature) throw new Error('null')
#     expect(Buffer.byteLength(Buffer.from(signedTxn.ownerSignature))).toBe(64)
#   })
#
#   it('adds the gateway signature', async () => {
#     const { bob, alice } = await usersFixture()
#     const payment = new AddGatewayV1({
#       owner: bob.address,
#       gateway: alice.address,
#     })
#
#     const signedTxn = await payment.sign({ gateway: alice })
#
#     if (!signedTxn.gatewaySignature) throw new Error('null')
#
#     expect(Buffer.byteLength(Buffer.from(signedTxn.gatewaySignature))).toBe(64)
#
#     const paymentString = signedTxn.toString()
#     const deserialized = AddGatewayV1.fromString(paymentString)
#     expect(deserialized.owner?.b58).toBe(signedTxn.owner?.b58)
#     expect(deserialized.payer?.b58).toBe(signedTxn.payer?.b58)
#     expect(deserialized.gateway?.b58).toBe(signedTxn.gateway?.b58)
#     expect(deserialized.fee).toBe(signedTxn.fee)
#     expect(deserialized.stakingFee).toBe(signedTxn.stakingFee)
#     expect(deserialized.ownerSignature).toEqual(signedTxn.ownerSignature)
#     expect(deserialized.payerSignature).toEqual(signedTxn.payerSignature)
#     expect(deserialized.gatewaySignature).toEqual(signedTxn.gatewaySignature)
#   })
#
#   it('adds the payer signature', async () => {
#     const { bob, alice } = await usersFixture()
#     const payment = new AddGatewayV1({
#       owner: bob.address,
#       gateway: alice.address,
#       payer: bob.address,
#     })
#
#     const signedTxn = await payment.sign({ payer: alice })
#
#     if (!signedTxn.payerSignature) throw new Error('null')
#
#     expect(Buffer.byteLength(Buffer.from(signedTxn.payerSignature))).toBe(64)
#
#     const paymentString = signedTxn.toString()
#     const deserialized = AddGatewayV1.fromString(paymentString)
#     expect(deserialized.owner?.b58).toBe(signedTxn.owner?.b58)
#     expect(deserialized.payer?.b58).toBe(signedTxn.payer?.b58)
#     expect(deserialized.gateway?.b58).toBe(signedTxn.gateway?.b58)
#     expect(deserialized.fee).toBe(signedTxn.fee)
#     expect(deserialized.stakingFee).toBe(signedTxn.stakingFee)
#     expect(deserialized.ownerSignature).toEqual(signedTxn.ownerSignature)
#     expect(deserialized.payerSignature).toEqual(signedTxn.payerSignature)
#     expect(deserialized.gatewaySignature).toEqual(signedTxn.gatewaySignature)
#   })
# })
