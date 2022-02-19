from dataclasses import dataclass
from typing import Optional

from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair

from helium_py import proto
from helium_py.transactions.transaction import Transaction
from helium_py.transactions.utils import EMPTY_SIGNATURE


@dataclass
class AddGatewayOptions:
    owner: Optional[Address] = None
    gateway: Optional[Address] = None
    payer: Optional[Address] = None
    fee: Optional[int] = None
    staking_fee: Optional[int] = None
    owner_signature: Optional[bytes] = None
    gateway_signature: Optional[bytes] = None
    payer_signature: Optional[bytes] = None


@dataclass
class SignOptions:
    owner: Optional[Keypair]
    gateway: Optional[Keypair]
    payer: Optional[Keypair]


class AddGatewayV1(Transaction):
    type: str = 'add_gateway_v1'

    owner: Optional[Address]
    gateway: Optional[Address]
    payer: Optional[Address]
    owner_signature: Optional[bytes]
    gateway_signature: Optional[bytes]
    payer_signature: Optional[bytes]
    staking_fee: Optional[int]
    fee: Optional[int]

    def __init__(self, options: AddGatewayOptions):
        self.owner = options.owner
        self.gateway = options.gateway
        self.payer = options.payer
        self.staking_fee = 0
        self.fee = 0

        if options.fee is not None:
            self.fee = options.fee
        else:
            self.fee = self.calculate_fee()

        if self.staking_fee is not None:
            self.staking_fee = options.staking_fee
        else:
            self.staking_fee = Transaction.staking_fee_txn_add_gateway_v1

        if options.owner_signature is not None:
            self.owner_signature = options.owner_signature
        if options.gateway_signature is not None:
            self.gateway_signature = options.gateway_signature
        if options.payer_signature is not None:
            self.payer_signature = options.payer_signature

    def serialize(self) -> bytes:
        return self.to_proto().SerializeToString()

    @classmethod
    def from_string(cls, serialized_transaction: bytes) -> 'AddGatewayV1':
        add_gateway_proto = proto.BlockchainTxn.FromString(serialized_transaction)

        owner = Address.from_bin(add_gateway_proto.owner) if add_gateway_proto.owner else None
        gateway = Address.from_bin(add_gateway_proto.gateway) if add_gateway_proto.gateway else None
        payer = Address.from_bin(add_gateway_proto.payer) if add_gateway_proto.payer else None

        owner_signature = add_gateway_proto.owner_signature or None
        gateway_signature = add_gateway_proto.gateway_signature or None
        payer_signature = add_gateway_proto.payer_signature or None

        fee = add_gateway_proto.fee
        staking_fee = add_gateway_proto.fee

        return cls(AddGatewayOptions(
            owner=owner,
            gateway=gateway,
            payer=payer,
            fee=fee,
            staking_fee=staking_fee,
            owner_signature=owner_signature,
            gateway_signature=gateway_signature,
            payer_signature=payer_signature,
        ))

    def sign(self, opts: SignOptions) -> 'AddGatewayV1':
        add_gateway_proto = self.to_proto(for_signing=True)
        serialized = add_gateway_proto.SerializeToString()
        if opts.owner:
            self.owner_signature = opts.owner.sign(serialized)
        if opts.gateway:
            self.gateway_signature = opts.gateway.sign(serialized)
        if opts.payer:
            self.payer_signature = opts.payer.sign(serialized)
        return self

    def to_proto(self, for_signing=False) -> proto.BlockchainTxnAddGatewayV1:
        return proto.BlockchainTxnAddGatewayV1().from_dict({
            'owner': self.owner.bin if self.owner else None,
            'gateway': self.gateway.bin if self.gateway else None,
            'payer': self.payer.bin if self.payer else None,
            'owner_signature': self.owner_signature if self.owner_signature and for_signing else None,
            'gateway_signature': self.gateway_signature if self.gateway_signature and for_signing else None,
            'payer_signature': self.payer_signature if self.payer_signature and for_signing else None,
            'staking_fee': self.staking_fee if self.staking_fee else None,
            'free': self.fee if self.fee else None,
        })

    def calculate_fee(self):
        self.owner_signature = EMPTY_SIGNATURE
        self.gateway_signature = EMPTY_SIGNATURE
        if self.payer:
            self.payer_signature = EMPTY_SIGNATURE
        payload = self.serialize()
        return Transaction.calculate_fee(payload)
