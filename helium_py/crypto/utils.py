"""Utility methods for cryptography."""
import binascii
from typing import Tuple

import nacl.bindings
import nacl.encoding
from base58 import b58decode, b58encode
from nacl.hash import sha256

EMPTY_SIGNATURE = bytes([0]*64)


def random_bytes(n: int) -> bytes:
    """Return random bytes of size n."""
    return nacl.bindings.randombytes(n)


def bytes_to_binary(byte_array: bytes) -> str:
    """Return binary from provided bytes."""
    return ''.join([format(byte_data, '08b') for byte_data in byte_array])


def derive_checksum_bits(entropy: bytes):
    """Return checksum bits from entropy bytes."""
    ent = len(entropy) * 8
    cs = int(ent / 32)
    hash_val = sha256(entropy)
    return bytes_to_binary(binascii.unhexlify(hash_val))[:cs]


def bs58_check_encode(version: int, binary: bytes) -> bytes:
    """Return endoed Base58 address from version and bytes."""
    versioned_payload = bytes([version]) + binary
    checksum = sha256(binascii.unhexlify(sha256(versioned_payload)))
    checksum_bytes = bytes(binascii.unhexlify(checksum[:8]))
    result = versioned_payload + checksum_bytes
    return b58encode(result)


def bs58_to_bin(bs58_address: bytes) -> bytes:
    """Return decoded bytes from Base58 address bytes."""
    bs58_bin = b58decode(bs58_address)
    versioned_payload = bs58_bin[0:-4]
    payload = bs58_bin[1:-4]
    checksum = binascii.hexlify(bs58_bin[-4:])
    checksum_verify = sha256(binascii.unhexlify(sha256(versioned_payload)))[:8]
    if checksum_verify != checksum:
        raise ValueError('Invalid checksum')
    return payload


def byte_to_net_type_and_key_type(byte_val: int) -> Tuple[int, int]:
    """Return network type and key type in a tuple from byte value."""
    return byte_to_net_type(byte_val), byte_to_key_type(byte_val)


def byte_to_net_type(byte_val: int) -> int:
    """Return network type from byte value."""
    return byte_val & 240


def byte_to_key_type(byte_val: int) -> int:
    """Return key type from byte value."""
    return byte_val & 15


def bs58_net_type(bs58_address: bytes) -> int:
    """Return network type from bs58 address."""
    bs58_bin = bs58_to_bin(bs58_address)
    byte_val = bs58_bin[0]
    return byte_to_net_type(byte_val)


def bs58_key_type(bs58_address: bytes) -> int:
    """Return key type from bs58 address."""
    bs58_bin = bs58_to_bin(bs58_address)
    byte_val = bs58_bin[0]
    return byte_to_key_type(byte_val)


def bs58_version(bs58_address: bytes) -> int:
    """Return version from bs58 address."""
    bs58_bin = b58decode(bs58_address)
    version = bs58_bin[0]
    return version


def bs58_public_key(bs58_address: bytes) -> bytes:
    """Return public key from bs58 address."""
    bs58_bin = bs58_to_bin(bs58_address)
    public_key = bs58_bin[1:]
    return public_key
