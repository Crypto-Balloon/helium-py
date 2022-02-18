# flake8: noqa
from helium_py.crypto.keypair import Keypair

bob_words = [
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
alice_words = [
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
bobB58 = b'13M8dUbxymE3xtiAXszRkGMmezMhBS8Li7wEsMojLdb4Sdxc4wc'
aliceB58 = b'148d8KTRcKA5JKPekBcKFd4KfvprvFRpjGtivhtmRmnZ8MFYnP3'

bob_bip39_words = ['episode' if word == 'energy' else word for word in bob_words]

bob = Keypair.from_words(bob_words)
alice = Keypair.from_words(alice_words)
