"""Replace placeholder docstrings."""
import base64
import math
from dataclasses import dataclass
from typing import Optional

from helium_py import proto


@dataclass
class ChainVars:
    """Replace placeholder docstrings."""

    transaction_fee_multiplier: Optional[int]
    dc_payload_size: Optional[int]
    staking_fee_txn_assert_location_v1: Optional[int]
    staking_fee_txn_add_gateway_v1: Optional[int]


class Transaction:
    """Replace placeholder docstrings."""

    transaction_fee_multiplier: int = 0
    dc_payload_size: int = 24
    staking_fee_txn_assert_location_v1: int = 1
    staking_fee_txn_add_gateway_v1: int = 1

    def to_bytes_string(self):
        """Replace placeholder docstrings."""
        return base64.b64encode(self.serialize())

    def serialize(self) -> bytes:
        """Replace placeholder docstrings."""
        raise NotImplementedError()

    @classmethod
    def config(cls, chain_vars: Optional[ChainVars] = None):
        """Replace placeholder docstrings."""
        if chain_vars:
            if chain_vars.transaction_fee_multiplier is not None:
                cls.transaction_fee_multiplier = chain_vars.transaction_fee_multiplier

            if chain_vars.dc_payload_size is not None:
                cls.dc_payload_size = chain_vars.dc_payload_size

            if chain_vars.staking_fee_txn_assert_location_v1 is not None:
                cls.staking_fee_txn_assert_location_v1 = chain_vars.staking_fee_txn_assert_location_v1

            if chain_vars.staking_fee_txn_add_gateway_v1 is not None:
                cls.staking_fee_txn_add_gateway_v1 = chain_vars.staking_fee_txn_add_gateway_v1

        return ChainVars(
            transaction_fee_multiplier=cls.transaction_fee_multiplier,
            dc_payload_size=cls.dc_payload_size,
            staking_fee_txn_assert_location_v1=cls.staking_fee_txn_assert_location_v1,
            staking_fee_txn_add_gateway_v1=cls.staking_fee_txn_add_gateway_v1
        )

    @staticmethod
    def string_type(transaction_string: str) -> str:
        """Replace placeholder docstrings."""
        buf = base64.b64decode(transaction_string)
        decoded = proto.BlockchainTxn.FromString(buf)
        return list(decoded.to_dict().keys())[0]

    @classmethod
    def _calculate_fee(cls, payload) -> int:
        """Replace placeholder docstrings."""
        return math.ceil(len(str(payload)) / cls.dc_payload_size) * cls.transaction_fee_multiplier