"""Validators client for Helium Blockchain API."""

from typing import Generator, List, Optional

from .api import API
from .decorators import (
    bucket_api,
    filter_transaction_types_api,
    limit_api,
    time_filterable_api,
)


class Validators(API):
    """Validators client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/validators
    """

    base_path = 'validators'

    def all(self) -> Generator[dict, None, None]:
        """Yield all validators."""
        return self.client.fetch_all()

    def validator_for_address(self, address: str) -> dict:
        """Return validators for provided address."""
        return self.client.get(path=f'/{address}')

    def validators_for_name(self, name: str) -> List[dict]:
        """Return validators identified by provided three-word animal name."""
        if len(name.split(' ')) == 3:
            name = '-'.join(name.split(' ')).lower()
        return self.client.get(path=f'/name/{name}')

    def validators_search_by_name(self, name: str) -> List[dict]:
        """Search for validators by name."""
        return self.client.get(path='/name', params={'search': name})

    @limit_api
    @time_filterable_api
    @filter_transaction_types_api
    def get_roles(self, address: str, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield all roles for provided validator address."""
        return self.client.fetch_all(path=f'/{address}/roles', params=params if params else None)

    @filter_transaction_types_api
    def get_roles_counts(self, address: str, params: Optional[dict]) -> dict:
        """Return roles counts for provided validator address."""
        return self.client.get(path=f'/{address}/roles/count', params=params if params else None)

    def get_stats(self) -> dict:
        """Return stats for all validators."""
        return self.client.get(path='/stats')

    def get_currently_elected_validators(self) -> List[dict]:
        """Return currently elected validators."""
        return self.client.get(path='/elected')

    def get_elected_validators_by_height(self, height: int) -> List[dict]:
        """Return elected validators for the provided block height."""
        return self.client.get(path=f'/elected/{height}')

    def get_elected_validators_by_election(self, election_hash: str) -> List[dict]:
        """Return elected validators for the provided block height."""
        return self.client.get(path=f'/elected/hash/{election_hash}')

    @time_filterable_api
    def get_validator_rewards(self, address: str, params: Optional[dict]) -> Generator[dict, None, None]:
        """Yield rewards information for a validator identified by validator_id."""
        return self.client.fetch_all(path=f'/{address}/rewards', params=params if params else None)

    @bucket_api
    @time_filterable_api
    def get_validator_rewards_total(self, address: str, params: Optional[dict]) -> dict:
        """Return rewards totals for a validator identified by validator_id."""
        return self.client.get(path=f'/{address}/rewards/sum', params=params if params else None)

    @time_filterable_api
    def get_all_validator_rewards_total(self, params: Optional[dict]) -> dict:
        """Return rewards totals for all validators."""
        return self.client.get(path='/rewards/sum', params=params if params else None)
