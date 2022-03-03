"""Transfer Validator Stake V1 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class TransferValidatorStakeV1(Transaction):
    """Transfer Validator Stake V1 Transaction Class."""

    type: str = 'transfer_validator_stake_v1'
    proto_model_class = proto.BlockchainTxnTransferValidatorStakeV1
    proto_txn_field = 'transfer_val_stake'
    fields = {
        'addresses': (
            'old_address',
            'new_address',
            'old_owner',
            'new_owner',
        ),
        'signatures': (
            'old_owner_signature',
            'new_owner_signature',
        ),
        'integers': (
            'stake_amount',
            'payment_amount',
            'fee',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'old_owner': 'old_owner_signature',
        'new_owner': 'new_owner_signature',
    }
