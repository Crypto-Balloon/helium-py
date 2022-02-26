"""Replace Placeholder Docstring."""
import typing
from typing import Optional

from helium_py import proto
from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair
from helium_py.transactions.transaction import Transaction
from helium_py.transactions.utils import EMPTY_SIGNATURE


class StakeValidatorV1(Transaction):
    """Replace Placeholder Docstring."""

    type: str = 'stake_validator_v1'
    address: Optional[Address]
    owner: Optional[Address]
    stake: Optional[int]
    fee: Optional[int] = None
    owner_signature: Optional[bytes]

    def __init__(
            self,
            address: Optional[Address],
            owner: Optional[Address],
            stake: Optional[int],
            fee: Optional[int] = None,
    ):
        """Replace Placeholder Docstring."""
        self.address = address
        self.owner = owner
        self.stake = stake
        self.fee = fee if fee is not None else self.calculate_fee()

    @classmethod
    def deserialize(cls, serialized_transaction: bytes) -> 'StakeValidatorV1':
        """Replace Placeholder Docstring."""
        validator_proto = proto.BlockchainTxn.FromString(serialized_transaction).stake_validator

        address = Address.from_bin(validator_proto.address) if validator_proto.address else None
        owner = Address.from_bin(validator_proto.owner) if validator_proto.owner else None
        stake = validator_proto.stake
        fee = validator_proto.fee

        return cls(
            address=address,
            owner=owner,
            stake=stake,
            fee=fee,
        )

    @typing.no_type_check
    def to_proto(self, for_signing=False) -> proto.BlockchainTxn:
        """Replace Placeholder Docstring."""
        return proto.BlockchainTxn(stake_validator=proto.BlockchainTxnStakeValidatorV1(
            address=self.address.bin if self.address else None,
            owner=self.owner.bin if self.owner else None,
            stake=self.stake if self.stake else None,
            fee=self.fee if self.fee and self.fee > 0 else None,
            owner_signature=self.owner_signature if self.owner_signature and not for_signing else None
        ))

    def sign(
            self,
            owner: Optional[Keypair] = None,
    ) -> 'StakeValidatorV1':
        """Replace Placeholder Docstring."""
        if not owner:
            raise ValueError('Owner argument required for signing')
        self.owner_signature = owner.sign(self.serialize())
        return self

    def calculate_fee(self):
        """Replace Placeholder Docstring."""
        self.owner_signature = EMPTY_SIGNATURE
        return super().calculate_fee()
