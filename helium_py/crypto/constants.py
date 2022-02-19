"""Constants for Cryptography."""
from enum import Enum

ALLOWED_VERSIONS = (0,)


class KeyTypes(Enum):
    """Enum for Key Types."""

    ECC_COMPACT_KEY_TYPE = 0
    ED25519_KEY_TYPE = 1


class NetTypes(Enum):
    """Enum for Network Types."""

    MAINNET = 0
    TESTNET = 16


SUPPORTED_KEY_TYPES = (
    KeyTypes.ECC_COMPACT_KEY_TYPE.value,
    KeyTypes.ED25519_KEY_TYPE.value,
)

SUPPORTED_NET_TYPES = (
    NetTypes.MAINNET.value,
    NetTypes.TESTNET.value,
)
