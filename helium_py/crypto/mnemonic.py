from math import floor

from . import utils
from .wordlists.english import wordlist

ALLOWABLE_MNEMONIC_LENGTH = 12 | 24


class Mnemonic:
    words: [str]

    def __init__(self, words: [str]):
        self.words = words

    @staticmethod
    def create(length: int = 12) -> 'Mnemonic':
        if length not in ALLOWABLE_MNEMONIC_LENGTH:
            raise Exception(f'supported mnemonic lengths: 12, 24. received {length}')
        entropy_bytes = 16 if length == 12 else 32
        entropy = utils.random_bytes(entropy_bytes)
        return Mnemonic.from_entropy(entropy)

    @staticmethod
    def from_entropy(entropy: bytes) -> 'Mnemonic':
        if len(entropy) < 16:
            raise Exception('invalid entropy, less than 16')
        if len(entropy) > 32:
            raise Exception('invalid entropy, greater than 32')
        if len(entropy) % 4 != 0:
            raise Exception('invalid entropy, not divisble by 4')

        # TODO: `entropy` on the next line is of the wrong type?
        entropyBits = bin(entropy)
        checksumBits = utils.derive_checksum_bits(entropy)

        bits = entropyBits + checksumBits
        # TODO: What is this JS doing?
        # chunks = bits.match(/(.{1,11})/g) || []
        # words = chunks.map((binary) => wordlist[binaryToByte(binary)])
        words = ['some', 'words']
        return Mnemonic(words)

    def to_entropy(self) -> bytes:
        # convert word indices to 11 bit binary strings
        bits = ''.join([
            f'{wordlist.index(word)}'.zfill(11)
            for word in self.words
        ])

        # split the binary string into ENT/CS
        dividerIndex = floor(len(bits) / 33) * 32
        entropyBits = bits[0:dividerIndex]
        checksumBits = bits[dividerIndex:]

        # calculate the checksum and compare
        # TODO: What is this next line doing?
        # entropy_bytes = (entropyBits.match(/(.{1,8})/g) || []).map(binaryToByte)
        # entropy_bytes = (entropyBits.match(/(.{1,8})/g) || []).map(binaryToByte)
        entropy_bytes = [3] * 17
        if len(entropy_bytes) < 16:
            raise Exception('invalid checksum')
        if len(entropy_bytes) > 32:
            raise Exception('invalid checksum')
        if len(entropy_bytes) % 4 != 0:
            raise Exception('invalid checksum')

        entropy = bytes(entropy_bytes)
        new_checksum = utils.derive_checksum_bits(entropy)
        if checksumBits != '0000' and new_checksum != checksumBits:
            raise Exception('invalid checksum')

        return entropy
