"""Replace Placeholder Docstring."""
from helium_py import proto
from helium_py.transactions.transaction import Transaction


class PaymentV2(Transaction):
    """Replace Placeholder Docstring."""

    type: str = 'payment_v2'
    proto_model_class = proto.BlockchainTxnPaymentV2
    proto_txn_field = 'payment_v2'
    fields = {
        'addresses': (
            'payer',
        ),
        'signatures': (
            'signature',
        ),
        'integers': (
            'fee',
            'nonce',
        ),
        'payment_lists': (
            'payments',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'payer': 'signature',
    }
