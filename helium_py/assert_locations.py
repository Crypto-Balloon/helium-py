"""Assert Locations client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import time_filterable_api


class AssertLocations(API):
    """Assert Locations client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/assert-locations
    """

    base_path = 'assert_locations'

    @time_filterable_api(has_limit=True)
    def all(self, params: Optional[dict], **kwargs):
        """Yield all assert location transactions."""
        return self.client.fetch_all(params=params, **kwargs)
