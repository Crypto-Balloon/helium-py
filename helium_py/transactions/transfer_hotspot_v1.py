"""Transfer Hotspot V1 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class TransferHotspotV1(Transaction):
    """Transfer Hotspot V1 Transaction Class."""

    type: str = 'transfer_hotspot_v1'
    proto_model_class = proto.BlockchainTxnTransferHotspotV1
    proto_txn_field = 'transfer_hotspot'
    fields = {
        'addresses': (
            'gateway',
            'seller',
            'buyer',
        ),
        'signatures': (
            'seller_signature',
            'buyer_signature',
        ),
        'integers': (
            'amount_to_seller',
            'fee',
            'buyer_nonce',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
    }
    keypairs = {
        'seller': 'seller_signature',
        'buyer': 'buyer_signature',
    }
