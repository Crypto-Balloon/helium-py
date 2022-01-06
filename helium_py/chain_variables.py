"""Chain Variables client for Helium Blockchain API."""

from typing import Optional

from .client import Client
from .decorators import time_filterable_api


class ChainVariables(Client):
    """Chain Variables client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/chain-variables
    """

    base_path = 'vars'

    @time_filterable_api
    def get_all(self, params: Optional[dict], **kwargs):
        """Yield all chain variables."""
        return list(super().all(params=params, **kwargs))[0]

    def get_by_name(self, var_name: str):
        """Return a var identified by var_name.

        Args:
            var_name: The name of a chain variable.
        """
        return list(self.all(path=f'/{var_name}'))[0]

    def all_activity(self, **kwargs):
        """Yield all chain variable activity."""
        return super().all(path='/activity', **kwargs)
