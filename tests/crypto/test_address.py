# flake8: noqa
from helium_py.crypto.address import Address
from helium_py.crypto.constants import KeyTypes, NetTypes

ED25519_KEY_TYPE = KeyTypes.ED25519_KEY_TYPE.value
MAINNET, TESTNET = NetTypes.MAINNET.value, NetTypes.TESTNET.value
ECC_COMPACT_ADDRESS = b'112qB3YaH5bZkCnKA5uRH7tBtGNv2Y5B4smv1jsmvGUzgKT71QpE'
BTC_ADDRESS = b'18wxa7qM8C8AXmGwJj13C7sGqn8hyFdcdR'
TESTNET_ADDRESS = b'1bijtibPhc16wx4oJbyK8vtkAgdoRoaUvJeo7rXBnBCufEYakfd'


def test_address_to_b58(users):
    address = Address(Address.DEFAULT_VERSION, MAINNET, ED25519_KEY_TYPE, users.bob.keypair.public_key)
    assert address.b58 == users.bob.b58


def test_address_to_b58_ed25519(users):
    address = Address.from_b58(users.bob.b58)
    assert address.b58 == users.bob.b58


def test_address_to_b58_ecc_compact():
    address = Address.from_b58(ECC_COMPACT_ADDRESS)
    assert address.b58 == ECC_COMPACT_ADDRESS


def test_bin_returns_binary_repr(users):
    address = Address(Address.DEFAULT_VERSION, MAINNET, ED25519_KEY_TYPE, users.bob.keypair.public_key)
    assert address.bin[0] == 1


def test_build_address_from_binary_repr(users):
    address = Address.from_bin(Address(
        Address.DEFAULT_VERSION, MAINNET, ED25519_KEY_TYPE, users.bob.keypair.public_key,
    ).bin)
    assert address.b58 == users.bob.b58


def test_from_bin_raises_when_null(users):
    try:
        address = Address.from_bin(None)
    except ValueError:
        pass
    else:
        raise Exception("Expected ValueError")


def test_from_bin_raises_when_empty(users):
    try:
        address = Address.from_bin(b'')
    except ValueError:
        pass
    else:
        raise Exception("Expected ValueError")


def test_build_address_from_b58_str(users):
    address = Address.from_b58(users.bob.b58)
    assert address.b58 == users.bob.b58


def test_unsupported_key_type_via_b58():
    try:
        Address.from_b58(BTC_ADDRESS)
    except Exception:
        pass
    else:
        raise Exception('Expected exception on bad key type')


def test_unsupported_key_type_via_init():
    try:
        Address(Address.DEFAULT_VERSION, MAINNET, 57, b'some random public key')
    except Exception:
        pass
    else:
        raise Exception('Expected exception on bad key type')


def test_unsupported_versions_raises(users):
    try:
        Address(1, MAINNET, ED25519_KEY_TYPE, users.bob.keypair.public_key)
    except Exception:
        pass
    else:
        raise Exception('Expected exception on bad version')


def test_testnet_address_decodes_from_b58():
    address = Address.from_b58(TESTNET_ADDRESS)
    assert address.net_type == TESTNET
