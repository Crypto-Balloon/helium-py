"""Mixin Classes for use in transactions classes."""


class AssertLocationMixin:
    """Mixin for AssertLocation transactions."""

    def get_calculate_fee_kwargs(self):
        """Remove payer_signature if no payer present."""
        fee_kwargs = super().get_calculate_fee_kwargs()
        fee_kwargs['staking_fee'] = self.orig_kwarg_gt0_or_none('staking_fee')
        if not self.payer:
            try:
                del fee_kwargs['payer_signature']
            except KeyError:
                pass
        return fee_kwargs
