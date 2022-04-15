"""Initial integration tests for transactions."""
from helium_py.api.api import API

from .constants import DEWI_ONBOARDING_BASE_URL


class OnboardingClient(API):
    """OnboardingClient class for integration with onboarding server."""

    host = DEWI_ONBOARDING_BASE_URL
    base_path = '/api/v2'

    def __init__(self, host=None):
        """Initialize OnboardingClient with a custom host."""
        super().__init__()
        if host:
            self.host = host

    def get_onboarding_record(self, address: str):
        """Return onboarding record for provided hotspot address."""
        return self.client.get(f'/hotspots/{address}')

    def get_makers(self):
        """Return list of makers."""
        return self.client.get('/makers')

    def get_firmware(self):
        """Return current firmware version."""
        return self.client.get('/firmware')

    def post_payment_transaction(self, address: str, txn: str):
        """Post payment transaction and return response."""
        return self.client.post(f'/transactions/pay/{address}', json={'txn': txn})
