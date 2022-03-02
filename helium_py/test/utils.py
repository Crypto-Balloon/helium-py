"""helium-py test utils."""

from dataclasses import dataclass
from typing import Optional

from helium_py.crypto.keypair import Keypair

BOB_WORDS = [
  'indicate',
  'flee',
  'grace',
  'spirit',
  'trim',
  'safe',
  'access',
  'oppose',
  'void',
  'police',
  'calm',
  'energy',
]
"""Words for test user Bob.

    These words generate a real Helium account and should be considered COMPROMISED.
    Don't send any money to them that you don't want to lose.
"""

ALICE_WORDS = [
  'trash',
  'speed',
  'marriage',
  'dress',
  'match',
  'nerve',
  'govern',
  'fence',
  'celery',
  'fiction',
  'myth',
  'gym',
]
"""Words for test user Alice.

    These words generate a real Helium account and should be considered COMPROMISED.
    Don't send any money to them that you don't want to lose.
"""

BOB_B58 = b'13M8dUbxymE3xtiAXszRkGMmezMhBS8Li7wEsMojLdb4Sdxc4wc'
"""B58 for Bob."""

ALICE_B58 = b'148d8KTRcKA5JKPekBcKFd4KfvprvFRpjGtivhtmRmnZ8MFYnP3'
"""B58 for Alice."""

BOB_BIP_39_WORDS = [word if word != 'energy' else 'episode' for word in BOB_WORDS]
"""BIP 39 Words for Bob."""


@dataclass
class TestUser:
    """Data for a test user."""

    words: str
    b58: bytes
    keypair: Keypair
    bip_39_words: Optional[str] = None


@dataclass
class TestUsers:
    """Users to be used in tests."""

    bob: TestUser
    alice: TestUser


def get_test_users():
    """Fixture to provide user objects to test cases."""
    return TestUsers(
        bob=TestUser(
            words=BOB_WORDS,
            b58=BOB_B58,
            keypair=Keypair.from_words(BOB_WORDS),
            bip_39_words=BOB_BIP_39_WORDS,
        ),
        alice=TestUser(
            words=ALICE_WORDS,
            b58=ALICE_B58,
            keypair=Keypair.from_words(ALICE_WORDS),
        ),
    )
