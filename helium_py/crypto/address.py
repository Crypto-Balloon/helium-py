"""Address class for cryptography."""
from typing import Optional

from helium_py.crypto import utils
from helium_py.crypto.constants import (
    ALLOWED_VERSIONS,
    SUPPORTED_KEY_TYPES,
    SUPPORTED_NET_TYPES,
)


class Address:
    """Address class for cryptography."""

    version: int
    net_type: int
    key_type: int
    public_key: bytes
    DEFAULT_VERSION: int = 0

    def __init__(self, version: int, net_type: int, key_type: int, public_key: bytes):
        """Instantiate an address class."""
        if version not in ALLOWED_VERSIONS:
            raise ValueError('unsupported version')

        if net_type not in SUPPORTED_NET_TYPES:
            raise ValueError('unsupported net_type')

        if key_type not in SUPPORTED_KEY_TYPES:
            raise ValueError('unsupported key_type')

        self.version = version
        self.net_type = net_type
        self.key_type = key_type
        self.public_key = public_key

    @property
    def bin(self) -> bytes:
        """Return binary representation of address."""
        return bytes([self.net_type | self.key_type]) + self.public_key

    @property
    def b58(self) -> bytes:
        """Return b58 representation of address."""
        return utils.bs58_check_encode(self.version, self.bin)

    @staticmethod
    def from_b58(b58: bytes) -> 'Address':
        """Return Address instance created from provided b58."""
        version = utils.bs58_version(b58)
        net_type = utils.bs58_net_type(b58)
        key_type = utils.bs58_key_type(b58)
        public_key = utils.bs58_public_key(b58)
        return Address(version, net_type, key_type, public_key)

    @staticmethod
    def from_bin(value: Optional[bytes] = None) -> 'Address':
        """Return Address instance created from provided binary."""
        if value is None or len(value) == 0:
            raise ValueError(f'Cannot create address instance.'
                             f'Binary value is {"null" if value is None else "blank"}')

        netType, keyType = utils.byte_to_net_type_and_key_type(value[0])
        return Address(Address.DEFAULT_VERSION, netType, keyType, public_key=value[1:])
