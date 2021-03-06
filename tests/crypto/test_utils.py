# flake8: noqa
import binascii

import base58

from helium_py.crypto import utils
from helium_py.crypto.address import Address
from helium_py.crypto.constants import NetTypes

MAINNET = NetTypes.MAINNET.value


def test_derive_checksum_bits():
    entropy = b'00000000000000000000000000000000'
    entropyBuffer = binascii.unhexlify(entropy)
    derivedChecksumBits = utils.derive_checksum_bits(entropyBuffer)
    assert derivedChecksumBits == '0011'


def test_encode_publickey_to_bs58_address(users):
    address = Address(Address.DEFAULT_VERSION, MAINNET, 1, users.bob.keypair.public_key)
    versioned_payload = bytes([0]) + address.bin
    checksum = utils.sha256(binascii.unhexlify(utils.sha256(versioned_payload)))
    checksum_bytes = bytes(binascii.unhexlify(checksum[:8]))
    result = versioned_payload + checksum_bytes
    encoded = base58.b58encode(result)
    assert encoded == users.bob.b58 == utils.bs58_check_encode(0, address.bin)


def test_bs58_to_bin(users):
    address_b58 = Address(Address.DEFAULT_VERSION, MAINNET, 1, users.bob.keypair.public_key).b58
    binary = base58.b58decode(address_b58)
    versioned_payload = binary[0:-4]
    payload = binary[1:-4]
    checksum = binascii.hexlify(binary[-4:])
    checksum_verify = utils.sha256(binascii.unhexlify(utils.sha256(versioned_payload)))[:8]
    assert checksum_verify == checksum
    assert payload == utils.bs58_to_bin(address_b58)


def test_bs58_to_bin_invalid_checksum(users):
    address_b58 = Address(Address.DEFAULT_VERSION, MAINNET, 1, users.bob.keypair.public_key).b58
    bad_address_b58 = address_b58[:-1] + b'z'
    try:
        utils.bs58_to_bin(bad_address_b58)
    except ValueError:
        pass
    else:
        raise Exception("Expected bs58_to_bin to raise ValueError on Invalid Checksum")
