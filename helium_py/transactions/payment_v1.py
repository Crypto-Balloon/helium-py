"""Replace Placeholder Docstring."""
import typing
from typing import Optional

from helium_py import proto
from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair
from helium_py.transactions.transaction import Transaction
from helium_py.transactions.utils import EMPTY_SIGNATURE


class PaymentV1(Transaction):
    """Replace Placeholder Docstring."""

    type: str = 'payment_v1'
    payer: Optional[Address]
    payee: Optional[Address]
    amount: Optional[int] = None
    fee: Optional[int] = None
    nonce: Optional[int] = None

    signature: Optional[bytes]

    def __init__(
            self,
            payer: Optional[Address],
            payee: Optional[Address],
            amount: Optional[int] = None,
            fee: Optional[int] = None,
            nonce: Optional[int] = None,
    ):
        """Replace Placeholder Docstring."""
        self.payer = payer
        self.payee = payee
        self.amount = amount
        self.fee = fee if fee is not None else self.calculate_fee()
        self.nonce = nonce

    @classmethod
    def deserialize(cls, serialized_transaction: bytes) -> 'PaymentV1':
        """Replace Placeholder Docstring."""
        payment_proto = proto.BlockchainTxn.FromString(serialized_transaction).payment

        payer = Address.from_bin(payment_proto.payer) if payment_proto.payer else None
        payee = Address.from_bin(payment_proto.payee) if payment_proto.payee else None
        amount = payment_proto.amount
        fee = payment_proto.fee
        nonce = payment_proto.nonce

        return cls(
            payer=payer,
            payee=payee,
            amount=amount,
            fee=fee,
            nonce=nonce,
        )

    @typing.no_type_check
    def to_proto(self, for_signing=False) -> proto.BlockchainTxn:
        """Replace Placeholder Docstring."""
        return proto.BlockchainTxn(payment=proto.BlockchainTxnPaymentV1(
            payer=self.payer.bin if self.payer else None,
            payee=self.payee.bin if self.payee else None,
            amount=self.amount if self.amount else None,
            fee=self.fee if self.fee and self.fee > 0 else None,
            nonce=self.nonce if self.nonce else None,
            signature=self.signature if self.signature and not for_signing else None
        ))

    def sign(
            self,
            payer: Optional[Keypair] = None,
    ) -> 'PaymentV1':
        """Replace Placeholder Docstring."""
        self.signature = payer.sign(self.serialize())
        return self

    def calculate_fee(self):
        """Replace Placeholder Docstring."""
        self.signature = EMPTY_SIGNATURE
        return super().calculate_fee()
