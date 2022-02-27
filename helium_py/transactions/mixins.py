"""Replace Placeholder Docstring."""


class AssertLocationMixin:
    """Replace Placeholder Docstring."""

    def get_calculate_fee_kwargs(self):
        """Replace placeholder docstrings."""
        fee_kwargs = super().get_calculate_fee_kwargs()
        fee_kwargs['staking_fee'] = self.orig_kwarg_gt0_or_none('staking_fee')
        if not self.payer:
            try:
                del fee_kwargs['payer_signature']
            except KeyError:
                pass
        return fee_kwargs
