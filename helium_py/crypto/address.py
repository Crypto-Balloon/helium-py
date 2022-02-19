"""Address class for cryptography."""
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
    def from_bin(bin_val: bytes) -> 'Address':
        """Return Address instance created from provided binary."""
        byte = bin_val[0]
        netType = utils.byte_to_net_type(byte)
        keyType = utils.byte_to_key_type(byte)
        publicKey = bin_val[1:len(bin_val)]
        return Address(Address.DEFAULT_VERSION, netType, keyType, publicKey)

    @staticmethod
    def is_valid(b58: bytes) -> bool:
        """Return True if b58 is valid."""
        try:
            Address.from_b58(b58)
            return True
        except Exception:
            return False
