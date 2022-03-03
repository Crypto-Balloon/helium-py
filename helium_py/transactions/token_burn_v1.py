"""Token Burn V1 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class TokenBurnV1(Transaction):
    """Token Burn V1 Transaction Class."""

    type: str = 'token_burn_v1'
    proto_model_class = proto.BlockchainTxnTokenBurnV1
    proto_txn_field = 'token_burn'
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
            'nonce',
            'fee',
            'memo',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'payer': 'signature',
    }
