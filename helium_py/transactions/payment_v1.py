"""Replace Placeholder Docstring."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import NewTransaction


@transaction_class
class PaymentV1(NewTransaction):
    """Replace Placeholder Docstring."""

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
