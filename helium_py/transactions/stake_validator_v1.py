"""Replace Placeholder Docstring."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import NewTransaction


@transaction_class
class StakeValidatorV1(NewTransaction):
    """Replace Placeholder Docstring."""

    type: str = 'stake_validator_v1'
    proto_model_class = proto.BlockchainTxnStakeValidatorV1
    proto_txn_field = 'stake_validator'
    fields = {
        'addresses': (
            'address',
            'owner',
        ),
        'signatures': (
            'owner_signature',
        ),
        'integers': (
            'stake',
            'fee',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'owner': 'owner_signature',
    }
