"""Replace Placeholder Docstring."""
import typing
from typing import Optional

from helium_py import proto
from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair
from helium_py.transactions.transaction import Transaction
from helium_py.transactions.utils import EMPTY_SIGNATURE


class AssertLocationV2(Transaction):
    """Replace Placeholder Docstring."""

    type: str = 'assert_location_v2'
    owner: Optional[Address]
    gateway: Optional[Address]
    payer: Optional[Address]
    location: Optional[str]
    nonce: Optional[int]
    gain: Optional[int]
    elevation: Optional[int]
    fee: Optional[int] = None
    staking_fee: Optional[int] = None
    owner_signature: Optional[bytes]
    payer_signature: Optional[bytes]

    def __init__(
            self,
            owner: Optional[Address] = None,
            gateway: Optional[Address] = None,
            payer: Optional[Address] = None,
            location: Optional[str] = None,
            nonce: Optional[int] = None,
            gain: Optional[int] = None,
            elevation: Optional[int] = None,
            fee: Optional[int] = None,
            staking_fee: Optional[int] = None,
            owner_signature: Optional[bytes] = None,
            payer_signature: Optional[bytes] = None,
    ):
        """Replace Placeholder Docstring."""
        self.owner = owner
        self.gateway = gateway
        self.payer = payer
        self.location = location
        self.nonce = nonce
        self.gain = gain
        self.elevation = elevation
        self.fee = fee if fee is not None else self.calculate_fee()
        self.staking_fee = staking_fee if staking_fee is not None else self.staking_fee_txn_assert_location_v1
        self.owner_signature = owner_signature
        self.payer_signature = payer_signature

    @classmethod
    def deserialize(cls, serialized_transaction: bytes) -> 'AssertLocationV2':
        """Replace Placeholder Docstring."""
        assert_location_proto = proto.BlockchainTxn.FromString(serialized_transaction).assert_location_v2

        owner = Address.from_bin(assert_location_proto.owner) if assert_location_proto.owner else None
        gateway = Address.from_bin(assert_location_proto.gateway) if assert_location_proto.gateway else None
        payer = Address.from_bin(assert_location_proto.payer) if assert_location_proto.payer else None
        location = assert_location_proto.location if assert_location_proto.location else None
        nonce = assert_location_proto.nonce if assert_location_proto.nonce else None
        gain = assert_location_proto.gain
        elevation = assert_location_proto.elevation if assert_location_proto.elevation else None
        fee = assert_location_proto.fee
        staking_fee = assert_location_proto.staking_fee
        owner_signature = assert_location_proto.owner_signature or None
        payer_signature = assert_location_proto.payer_signature or None

        return cls(
            owner=owner,
            gateway=gateway,
            payer=payer,
            location=location,
            nonce=nonce,
            gain=gain,
            elevation=elevation,
            fee=fee,
            staking_fee=staking_fee,
            owner_signature=owner_signature,
            payer_signature=payer_signature,
        )

    @typing.no_type_check
    def to_proto(self, for_signing=False) -> proto.BlockchainTxn:
        """Replace Placeholder Docstring."""
        return proto.BlockchainTxn(assert_location_v2=proto.BlockchainTxnAssertLocationV2(
            owner=self.owner.bin if self.owner else None,
            gateway=self.gateway.bin if self.gateway else None,
            payer=self.payer.bin if self.payer else None,
            location=self.location if self.location else None,
            nonce=self.nonce if self.nonce else None,
            gain=self.gain if self.gain else None,
            elevation=self.elevation if self.elevation else None,
            fee=self.fee if self.fee else None,
            staking_fee=self.staking_fee if self.staking_fee else None,
            owner_signature=self.owner_signature if self.owner_signature and for_signing else None,
            payer_signature=self.payer_signature if self.payer and self.payer_signature and for_signing else None,
        ))

    def sign(
            self,
            owner: Optional[Keypair] = None,
            payer: Optional[Keypair] = None,
    ) -> 'AssertLocationV2':
        """Replace Placeholder Docstring."""
        assert_location_proto = self.to_proto(for_signing=True)
        serialized = bytes(assert_location_proto)
        if owner:
            self.owner_signature = owner.sign(serialized)
        if payer:
            self.payer_signature = payer.sign(serialized)
        return self

    def calculate_fee(self):
        """Replace Placeholder Docstring."""
        self.owner_signature = EMPTY_SIGNATURE
        if self.payer:
            self.payer_signature = EMPTY_SIGNATURE
        return super().calculate_fee()
