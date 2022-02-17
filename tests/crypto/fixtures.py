from helium_py.crypto.keypair import Keypair

bobWords = [
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
aliceWords = [
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
bobB58 = '13M8dUbxymE3xtiAXszRkGMmezMhBS8Li7wEsMojLdb4Sdxc4wc'
aliceB58 = '148d8KTRcKA5JKPekBcKFd4KfvprvFRpjGtivhtmRmnZ8MFYnP3'

bobBip39Words = ['episode' if word == 'energy' else word for word in bobWords]

usersFixture = {
  'bob': Keypair.from_words(bobWords),
  'alice': Keypair.from_words(aliceWords),
}