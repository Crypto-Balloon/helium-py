"""Replace Placeholder Docstring."""
import typing
from typing import Optional

from helium_py import proto
from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair
from helium_py.transactions.transaction import Transaction
from helium_py.transactions.utils import EMPTY_SIGNATURE


class AddGatewayV1(Transaction):
    """Replace Placeholder Docstring."""

    type: str = 'add_gateway_v1'
    owner: Optional[Address]
    gateway: Optional[Address]
    payer: Optional[Address]
    owner_signature: Optional[bytes]
    gateway_signature: Optional[bytes]
    payer_signature: Optional[bytes]
    fee: Optional[int] = None
    staking_fee: Optional[int] = None

    def __init__(
            self,
            owner: Optional[Address] = None,
            gateway: Optional[Address] = None,
            payer: Optional[Address] = None,
            owner_signature: Optional[bytes] = None,
            gateway_signature: Optional[bytes] = None,
            payer_signature: Optional[bytes] = None,
            staking_fee: Optional[int] = None,
            fee: Optional[int] = None,
    ):
        """Replace Placeholder Docstring."""
        self.owner = owner
        self.gateway = gateway
        self.payer = payer
        self.owner_signature = owner_signature
        self.gateway_signature = gateway_signature
        self.payer_signature = payer_signature
        self.fee = fee if fee is not None else self.calculate_fee()
        self.staking_fee = staking_fee if staking_fee is not None else self.staking_fee_txn_add_gateway_v1

    @classmethod
    def deserialize(cls, serialized_transaction: bytes) -> 'AddGatewayV1':
        """Replace Placeholder Docstring."""
        add_gateway_proto = proto.BlockchainTxn.FromString(serialized_transaction).add_gateway

        owner = Address.from_bin(add_gateway_proto.owner) if add_gateway_proto.owner else None
        gateway = Address.from_bin(add_gateway_proto.gateway) if add_gateway_proto.gateway else None
        payer = Address.from_bin(add_gateway_proto.payer) if add_gateway_proto.payer else None

        owner_signature = add_gateway_proto.owner_signature or None
        gateway_signature = add_gateway_proto.gateway_signature or None
        payer_signature = add_gateway_proto.payer_signature or None

        fee = add_gateway_proto.fee
        staking_fee = add_gateway_proto.staking_fee

        return cls(
            owner=owner,
            gateway=gateway,
            payer=payer,
            fee=fee,
            staking_fee=staking_fee,
            owner_signature=owner_signature,
            gateway_signature=gateway_signature,
            payer_signature=payer_signature,
        )

    @typing.no_type_check
    def to_proto(self, for_signing=False) -> proto.BlockchainTxn:
        """Replace Placeholder Docstring."""
        return proto.BlockchainTxn(add_gateway=proto.BlockchainTxnAddGatewayV1(
            owner=self.owner.bin if self.owner else None,
            gateway=self.gateway.bin if self.gateway else None,
            payer=self.payer.bin if self.payer else None,
            owner_signature=self.owner_signature if self.owner_signature and for_signing else None,
            gateway_signature=self.gateway_signature if self.gateway_signature and for_signing else None,
            payer_signature=self.payer_signature if self.payer and self.payer_signature and for_signing else None,
            staking_fee=self.staking_fee if self.staking_fee else None,
            fee=self.fee if self.fee else None,
        ))

    def sign(
            self,
            owner: Optional[Keypair] = None,
            gateway: Optional[Keypair] = None,
            payer: Optional[Keypair] = None,
    ) -> 'AddGatewayV1':
        """Replace Placeholder Docstring."""
        add_gateway_proto = self.to_proto(for_signing=True)
        serialized = bytes(add_gateway_proto)
        if owner:
            self.owner_signature = owner.sign(serialized)
        if gateway:
            self.gateway_signature = gateway.sign(serialized)
        if payer:
            self.payer_signature = payer.sign(serialized)
        return self

    def calculate_fee(self):
        """Replace Placeholder Docstring."""
        self.owner_signature = EMPTY_SIGNATURE
        self.gateway_signature = EMPTY_SIGNATURE
        if self.payer:
            self.payer_signature = EMPTY_SIGNATURE
        return super().calculate_fee()
