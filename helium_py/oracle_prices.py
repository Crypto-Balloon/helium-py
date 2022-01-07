"""Oracle Prices client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import time_filterable_api


class OraclePrices(API):
    """Oracle Prices client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/oracle-prices/
    """

    base_path = 'oracle'

    def all(self, **kwargs):
        """Yield all price data."""
        return self.client.fetch_all(path='/prices', **kwargs)

    @time_filterable_api(has_limit=True)
    def all_activity(self, params: Optional[dict], **kwargs):
        """Yield all oracle activity."""
        return self.client.fetch_all(path='/activity', params=params, **kwargs)

    @time_filterable_api(has_limit=True)
    def all_activity_for_oracle(self, params: Optional[dict], address: str, **kwargs):
        """Yield all activity for specific oracle.

        Args:
            address: The oracle addres to fetch activity for.
        """
        return self.client.fetch_all(path=f'{address}/activity', params=params, **kwargs)

    def get_current(self, **kwargs):
        """Get the current oracle price data."""
        return list(self.client.fetch_all(path='/prices/current', **kwargs))[0]

    def get_price_at_block(self, block: int, **kwargs):
        """Return price at a specific block.

        Args:
            block: The block to retrieve price data for.
        """
        return list(self.client.fetch_all(path=f'/prices/{block}', **kwargs))[0]

    @time_filterable_api
    def get_stats(self, params: Optional[dict], **kwargs):
        """Get price stats."""
        return list(self.client.fetch_all(path='/prices/stats', params=params, **kwargs))[0]

    def predictions(self, **kwargs):
        """Yield price predictions.

        May return one or more so caller should be prepared to handle StopIteration.
        """
        return self.client.fetch_all(path='/predictions', **kwargs)
