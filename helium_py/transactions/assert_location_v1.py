"""Assert Location V1 Transaction Class."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.mixins import AssertLocationMixin
from helium_py.transactions.transaction import Transaction


@transaction_class
class AssertLocationV1(AssertLocationMixin, Transaction):
    """Assert Location V1 Transaction Class."""

    type: str = 'assert_location_v1'
    proto_model_class = proto.BlockchainTxnAssertLocationV1
    proto_txn_field = 'assert_location'
    fields = {
        'addresses': (
            'owner',
            'gateway',
            'payer',
        ),
        'signatures': (
            'owner_signature',
            'gateway_signature',
            'payer_signature',
        ),
        'integers': (
            'nonce',
            'fee',
            'staking_fee',
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
        'gateway': 'gateway_signature',
        'payer': 'payer_signature',
    }
