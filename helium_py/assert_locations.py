"""Assert Locations client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class AssertLocations(Client):
    """Assert Locations client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/assert-locations
    """

    base_path = 'assert_locations'

    @time_filterable_api
    def all(self, params: Optional[dict], **kwargs):
        """Yield all assert location transactions."""
        return super().all(params=params, **kwargs)
