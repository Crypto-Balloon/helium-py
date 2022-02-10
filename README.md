# helium-py

<img src="helium-py.png" width="250px" height="250px" alt="helium-py logo" title="helium.py">

## Versioning

This project follows [semantic versioning](https://semver.org/). Prior to 1.0.0 this project does not
guarantee a stable public API.

## Progress

Feature parity with Helium-JS is tracked here.

### Crypto Module

- [ ] __Base-58 Address__

  - [ ] Class `Address` with fields and methods:

    * [ ] __Fields:__
      * `version` - number
      * `netType` - `NetType` object
      * `keyType` - `KeyType` object
      * `publicKey` - Uint8Array

    * [ ] __Methods:__
      * [ ] `bin` - concats nettype | keytype with public key
      * [ ] `b58` - encodes version with prefix (result of bin method call) to string using [bs58CheckEncode](https://www.npmjs.com/package/tezbridge-crypto/v/1.0.31?activeTab=dependencies#tezbridgecryptocodecbs58checkencodeinput_bytes-prefix)
      * [ ] `fromB58` - constructs a new instance of `Address` by getting version, net type, key type, and public key from b58 string (using bs58* methods from utils; see below)
      * [ ] `fromBin` - constructs a new instance of `Address` by getting version, net type, key type, and public key from binary buffer passed in (using byteTo* methods from utils; see below)
      * [ ] `isValid` - takes a b58 string and returns true if Address.fromB58 does not throw, otherwise false

- [ ] __Mnemonic__

  Imports English wordlist JSON for mapping to a random mnemonic.

  - [ ] Class `Mnemonic` with fields and methods:

    * [ ] __Fields:__
      * `words` - Array<string>

    * [ ] __Methods:__
      * [ ] `create` - takes a length (defaults to 12, can also be 24) and constructs a new Mnemonic object from random bytes generated with a seed of (16/12) * length using the `fromEntropy` methods (see below)
      * [ ] `fromEntropy` - takes a entropy buffer of random bytes (16 < len < 32 and divisible by 4), converts to binary bits and a checksum (using `deriveChecksumBits` method from utils; see below), and maps the bits to words in the wordlist, generating the new `Mnemonic` object from the selected words
      * [ ] `toEntropy` - converts a `Mnenomic` object back into a bit string, checksum is calculated (again using `deriveChecksumBits`) and verified (throws if invalid)

- [ ] __Keypair__

- [ ] __Address__

- [ ] __NetType__

  Defines constants to indicate the network used, either test or main.

  * [ ] `MAINNET` - constant 0x00
  * [ ] `TESTNET` - constant 0x10
  * [ ] `SUPPORTED_NET_TYPES` - list containing the above two constants
  * [ ] `NetType` - type represented as a number

- [ ] __KeyType__

  Defines constants to indicate the public key type, either ECC or ED25519.

  * [ ] `ECC_COMPACT_KEY_TYPE` - constant 0
  * [ ] `ED25519_KEY_TYPE` - constant 1
  * [ ] `SUPPORTED_KEY_TYPES` - list containing the above two constants
  * [ ] `KeyType` - type represented as a number

- [ ] __Utils__

  Utility functions used by classes in the crypto module.

  * __Functions:__
    * [ ] `randomBytes` - uses libsodium to generate random bytes from a passed seed number
    * [ ] `sha256` - generates a SHA256 digest of the buffer passed in
    * [ ] `lpad` - takes a source string, a pad string, and a length and left-pads the source string with the pad string until it is greater than or equal to the length requested
    * [ ] `bytesToBinary` - takes a buffer of bytes and returns a binary string representation
    * [ ] `binaryToByte` - takes a string of 0s and 1s and parses it as binary, returning a number
    * [ ] `deriveChecksumBits` - calculates the checksum of a passed buffer using the sha256 helper
    * [ ] `bs58CheckEncode` - base-58 encodes a passed binary buffer payload after concatinating it with its checksum
    * [ ] `bs58ToBin` - extracts the payload from a base-58 encoded string and verifies its checksum before returning the binary data
    * [ ] `byteToNetType` - bitwise ANDs a byte with 0xf0, producing a NetType object
    * [ ] `byteToKeyType` - bitwise ANDs a byte with 0x0f, producing a KeyType object
    * [ ] `bs58NetType` - takes a base-58 encoded address string and returns its NetType from the first byte
    * [ ] `bs58KeyType` - takes a base-58 encoded address string and returns its KeyType from the first byte
    * [ ] `bs58Version` - takes a base-58 encoded address string and returns its version from the first byte
    * [ ] `bs58PublicKey` - takes a base-58 encoded address string and returns its public key from the second byte

### Transactions Module

### Proto Module

### HTTP Module

- [X] Connection management

- [X] In-memory page caching

- [/] API module coverage ([helium docs](https://docs.helium.com/api/blockchain/introduction)):

  - [X] Stats

  - [X] Blocks

  - [X] Accounts

  - [X] Validators

  - [X] Hotspots

  - [X] Cities

  - [X] Locations

  - [X] Transactions
 
  - [X] Pending Transactions

  - [X] Oracle Prices

  - [X] Chain Variables

  - [X] OUIs

  - [X] Rewards

  - [X] DC Burns

  - [X] Challenges

  - [X] Elections

  - [X] State Channels

  - [X] Assert Locations

### Currency Module
