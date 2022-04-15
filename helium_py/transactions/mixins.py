"""Mixin Classes for use in transactions classes."""


class AssertLocationMixin:
    """Mixin for AssertLocation transactions."""

    def get_calculate_fee_kwargs(self):
        """Remove payer_signature if no payer present."""
        fee_kwargs = getattr(super(), 'get_calculate_fee_kwargs')()
        fee_kwargs['staking_fee'] = getattr(self, 'orig_kwarg_gt0_or_none')('staking_fee')
        if not getattr(self, 'payer') and 'payer_signature' in fee_kwargs:
            del fee_kwargs['payer_signature']
        return fee_kwargs
