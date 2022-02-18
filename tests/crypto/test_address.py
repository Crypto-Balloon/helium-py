# flake8: noqa
from helium_py.crypto.address import Address
from helium_py.crypto.key_types import ED25519_KEY_TYPE
from helium_py.crypto.net_types import MAINNET, TESTNET
from tests.crypto.fixtures import bob, bobB58

ECC_COMPACT_ADDRESS = b'112qB3YaH5bZkCnKA5uRH7tBtGNv2Y5B4smv1jsmvGUzgKT71QpE'
BTC_ADDRESS = b'18wxa7qM8C8AXmGwJj13C7sGqn8hyFdcdR'
TESTNET_ADDRESS = b'1bijtibPhc16wx4oJbyK8vtkAgdoRoaUvJeo7rXBnBCufEYakfd'


def test_address_to_b58():
    address = Address(0, MAINNET, ED25519_KEY_TYPE, bob.public_key)
    assert address.b58 == bobB58


def test_address_to_b58_ed25519():
    address = Address.from_b58(bobB58)
    assert address.b58 == bobB58


def test_address_to_b58_ecc_compact():
    address = Address.from_b58(ECC_COMPACT_ADDRESS)
    assert address.b58 == ECC_COMPACT_ADDRESS


def test_bin_returns_binary_repr():
    address = Address(0, MAINNET, ED25519_KEY_TYPE, bob.public_key)
    assert address.bin[0] == 1


def test_build_address_from_binary_repr():
    address = Address.from_bin(Address(0, MAINNET, ED25519_KEY_TYPE, bob.public_key).bin)
    assert address.b58 == bobB58


def test_build_address_from_b58_str():
    address = Address.from_b58(bobB58)
    assert address.b58 == bobB58


def test_unsupported_key_type_via_b58():
    try:
        Address.from_b58(BTC_ADDRESS)
    except Exception:
        pass
    else:
        raise Exception('Expected exception on bad key type')


def test_unsupported_key_type_via_init():
    try:
        Address(0, MAINNET, 57, b'some random public key')
    except Exception:
        pass
    else:
        raise Exception('Expected exception on bad key type')


def test_is_valid_happy_path():
    assert Address.is_valid(bobB58) is True
    assert Address.is_valid(ECC_COMPACT_ADDRESS) is True


def test_is_valid_false_on_invalid():
    assert Address.is_valid(b'some invalid address') is False


def test_is_valid_false_on_decode_check_failure():
    bad_bob_b58 = b'13M8dUbxymE3xtiAXszRkGMmezMhBS8Li7wEsMojLdb4Sdxc4wb'
    assert Address.is_valid(bad_bob_b58) is False


def test_is_valid_false_on_invalid_key_type():
    assert Address.is_valid(BTC_ADDRESS) is False


def test_unsupported_versions_raises():
    try:
        Address(1, MAINNET, ED25519_KEY_TYPE, bob.public_key)
    except Exception:
        pass
    else:
        raise Exception('Expected exception on bad version')


def test_testnet_address_decodes_from_b58():
    address = Address.from_b58(TESTNET_ADDRESS)
    assert address.net_type == TESTNET
