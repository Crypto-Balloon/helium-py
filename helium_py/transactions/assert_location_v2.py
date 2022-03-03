"""Assert Location V2 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.mixins import AssertLocationMixin
from helium_py.transactions.transaction import Transaction


@transaction_class
class AssertLocationV2(AssertLocationMixin, Transaction):
    """Assert Location V2 Transaction Class."""

    type = 'assert_location_v2'
    proto_model_class = proto.BlockchainTxnAssertLocationV2
    proto_txn_field = 'assert_location_v2'
    fields = {
        'addresses': (
            'owner',
            'gateway',
            'payer',
        ),
        'signatures': (
            'owner_signature',
            'payer_signature',
        ),
        'integers': (
            'nonce',
            'fee',
            'staking_fee',
            'gain',
            'elevation',
        ),
        'strings': (
            'location',
        )
    }
    defaults = {
        'fee': 'calculated_fee',
        'staking_fee': 'staking_fee_txn_assert_location_v1',
    }
    keypairs = {
        'owner': 'owner_signature',
        'payer': 'payer_signature',
    }
