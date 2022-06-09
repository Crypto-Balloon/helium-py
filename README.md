<p align="center">
<img src="https://raw.githubusercontent.com/Crypto-Balloon/helium-py/main/helium-py.png" width="120px" height="120px" alt="helium-py logo" title="helium.py">
</p>

# helium-py
![Test](https://github.com/Crypto-Balloon/helium-py/actions/workflows/test.yml/badge.svg)

## Versioning

This project follows [semantic versioning](https://semver.org/). Prior to 1.0.0 this project does not
guarantee a stable public API.

## Modules

- [api](#api)
- [crypto](#crypto)
- [currency](#currency)
- [onboarding](#onboarding)
- [proto](#proto)
- [test](#test)
- [transactions](#transactions)

### API

The API module classes provide client classes for interacting with the Helium APIs.

For full API specification and documentation please reference [docs.helium.com](https://docs.helium.com/api/blockchain).

```python
from datetime import datetime, timedelta
from helium_py.api import ChainVariables, Hotspots

# Example of fetching chain variables
chain_vars = ChainVariables()  # Create a ChainVariables client
print(chain_vars.get_all())    # Get all chain variables

# Example of fetching hotspot earnings for the last five days
hotspot_address = "some_valid_hotspot_address"
hotspots = Hotspots()
hotspots.get_hotspot_rewards_total(hotspot_address, min_time=datetime.now() - timedelta(days=5))
```

### Crypto

The Crypto module classes provide Address, Keypair, and Mnemonic classes as well as helpful utilities.

```python
from helium_py.crypto.keypair import Keypair

# Example of creating a random keypair, accessing the address, and signing a message
keypair = Keypair.make_random()
address = keypair.address.b58  # B58 public key address
keypair.sign(b'message')  # Sign a message with keypair private key
```
