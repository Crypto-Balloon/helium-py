"""Transfer Hotspot V2 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class TransferHotspotV2(Transaction):
    """Transfer Hotspot V2 Transaction Class."""

    type: str = 'transfer_hotspot_v2'
    proto_model_class = proto.BlockchainTxnTransferHotspotV2
    proto_txn_field = 'transfer_hotspot_v2'
    fields = {
        'addresses': (
            'gateway',
            'owner',
            'new_owner',
        ),
        'signatures': (
            'owner_signature',
        ),
        'integers': (
            'fee',
            'nonce',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'owner': 'owner_signature',
    }
