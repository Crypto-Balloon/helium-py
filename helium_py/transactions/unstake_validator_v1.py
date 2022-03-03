"""Unstake Validator V1 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class UnstakeValidatorV1(Transaction):
    """Unstake Validator V1 Transaction Class."""

    type: str = 'unstake_validator_v1'
    proto_model_class = proto.BlockchainTxnUnstakeValidatorV1
    proto_txn_field = 'unstake_validator'
    fields = {
        'addresses': (
            'address',
            'owner',
        ),
        'signatures': (
            'owner_signature',
        ),
        'integers': (
            'stake_amount',
            'stake_release_height',
            'fee',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'owner': 'owner_signature',
    }
