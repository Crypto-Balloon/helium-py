==========
Quickstart
==========

.. contents:: Table of Contents
    :depth: 3

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
    :linenos:

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

Sending an Account's full balance
----------------------------------------
Sending the maximum amount from an account (leaving a 0 HNT balance) requires taking into account the transaction fee. All fees are denominated in Data Credits (DC), which is equal to $0.00001 USD, meaning 35,000 DC equals $0.35 USD. DC are obtained by burning HNT, permanently removing it from circulation. If you do not already have DC in your account, the appropriate amount of HNT will be burned to cover the fee.

The general formula is: amountToSend = balance - feeInHNT

The packages in helium-js provide utility functions to calculate the above:

.. code-block:: python
    :linenos:

    import logging

    from helium_py.crypto.keypair import Address, Keypair
    from helium_py.transactions import Payment, PaymentV2
    from helium_py.api import Accounts, PendingTransactions, Transactions
    from helium_py.currency import Balance, types

    logger = logging.getLogger(__name__)

    # Initialize an owned keypair from a 12 word mnemonic
    bob = Keypair.from_words(['one', 'two', ..., 'twelve'])

    # Initialize an address from a b58 string
    alice = Address.from_b58(b'148d8KTRcKA5JKPekBcKFd4KfvprvFRpjGtivhtmRmnZ8MFYnP3')

    # get the speculative nonce for the keypair
    account = Accounts().account_for_address(bob.address.b58.decode())

    payment_transaction = PaymentV2(
        payer=bob.address,
        payments=[
            Payment(
                payee=alice,
                amount=account['balance'],
            ),
        ],
        nonce=account['speculative_nonce'] + 1,
    )

    # an appropriate transaction fee is calculated at initialization
    logger.info(f'transaction fee is: {payment_transaction.calculated_fee}')

    fee_in_dc = Balance(payment_transaction.calculated_fee, currency_type=types.DATA_CREDITS)
    fee_in_hnt = fee_in_dc.to_network_tokens()  # Oracle price can be provided manually or automatically injected
    amount_to_send = Balance(account['balance'], currency_type=types.NETWORK_TOKENS).minus(fee_in_hnt)

    payment_transaction_for_fee = PaymentV2(
        payer=bob.address,
        payments=[
            Payment(
                payee=alice,
                amount=amount_to_send,
            ),
        ],
        nonce=account['speculative_nonce'] + 1,
    )

    # sign the payment txn with bob's keypair
    signed_payment_transaction = payment_transaction_for_fee.sign(payer=bob)

    # submit the serialized txn to the Blockchain HTTP API
    pending_transactions_client = PendingTransactions()
    response_dict = pending_transactions_client.submit_transaction(signed_payment_transaction)

    # check on status of pending transaction
    pending_transactions_client.get_status(response_dict['hash'])

    # view finalized transaction information
    transaction_dict = Transactions().get_transaction(response_dict['hash'])