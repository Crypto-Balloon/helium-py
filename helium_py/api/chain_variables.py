"""Chain Variables client for Helium Blockchain API."""

from typing import Any, Generator, Optional

from .api import API
from .decorators import limit_api, time_filterable_api


class ChainVariables(API):
    """Chain Variables client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/chain-variables
    """

    base_path = 'vars'

    @limit_api
    @time_filterable_api
    def get_all(self, params: Optional[dict]) -> dict:
        """Return all chain variables."""
        return self.client.get(params=params)

    def get_by_name(self, var_name: str) -> Any:
        """Return a var identified by var_name."""
        return self.client.get(path=f'/{var_name}')

    def all_activity(self) -> Generator[dict, None, None]:
        """Yield all chain variable activity."""
        return self.client.fetch_all(path='/activity')
