"""Chain Variables client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import time_filterable_api, limit_api


class ChainVariables(API):
    """Chain Variables client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/chain-variables
    """

    base_path = 'vars'

    @limit_api
    @time_filterable_api
    def get_all(self, params: Optional[dict], **kwargs):
        """Yield all chain variables."""
        return list(self.client.fetch_all(params=params, **kwargs))[0]

    def get_by_name(self, var_name: str):
        """Return a var identified by var_name.

        Args:
            var_name: The name of a chain variable.
        """
        return list(self.client.fetch_all(path=f'/{var_name}'))[0]

    def all_activity(self, **kwargs):
        """Yield all chain variable activity."""
        return self.client.fetch_all(path='/activity', **kwargs)
