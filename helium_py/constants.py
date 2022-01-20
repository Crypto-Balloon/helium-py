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
VALID_HOTSPOT_MODES = ('full', 'dataonly', 'light')
VALID_TRANSACTION_TYPES = (
    'add_gateway',
    'assert_location',
    'coinbase',
    'create_htlc',
    'gen_gateway',
    'consensus_group',
    'oui',
    'payment',
    'poc_receipts',
    'poc_request',
    'redeem_htlc',
    'security_coinbase',
    'routing',
    'security_exchange',
    'vars',
    'rewards',
    'token_burn',
    'dc_coinbase',
    'token_burn_exchange_rate',
    'bundle',
    'state_channel_open',
    'update_gateway_oui',
    'state_channel_close',
    'payment_v2',
    'price_oracle_submission',
    'gen_price_oracle',
    'transfer_hotspot',
    'gen_validator',
    'stake_validator',
    'transfer_val_stake',
    'unstake_validator',
    'val_heartbeat',
    'consensus_group_failure',
    'rewards_v2',
    'assert_location_v2',
    'transfer_hotspot_v2',
)
