"""Oracle Prices client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class OraclePrices(Client):
    """Oracle Prices client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/oracle/prices/
    """

    base_path = 'oracle'

    def all_prices(self, **kwargs):
        """Yield all price data."""
        return super().all(path='/prices', **kwargs)

    @time_filterable_api(has_limit=True)
    def all_activity(self, params: Optional[dict], **kwargs):
        """Yield all oracle activity."""
        return super().all(path='/activity', params=params, **kwargs)

    @time_filterable_api(has_limit=True)
    def all_activity_for_oracle(self, params: Optional[dict], address: str, **kwargs):
        """Yield all activity for specific oracle.

        Args:
            address: The oracle addres to fetch activity for.
        """
        return super().all(path=f'{address}/activity', params=params, **kwargs)

    def get_current(self, **kwargs):
        """Get the current oracle price data."""
        return list(super().all(path='/prices/current', **kwargs))[0]

    def get_price_at_block(self, block: int, **kwargs):
        """Return price at a specific block.

        Args:
            block: The block to retrieve price data for.
        """
        return list(self.all(path=f'/prices/{block}', **kwargs))[0]

    @time_filterable_api
    def get_stats(self, params: Optional[dict], **kwargs):
        """Get price stats."""
        return list(super().all(path='/prices/stats', params=params, **kwargs))[0]

    def predictions(self, **kwargs):
        """Yield price predictions.

        May return one or more so caller should be prepared to handle StopIteration.
        """
        return super().all(path='/predictions', **kwargs)
