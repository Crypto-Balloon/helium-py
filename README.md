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

- [ ] __KeyType__

- [ ] __Utils__

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
