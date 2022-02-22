"""Keypair class for cryptography."""
from dataclasses import dataclass
from typing import List, Optional

import nacl.bindings

from .address import Address
from .constants import SUPPORTED_NET_TYPES, KeyTypes, NetTypes
from .mnemonic import Mnemonic


@dataclass
class SodiumKeyPair:
    """Base SodiumKeypair dataclass."""

    pk: bytes
    sk: bytes
    key_type: Optional[int] = None


class Keypair:
    """Keypair class with mnemonic, entropy, and signing capabilities."""

    keypair: SodiumKeyPair
    public_key: bytes
    private_key: bytes
    key_type: int
    net_type: int

    def __init__(self, keypair: SodiumKeyPair, net_type: Optional[int] = None):
        """Initialize Keypair instance."""
        self.keypair = keypair
        self.public_key = keypair.pk
        self.private_key = keypair.sk
        self.key_type = keypair.key_type if keypair.key_type is not None else KeyTypes.ED25519_KEY_TYPE.value
        self.net_type = net_type if net_type is not None and net_type in SUPPORTED_NET_TYPES else NetTypes.MAINNET.value

    @property
    def address(self) -> Address:
        """Return Address instance for Keypair."""
        return Address(Address.DEFAULT_VERSION, self.net_type, KeyTypes.ED25519_KEY_TYPE.value, self.public_key)

    @staticmethod
    def make_random(net_type: int = None) -> 'Keypair':
        """Return randomly generated Keypair."""
        keypair = nacl.bindings.crypto_sign_keypair()
        return Keypair(SodiumKeyPair(pk=keypair[0], sk=keypair[1]), net_type)

    @classmethod
    def from_words(cls, words: List[str], net_type: Optional[int] = None) -> 'Keypair':
        """Return Keypair generated from list of words (mnemonic)."""
        mnemonic = Mnemonic(words)
        keypair = cls.from_mnemonic(mnemonic, net_type)
        return keypair

    @classmethod
    def from_mnemonic(cls, mnemonic: Mnemonic, net_type: Optional[int] = None) -> 'Keypair':
        """Return Keypair generated from a Mnemonic object."""
        entropy = mnemonic.to_entropy()
        seed = entropy + entropy if len(entropy) == 16 else entropy
        return cls.from_entropy(seed, net_type)

    @classmethod
    def from_entropy(cls, entropy: bytes, net_type: Optional[int] = None) -> 'Keypair':
        """Return Keypair generated from entropy."""
        if len(entropy) != 32:
            raise ValueError(f'Invalid entropy, must be 32 bytes. Found {len(entropy)}')
        keypair = nacl.bindings.crypto_sign_seed_keypair(entropy)
        return cls(SodiumKeyPair(pk=keypair[0], sk=keypair[1]), net_type)

    def sign(self, message: bytes) -> bytes:
        """Return signature for provided message utilizing private_key."""
        signature = nacl.bindings.crypto_sign(message, self.private_key)
        return signature[:signature.index(message)]
