# flake8: noqa
import binascii

from helium_py.crypto.mnemonic import Mnemonic
from helium_py.crypto.utils import random_bytes


def test_keypair(users):
    mnemonic = Mnemonic(users.bob.words)
    assert mnemonic.words == users.bob.words


def test_create_defaults_to_12_words():
    mnemonic = Mnemonic.create()
    assert len(mnemonic.words) == 12


def test_can_create_24_word_mnemonic():
    mnemonic = Mnemonic.create(24)
    assert len(mnemonic.words) == 24


def test_bad_length_mnemonic_raises():
    try:
        Mnemonic.create(55)
    except ValueError:
        pass
    else:
        raise Exception("Expected ValueError")


def test_create_mnemonic_from_entropy():
    entropy = random_bytes(16)
    mnemonic = Mnemonic.from_entropy(entropy)
    assert len(mnemonic.words) == 12


def test_create_24_word_mnemonic_from_entropy():
    entropy = random_bytes(32)
    mnemonic = Mnemonic.from_entropy(entropy)
    assert len(mnemonic.words) == 24


def test_generate_bip39_checksum_word():
    entropy = binascii.unhexlify(b'00000000000000000000000000000000')
    mnemonic = Mnemonic.from_entropy(entropy)
    assert mnemonic.words[11] == 'about'


def test_raise_error_if_entropy_under_16_bytes():
    entropy = random_bytes(12)
    try:
        Mnemonic.from_entropy(entropy)
    except Exception:
        pass
    else:
        raise Exception('Expected error on less than 16 bytes')


def test_throws_error_if_entropy_over_32_bytes():
    entropy = random_bytes(40)
    try:
        Mnemonic.from_entropy(entropy)
    except Exception:
        pass
    else:
        raise Exception('Expected error on greater than 32 bytes')


def test_throws_error_if_entropy_mod_four_non_zero():
    entropy = random_bytes(17)
    try:
        Mnemonic.from_entropy(entropy)
    except Exception:
        pass
    else:
        raise Exception('Expected error on entropy indivisible by four.')


def test_to_entropy_returns_expected():
    entropy = random_bytes(16)
    mnemonic = Mnemonic.from_entropy(entropy)
    assert mnemonic.to_entropy() == entropy


def test_to_entropy_returns_expected_32_bytes():
    entropy = random_bytes(32)
    mnemonic = Mnemonic.from_entropy(entropy)
    assert mnemonic.to_entropy() == entropy
