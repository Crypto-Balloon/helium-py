# flake8: noqa
import base64
import binascii

from helium_py.crypto import utils
from helium_py.crypto.constants import KeyTypes, NetTypes
from helium_py.crypto.keypair import Keypair
from helium_py.crypto.mnemonic import Mnemonic

ED25519_KEY_TYPE = KeyTypes.ED25519_KEY_TYPE.value
TESTNET = NetTypes.TESTNET.value


def test_keypair_returns_public_key():
    keypair = Keypair.make_random()
    assert len(keypair.public_key) == 32


def test_keypair_returns_private_key():
    keypair = Keypair.make_random()
    assert len(keypair.private_key) == 64


def test_keypair_returns_key_type():
    keypair = Keypair.make_random()
    assert keypair.key_type == ED25519_KEY_TYPE


def test_returns_address_from_public_key(users):
    keypair = Keypair.from_words(users.bob.words)
    assert keypair.address.b58 == users.bob.b58


def test_same_keypair_with_bip39_and_legacy_checksum_words(users):
    words_keypair = Keypair.from_words(users.bob.words)
    bip39_keypair = Keypair.from_words(users.bob.bip_39_words)
    assert words_keypair.private_key == bip39_keypair.private_key


def test_return_keypair_seeded_by_provided_entropy():
    entropy = b'1f5b981baca0420259ab53996df7a8ce0e3549c6616854e7dff796304bafb6bf'
    keypair = Keypair.from_entropy(binascii.unhexlify(entropy))
    assert keypair.key_type == ED25519_KEY_TYPE


def test_raise_if_entropy_incorrect_byte_size():
    entropy = b'e8e0b9e9badae50f230e9ec12f213fd9'
    try:
        Keypair.from_entropy(binascii.unhexlify(entropy))
    except Exception:
        pass
    else:
        raise Exception('Expected failure on bad entropy bytes')

def test_signing_message_with_private_key(users):
    mnemonic = Mnemonic(users.bob.words)
    keypair = Keypair.from_mnemonic(mnemonic)
    message = b'the shark feeds at midnight'
    signature = keypair.sign(message)
    expectedSignature = b'NKGpxhYtcXdyFDDRbbY5KjY7r38R8q1ViBft85t4QcH/WrB2Mg9bg2RocfYy16YGcxjLLNSwTLOmfxsjwPWdBQ=='
    assert base64.b64encode(signature) == expectedSignature


def test_make_testnet_keypair_from_entropy():
    entropy = binascii.unhexlify(b'1f5b981baca0420259ab53996df7a8ce0e3549c6616854e7dff796304bafb6bf')
    keypair = Keypair.from_entropy(entropy, TESTNET)
    assert keypair.net_type == TESTNET
    assert utils.bs58_net_type(keypair.address.b58) == TESTNET
