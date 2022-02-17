from dataclasses import dataclass
from typing import Optional

import nacl.bindings

from .address import Address
from .key_types import ED25519_KEY_TYPE
from .mnemonic import Mnemonic
from .net_types import MAINNET, SUPPORTED_NET_TYPES


@dataclass
class SodiumKeyPair:
    pk: bytes
    sk: bytes
    key_type: Optional[int] = None


class Keypair:
    keypair: SodiumKeyPair
    public_key: bytes
    private_key: bytes
    key_type: int
    net_type: int

    def __init__(self, keypair: SodiumKeyPair, net_type: int = None):
        self.keypair = keypair
        self.public_key = keypair.pk
        self.private_key = keypair.sk
        self.key_type = keypair.key_type if keypair.key_type is not None else ED25519_KEY_TYPE
        self.net_type = net_type if net_type in SUPPORTED_NET_TYPES else MAINNET

    def address(self) -> Address:
        return Address(0, self.net_type, ED25519_KEY_TYPE, self.public_key)

    @staticmethod
    def make_random(net_type: int = None) -> 'Keypair':
        keypair = nacl.bindings.crypto_sign_keypair()
        return Keypair(SodiumKeyPair(pk=keypair[0], sk=keypair[1]), net_type)

    @classmethod
    def from_words(cls, words: [str], net_type: int = None) -> 'Keypair':
        mnenomic = Mnemonic(words)
        keypair = cls.from_mnemonic(mnenomic, net_type)
        return keypair

    @classmethod
    def from_mnemonic(cls, mnenomic: Mnemonic, net_type: int = None) -> 'Keypair':
        entropy = mnenomic.to_entropy()
        seed = entropy + entropy if len(entropy) == 16 else entropy
        return cls.from_entropy(seed, net_type)

    @classmethod
    def from_entropy(cls, entropy: bytes, net_type: int) -> 'Keypair':
        entropyBuffer = bytes(entropy)
        if len(entropyBuffer) != 32:
            raise Exception('Invalid entropy, must be 32 bytes')
        keypair = nacl.bindings.crypto_sign_seed_keypair(entropy)
        return cls(SodiumKeyPair(pk=keypair[0], sk=keypair[1]), net_type)

    def sign(self, message: str | bytes) -> bytes:
        signature = nacl.bindings.crypto_sign(message, self.private_key)
        return signature
