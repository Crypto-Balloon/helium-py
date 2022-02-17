from helium_py.crypto.address import Address, MAINNET, ECC_COMPACT_KEY_TYPE, ED25519_KEY_TYPE

ECC_COMPACT_ADDRESS = '112qB3YaH5bZkCnKA5uRH7tBtGNv2Y5B4smv1jsmvGUzgKT71QpE'
BTC_ADDRESS = '18wxa7qM8C8AXmGwJj13C7sGqn8hyFdcdR'
TESTNET_ADDRESS = '1bijtibPhc16wx4oJbyK8vtkAgdoRoaUvJeo7rXBnBCufEYakfd'


def test_address():
    address = Address(0, MAINNET, ED25519_KEY_TYPE, bob.public_key)
    expect(address.b58).toBe(bobB58)