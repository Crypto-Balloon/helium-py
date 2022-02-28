"""Replace Placeholder Docstring."""
from helium_py import proto
from helium_py.transactions.decorators import transaction_class
from helium_py.transactions.transaction import Transaction


@transaction_class
class AddGatewayV1(Transaction):
    """Replace Placeholder Docstring."""

    type = 'add_gateway_v1'
    proto_model_class = proto.BlockchainTxnAddGatewayV1
    proto_txn_field = 'add_gateway'
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
            'fee',
            'staking_fee',
        ),
    }
    defaults = {
        'fee': 'calculated_fee',
        'staking_fee': 'staking_fee_txn_add_gateway_v1',
    }
    keypairs = {
        'owner': 'owner_signature',
        'gateway': 'gateway_signature',
        'payer': 'payer_signature',
    }

    def get_calculate_fee_kwargs(self):
        """Replace placeholder docstrings."""
        fee_kwargs = super().get_calculate_fee_kwargs()
        if not self.payer:
            try:
                del fee_kwargs['payer_signature']
            except KeyError:
                pass
        return fee_kwargs
