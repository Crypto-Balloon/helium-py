==========
Quickstart
==========

.. contents:: Table of Contents
    :depth: 2

Installation
============

To use helium-py, first install it using pip:

.. code-block:: console

   $ pip install helium-py

Example Transactions
====================

Creating and submitting a payment transaction
---------------------------------------------
A payment from an owned keypair initialized with a 12 word mnemonic to an address specified by its base58 representation. The transaction is serialized to binary and submitted to the blockchain API.

.. code-block:: python

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
        payer=bob,
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
