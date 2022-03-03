"""Payment V2 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class PaymentV2(Transaction):
    """Payment V2 Transaction Class."""

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
