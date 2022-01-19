"""Constants for Helium Blockchain API."""
HELIUM_API_DEFAULT_VERSION = 'v1'
HELIUM_API_DEFAULT_HOST = 'api.helium.io'
HELIUM_API_BETA_HOST = 'api.helium.wtf'
HELIUM_API_TESTNET_HOST = 'testnet-api.helium.wtf'
HELIUM_API_OFFICIAL_HOSTS = {
    HELIUM_API_DEFAULT_HOST,
    HELIUM_API_BETA_HOST,
    HELIUM_API_TESTNET_HOST,
}
VALID_BUCKETS = ('hour', 'day', 'week')
VALID_FILTER_MODES = ('full', 'dataonly', 'light')
VALID_FILTER_TYPES = (
    'add_gateway',
    'assert_location',
    'chain_vars',
    'coinbase',
    'coinbase_data_credits',
    'consensus_group',
    'create_hashed_timelock',
    'create_proof_of_coverage_request',
    'data_credits',
    'genesis_gateway',
    'multi-payment',
    'OUI',
    'payment',
    'proof_of_coverage_receipts',
    'redeem_hashed_timelock',
    'reward',
    'rewards',
    'routing',
    'security_coinbase',
    'security_exchange',
    'state_channel_open',
    'state_channel_close',
    'token_burn_exchange_rate'
)
