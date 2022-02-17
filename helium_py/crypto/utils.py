"""Replace Placeholder docstring."""
import binascii
from typing import List

from base58 import b58encode, b58decode
import nacl.bindings
import nacl.encoding
from nacl.hash import sha256


def random_bytes(n: int) -> bytes:
    """Replace Placeholder docstring."""
    return nacl.bindings.randombytes(n)


def bytes_to_binary(byte_array: bytes) -> List[str]:
    """Replace Placeholder docstring."""
    return [bin(byte_data) for byte_data in byte_array]


def binary_to_byte(bin_val: str) -> bytes:
    """Replace Placeholder docstring."""
    return int(bin_val, 2).to_bytes((len(bin_val) + 7) // 8, byteorder='big')


def derive_checksum_bits(entropy: bytes):
    """Replace Placeholder docstring."""
    ent = len(entropy) * 8
    cs = int(ent / 32)
    hash_val = sha256(entropy)
    return bytes_to_binary(hash_val)[0:cs]


def bs58_check_encode(version: int, binary: bytes) -> bytes:
    """Replace Placeholder docstring."""
    versioned_payload = bytes([version]) + binary
    checksum = sha256(binascii.unhexlify(sha256(versioned_payload)))
    checksum_bytes = bytes(binascii.unhexlify(checksum[:8]))
    result = versioned_payload + checksum_bytes
    return b58encode(result)


def bs58_to_bin(bs58_address: str) -> bytes:
    """Replace Placeholder docstring."""
    bs85_bin = b58decode(bs58_address)
    versioned_payload = bs85_bin[0:-4]
    payload = bs85_bin[1:-4]
    checksum = binascii.hexlify(bs85_bin[-4:])
    checksum_verify = sha256(binascii.unhexlify(sha256(versioned_payload)))[:8]
    if checksum_verify != checksum:
        raise Exception("Invalid checksum")
    return payload


def byte_to_net_type(byte_val: int) -> int:
    """Replace Placeholder docstring."""
    return byte_val & 240


def byte_to_key_type(byte_val: int) -> int:
    """Replace Placeholder docstring."""
    return byte_val & 15


def bs58_net_type(bs58_address: str) -> int:
    """Replace Placeholder docstring."""
    bs85_bin = bs58_to_bin(bs58_address)
    byte_val = bs85_bin[0]
    return byte_to_net_type(byte_val)


def bs58_key_type(bs58_address: str) -> int:
    """Replace Placeholder docstring."""
    bs85_bin = bs58_to_bin(bs58_address)
    byte_val = bs85_bin[0]
    return byte_to_key_type(byte_val)


def bs58_version(bs58_address: str) -> int:
    """Replace Placeholder docstring."""
    bs85_bin = b58decode(bs58_address)
    version = bs85_bin[0]
    return version


def bs58_public_key(bs58_address: str) -> bytes:
    """Replace Placeholder docstring."""
    bs85_bin = bs58_to_bin(bs58_address)
    public_key = bs85_bin[1:]
    return public_key
