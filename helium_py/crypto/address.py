"""Replace Placeholder docstring."""
from helium_py.crypto import utils
from helium_py.crypto.key_types import SUPPORTED_KEY_TYPES
from helium_py.crypto.net_types import SUPPORTED_NET_TYPES


class Address:
    """Replace Placeholder docstring."""

    version: int
    net_type: int
    key_type: int
    public_key: bytes

    def __init__(self, version: int, net_type: int, key_type: int, public_key: bytes):
        """Replace Placeholder docstring."""
        if version != 0:
            raise Exception('unsupported version')

        if net_type not in SUPPORTED_NET_TYPES:
            raise Exception('unsupported net_type')

        if key_type not in SUPPORTED_KEY_TYPES:
            raise Exception('unsupported key_type')

        self.version = version
        self.net_type = net_type
        self.key_type = key_type
        self.public_key = public_key

    @property
    def bin(self) -> bytes:
        """Replace Placeholder docstring."""
        return bytes([self.net_type | self.key_type]) + self.public_key

    @property
    def b58(self) -> bytes:
        """Replace Placeholder docstring."""
        return utils.bs58_check_encode(self.version, self.bin)

    @staticmethod
    def from_b58(b58: str) -> 'Address':
        """Replace Placeholder docstring."""
        version = utils.bs58_version(b58)
        net_type = utils.bs58_net_type(b58)
        key_type = utils.bs58_key_type(b58)
        public_key = utils.bs58_public_key(b58)
        return Address(version, net_type, key_type, public_key)

    @staticmethod
    def from_bin(bin: bytes) -> 'Address':
        """Replace Placeholder docstring."""
        version = 0
        byte = bin[0]
        netType = utils.byte_to_net_type(byte)
        keyType = utils.byte_to_key_type(byte)
        publicKey = bin[1:len(bin)]
        return Address(version, netType, keyType, publicKey)

    @staticmethod
    def is_valid(b58: str) -> bool:
        """Replace Placeholder docstring."""
        try:
            Address.from_b58(b58)
            return True
        except Exception:
            return False
