"""Replace Placeholder docstring."""
from math import floor
from typing import List

from . import utils
from .wordlists.english import wordlist

ALLOWABLE_MNEMONIC_LENGTHS = (12, 24)


class Mnemonic:
    """Replace Placeholder docstring."""

    words: List[str]

    def __init__(self, words: List[str]):
        """Replace Placeholder docstring."""
        self.words = words

    @staticmethod
    def create(length: int = 12) -> 'Mnemonic':
        """Replace Placeholder docstring."""
        if length not in ALLOWABLE_MNEMONIC_LENGTHS:
            raise Exception(f'supported mnemonic lengths: 12, 24. received {length}')
        entropy_bytes = 16 if length == 12 else 32
        entropy = utils.random_bytes(entropy_bytes)
        return Mnemonic.from_entropy(entropy)

    @staticmethod
    def from_entropy(entropy: bytes) -> 'Mnemonic':
        """Replace Placeholder docstring."""
        if len(entropy) < 16:
            raise Exception('invalid entropy, less than 16')
        if len(entropy) > 32:
            raise Exception('invalid entropy, greater than 32')
        if len(entropy) % 4 != 0:
            raise Exception('invalid entropy, not divisble by 4')

        # TODO: `entropy` on the next line is of the wrong type?
        entropyBits = utils.bytes_to_binary(entropy)
        checksumBits = utils.derive_checksum_bits(entropy)
        bits = entropyBits + checksumBits
        chunks = [bits[x:x + 11] for x in range(0, len(bits), 11)]
        words = [wordlist[int(binary, 2)] for binary in chunks]
        return Mnemonic(words)

    def to_entropy(self) -> bytes:
        """Replace Placeholder docstring."""
        # convert word indices to 11 bit binary strings
        bits = ''.join([
            f'{bin(wordlist.index(word))}'.lstrip('0b').zfill(11)
            for word in self.words
        ])

        # split the binary string into ENT/CS
        dividerIndex = floor(len(bits) / 33) * 32
        entropyBits = bits[0:dividerIndex]
        checksumBits = bits[dividerIndex:]

        # calculate the checksum and compare
        chunks = [entropyBits[x:x + 8] for x in range(0, len(entropyBits), 8)]
        entropy_bytes = [int(entropy, 2).to_bytes((len(entropy) + 7) // 8, byteorder='big') for entropy in chunks]

        if len(entropy_bytes) < 16:
            raise Exception('invalid checksum')
        if len(entropy_bytes) > 32:
            raise Exception('invalid checksum')
        if len(entropy_bytes) % 4 != 0:
            raise Exception('invalid checksum')

        entropy = bytes([int(byte_val, 2) for byte_val in chunks])
        new_checksum = utils.derive_checksum_bits(entropy)
        if checksumBits != '0000' and new_checksum != checksumBits:
            raise Exception('invalid checksum')

        return entropy
