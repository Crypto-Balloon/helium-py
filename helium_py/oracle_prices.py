"""Oracle Prices client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import limit_api, time_filterable_api


class OraclePrices(API):
    """Oracle Prices client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/oracle-prices/
    """

    base_path = 'oracle'

    def all(self) -> Generator[dict, None, None]:
        """Yield all price data."""
        return self.client.fetch_all(path='/prices')

    @limit_api
    @time_filterable_api
    def all_activity(self, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all oracle activity."""
        return self.client.fetch_all(path='/activity', params=params)

    @limit_api
    @time_filterable_api
    def all_activity_for_oracle(self, address: str, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all activity for specific oracle with provided address.

        Args:
            address: The oracle addres to fetch activity for.
            params: Limit and time filter parameters
        """
        return self.client.fetch_all(path=f'/{address}/activity', params=params)

    def get_current(self) -> dict:
        """Return the current oracle price data."""
        return self.client.get(path='/prices/current')

    def get_price_at_block(self, block: int) -> dict:
        """Return price at a specific block.

        Args:
            block: The block to retrieve price data for.
        """
        return self.client.get(path=f'/prices/{block}')

    @time_filterable_api
    def get_stats(self, params: Optional[dict]) -> dict:
        """Return price stats."""
        return self.client.get(path='/prices/stats', params=params)

    def predictions(self) -> Generator[dict, None, None]:
        """Yield price predictions.

        May return one or more so caller should be prepared to handle StopIteration.
        """
        return self.client.fetch_all(path='/predictions')
