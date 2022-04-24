"""Mnemonic class for cryptography."""
from math import floor
from typing import Any, List, Tuple

from . import utils
from .wordlists.english import wordlist

ALLOWABLE_MNEMONIC_LENGTHS = (12, 24)


class Mnemonic:
    """Mnemonic class with conversion to/from entropy."""

    words: List[str]

    def __init__(self, words: List[str]):
        """Initialize Mnemonic class with list of words."""
        self.words = words

    @staticmethod
    def create(length: int = 12) -> 'Mnemonic':
        """Return a randomly generated Mnemonic of the provided length."""
        if length not in ALLOWABLE_MNEMONIC_LENGTHS:
            raise ValueError(f'supported mnemonic lengths: 12, 24. received {length}')
        entropy_bytes = 16 if length == 12 else 32
        entropy = utils.random_bytes(entropy_bytes)
        return Mnemonic.from_entropy(entropy)

    @staticmethod
    def from_entropy(entropy: bytes) -> 'Mnemonic':
        """Return a Mnemonic generated from provided entropy."""
        if len(entropy) < 16:
            raise ValueError('invalid entropy, less than 16')
        if len(entropy) > 32:
            raise ValueError('invalid entropy, greater than 32')
        if len(entropy) % 4 != 0:
            raise ValueError('invalid entropy, not divisible by 4')

        entropyBits = utils.bytes_to_binary(entropy)
        checksumBits = utils.derive_checksum_bits(entropy)
        bits = entropyBits + checksumBits
        chunks = [bits[x:x + 11] for x in range(0, len(bits), 11)]
        words = [wordlist[int(binary, 2)] for binary in chunks]
        return Mnemonic(words)

    def _get_entropy_bits_and_checksum(self) -> Tuple[str, str]:
        bits = ''.join([
            f'{bin(wordlist.index(word))}'.lstrip('0b').zfill(11)
            for word in self.words
        ])

        # split the binary string into entropy and checksum
        dividerIndex = floor(len(bits) / 33) * 32
        return (bits[0:dividerIndex], bits[dividerIndex:])

    @staticmethod
    def _get_entropy_bytes(entropyBits) -> Tuple[List[Any], List[bytes]]:
        # calculate the checksum and compare
        chunks = [entropyBits[x:x + 8] for x in range(0, len(entropyBits), 8)]
        return (chunks, [int(entropy, 2).to_bytes((len(entropy) + 7) // 8, byteorder='big') for entropy in chunks])

    def to_entropy(self) -> bytes:
        """Return entropy bytes generated from provided Mnemonic."""
        entropyBits, checksumBits = self._get_entropy_bits_and_checksum()
        entropy_chunks, entropy_bytes = self._get_entropy_bytes(entropyBits)

        if len(entropy_bytes) < 16:
            raise ValueError('invalid entropy, less than 16')
        if len(entropy_bytes) > 32:
            raise ValueError('invalid entropy, greater than 32')
        if len(entropy_bytes) % 4 != 0:
            raise ValueError('invalid entropy, not divisible by 4')

        # calculate the checksum and compare
        entropy = bytes([int(byte_val, 2) for byte_val in entropy_chunks])
        new_checksum = utils.derive_checksum_bits(entropy)

        if checksumBits != '0000' and new_checksum != checksumBits:
            raise ValueError('invalid checksum')

        return entropy
