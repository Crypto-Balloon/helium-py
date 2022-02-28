"""Replace Placeholder Docstring."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class SecurityExchangeV1(Transaction):
    """Replace Placeholder Docstring."""

    type: str = 'security_exchange_v1'
    proto_model_class = proto.BlockchainTxnSecurityExchangeV1
    proto_txn_field = 'security_exchange'
    fields = {
        'addresses': (
            'payer',
            'payee',
        ),
        'signatures': (
            'signature',
        ),
        'integers': (
            'amount',
            'fee',
            'nonce',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'payer': 'signature',
    }
