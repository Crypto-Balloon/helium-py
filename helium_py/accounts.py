"""Accounts client for Helium Blockchain API."""

from typing import Optional

from .api import API
from .decorators import (
    bucket_api,
    filter_modes_api,
    filter_transaction_types_api,
    limit_api,
    time_filterable_api,
)


class Accounts(API):
    """Accounts client class for Helium Blockchain API.

    https://docs.helium.com/api/blockchain/accounts
    """

    base_path = 'accounts'

    def all(self):
        """Yield all accounts."""
        return self.client.fetch_all()

    @limit_api
    def richest(self, params: Optional[dict]):
        """Yield all accounts."""
        return self.client.get(path='/rich', params=params if params else None)

    def account_for_address(self, address: str):
        """Yield accounts for a account."""
        return self.client.get(path=f'/{address}')

    @filter_modes_api
    def hotspots_for_account(self, address: str, params: Optional[dict]):
        """Return a account identified by account_id."""
        return self.client.fetch_all(path=f'/{address}/hotspots', params=params if params else None)

    def validators_for_account(self, address: str):
        """Return a account identified by account_id."""
        return self.client.fetch_all(path=f'/{address}/validators')

    def ouis_for_account(self, address: str):
        """Return a account identified by account_id."""
        return self.client.fetch_all(path=f'/{address}/ouis')

    @limit_api
    @time_filterable_api
    @filter_transaction_types_api
    def get_account_activity(self, address: str, params: Optional[dict]):
        """Return a account identified by account_id."""
        return self.client.fetch_all(path=f'/{address}/activity', params=params if params else None)

    @filter_transaction_types_api
    def get_account_activity_counts(self, address: str, params: Optional[dict]):
        """Return a account identified by account_id."""
        return self.client.get(path=f'/{address}/activity/count', params=params if params else None)

    @limit_api
    @time_filterable_api
    def get_account_elections(self, address: str, params: Optional[dict]):
        """Return a account identified by account_id."""
        return self.client.get(path=f'/{address}/elections', params=params if params else None)

    @limit_api
    @time_filterable_api
    def challenges_for_account(self, address: str, params: Optional[dict]):
        """Return a account identified by account_id."""
        return self.client.fetch_all(path=f'/{address}/challenges', params=params if params else None)

    def pending_transactions_for_account(self, address: str):
        """Return a account identified by account_id."""
        return self.client.fetch_all(path=f'/{address}/pending_transactions')

    @time_filterable_api
    def get_account_rewards(self, address: str, params: Optional[dict]):
        """Return a account identified by account_id."""
        return self.client.fetch_all(path=f'/{address}/rewards', params=params if params else None)

    @bucket_api
    @time_filterable_api
    def get_account_rewards_total(self, address: str, params: Optional[dict]):
        """Return a account identified by account_id."""
        return self.client.get(path=f'/{address}/rewards/sum', params=params if params else None)

    def get_stats_for_account(self, address: str):
        """Return stats for an account."""
        return self.client.get(path=f'/{address}/stats')
