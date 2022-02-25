"""Replace placeholder docstrings."""
import base64
import math
from typing import Optional

from helium_py import proto


class Transaction:
    """Replace placeholder docstrings."""

    transaction_fee_multiplier: int = 0
    dc_payload_size: int = 24
    staking_fee_txn_assert_location_v1: int = 1
    staking_fee_txn_add_gateway_v1: int = 1

    def serialize(self) -> bytes:
        """Replace Placeholder Docstring."""
        return bytes(self.to_proto(for_signing=True))

    @classmethod
    def deserialize(cls, serialized_transaction: bytes):
        """Replace placeholder docstrings."""
        raise NotImplementedError()

    def to_b64(self) -> bytes:
        """Replace placeholder docstrings."""
        return base64.b64encode(self.serialize())

    @classmethod
    def from_b64(cls, serialized_transaction: bytes):
        """Replace placeholder docstrings."""
        return cls.deserialize(base64.b64decode(serialized_transaction))

    def to_proto(self, for_signing=False):
        """Replace placeholder docstrings."""
        raise NotImplementedError()

    @classmethod
    def config(
            cls,
            transaction_fee_multiplier: Optional[int] = None,
            dc_payload_size: Optional[int] = None,
            staking_fee_txn_assert_location_v1: Optional[int] = None,
            staking_fee_txn_add_gateway_v1: Optional[int] = None,
    ):
        """Replace placeholder docstrings."""
        if transaction_fee_multiplier is not None:
            cls.transaction_fee_multiplier = transaction_fee_multiplier

        if dc_payload_size is not None:
            cls.dc_payload_size = dc_payload_size

        if staking_fee_txn_assert_location_v1 is not None:
            cls.staking_fee_txn_assert_location_v1 = staking_fee_txn_assert_location_v1

        if staking_fee_txn_add_gateway_v1 is not None:
            cls.staking_fee_txn_add_gateway_v1 = staking_fee_txn_add_gateway_v1

        return dict(
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

    def calculate_fee(self) -> int:
        """Replace placeholder docstrings."""
        payload = self.serialize()
        return math.ceil(len(payload) / self.dc_payload_size) * self.transaction_fee_multiplier
