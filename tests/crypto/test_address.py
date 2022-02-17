from helium_py.crypto.address import Address
from helium_py.crypto.key_types import ED25519_KEY_TYPE
from helium_py.crypto.net_types import MAINNET
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
