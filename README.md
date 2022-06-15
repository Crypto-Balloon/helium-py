<p align="center">
<img src="https://raw.githubusercontent.com/Crypto-Balloon/helium-py/main/helium-py.png" width="120px" height="120px" alt="helium-py logo" title="helium.py">
</p>

# helium-py
![https://crypto-balloon.github.io/helium-py/](https://github.com/Crypto-Balloon/helium-py/actions/workflows/docs.yml/badge.svg)
![Test](https://github.com/Crypto-Balloon/helium-py/actions/workflows/test.yml/badge.svg)
![https://pypi.org/project/helium-py/](https://github.com/Crypto-Balloon/helium-py/actions/workflows/pypi.yml/badge.svg)
![https://pepy.tech/project/helium-py](https://pepy.tech/badge/helium-py/month)
![https://pypi.org/project/helium-py/](https://img.shields.io/pypi/l/helium-py.svg)
![https://pypi.org/project/helium-py/](https://img.shields.io/pypi/pyversions/helium-py.svg)

## Versioning

This project follows [semantic versioning](https://semver.org/). Prior to 1.0.0 this project does not
guarantee a stable public API.

## Installation

To use helium-py, first install it using pip:

```console
$ pip install helium-py
```

## Example Transactions

For more example transactions and full module documentation, view the [full documentation](https://crypto-balloon.github.io/helium-py/).

For full API specification and network documentation please reference [docs.helium.com](https://docs.helium.com/api/blockchain).

### Creating and submitting a payment transaction
A payment from an owned keypair initialized with a 12 word mnemonic to an address specified by its base58 representation. The transaction is serialized to binary and submitted to the blockchain API.


```python
import logging

from helium_py.crypto.keypair import Address, Keypair
from helium_py.transactions import Payment, PaymentV2
from helium_py.api import Accounts, PendingTransactions, Transactions

logger = logging.getLogger(__name__)

# Initialize an owned keypair from a 12 word mnemonic
bob = Keypair.from_words(['one', 'two', ..., 'twelve'])

# Initialize an address from a b58 string
alice = Address.from_b58(b'148d8KTRcKA5JKP ekBcKFd4KfvprvFRpjGtivhtmRmnZ8MFYnP3')

# get the speculative nonce for the keypair
account = Accounts().account_for_address(bob.address.b58.decode())

payment_transaction = PaymentV2(
    payer=bob.address,
    payments=[
        Payment(
            payee=alice,
            amount=10,
            memo=b'memo',
        ),
    ],
    nonce=account['speculative_nonce'] + 1,
)

# an appropriate transaction fee is calculated at initialization
logger.info(f'transaction fee is: {payment_transaction.calculated_fee}')

# sign the payment txn with bob's keypair
signed_payment_transaction = payment_transaction.sign(payer=bob)

# submit the serialized txn to the Blockchain HTTP API
pending_transactions_client = PendingTransactions()
response_dict = pending_transactions_client.submit_transaction(signed_payment_transaction)

# check on status of pending transaction
pending_transactions_client.get_status(response_dict['hash'])

# view finalized transaction information
transaction_dict = Transactions().get_transaction(response_dict['hash'])
```
