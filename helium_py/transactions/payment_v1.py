"""Payment V1 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class PaymentV1(Transaction):
    """Payment V1 Transaction Class."""

    type: str = 'payment_v1'
    proto_model_class = proto.BlockchainTxnPaymentV1
    proto_txn_field = 'payment'
    fields = {
        'addresses': (
            'payer',
            'payee',
        ),
        'signatures': (
            'signature',
        ),
        'integers': (
            'nonce',
            'fee',
            'amount',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'payer': 'signature',
    }
