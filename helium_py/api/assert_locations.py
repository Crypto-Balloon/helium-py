"""Assert Locations client for Helium Blockchain API."""

from typing import Generator, Optional

from .api import API
from .decorators import limit_api, time_filterable_api


class AssertLocations(API):
    """Assert Locations client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/assert-locations
    """

    base_path = 'assert_locations'

    @limit_api
    @time_filterable_api
    def all(self, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all assert location transactions."""
        return self.client.fetch_all(params=params)
