"""Replace Placeholder Docstring."""
import pytest

from helium_py import proto
from helium_py.crypto.utils import EMPTY_SIGNATURE
from helium_py.transactions import TokenBurnV1

TokenBurnV1.config(
    transaction_fee_multiplier=5000,
    dc_payload_size=24,
    staking_fee_txn_add_gateway_v1=40 * 100000,
    staking_fee_txn_assert_location_v1=10 * 100000,
)


@pytest.fixture
def token_burn(users):
    """Replace Placeholder Docstring."""
    return TokenBurnV1(
        payer=users.bob.keypair.address,
        payee=users.alice.keypair.address,
        amount=10,
        nonce=1,
        memo=b'12345678',
    )


def test_create_token_burn_transaction(token_burn, users):
    """Replace Placeholder Docstring."""
    assert token_burn.payer.b58 == users.bob.b58
    assert token_burn.payee.b58 == users.alice.b58
    assert token_burn.amount == 10
    assert token_burn.nonce == 1
    assert token_burn.fee == 35000
    assert token_burn.memo == b'12345678'
    assert token_burn.type == 'token_burn_v1'


def test_serialize_returns_value(token_burn):
    """Replace Placeholder Docstring."""
    assert len(token_burn.serialize()) > 0


def test_more_than_eight_byte_memo_fails(token_burn):
    """Replace Placeholder Docstring."""
    token_burn.memo = b'123456789'
    try:
        token_burn.serialize()
    except ValueError:
        pass
    else:
        raise Exception('Expected test failure on 9 byte memo')


def test_serialize_to_base64(token_burn):
    """Replace Placeholder Docstring."""
    assert TokenBurnV1.from_b64(token_burn.to_b64()).amount == 10
    assert proto.BlockchainTxn.FromString(token_burn.serialize()).token_burn.amount == 10


def test_deserializes_from_base64_string(token_burn):
    """Replace Placeholder Docstring."""
    token_burn.signature = EMPTY_SIGNATURE
    serialized = token_burn.to_b64()
    assert serialized == b'igGaAQohATUaccIv7+wiMZNq0oJrIX7OOdn3f8bEljmSYpnDhpKVEiEBnGWdcjzB6BCnLnj33q9HNqh/EO+Pz' \
                         b'8gBALUzJ+fuSaQYCiABKkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
                         b'AAAAAAAAAAAAAAAAAAAAAAMLiRAjix5Myh08bNmzg='

    deserialized = TokenBurnV1.from_b64(serialized)
    deserialized.calculate_fee()
    assert deserialized.payer.b58 == token_burn.payer.b58
    assert deserialized.payee.b58 == token_burn.payee.b58
    assert deserialized.amount == 10
    assert deserialized.nonce == 1
    assert deserialized.memo == token_burn.memo
    assert deserialized.fee == token_burn.fee
    assert deserialized.signature == token_burn.signature


def test_signing_adds_signature(token_burn, users):
    """Replace Placeholder Docstring."""
    signed_transaction = token_burn.sign(payer=users.bob.keypair)
    assert signed_transaction.signature is not None
    assert len(signed_transaction.signature) == 64
