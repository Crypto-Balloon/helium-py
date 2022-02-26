"""Replace Placeholder Docstring."""
import base64
import typing
from dataclasses import dataclass
from typing import Optional

from helium_py import proto
from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair
from helium_py.transactions.transaction import Transaction
from helium_py.transactions.utils import EMPTY_SIGNATURE


class PaymentV2(Transaction):
    """Replace Placeholder Docstring."""

    @dataclass
    class Payment:
        """Replace Placeholder Docstring."""

        payee: Address
        amount: int
        memo: Optional[bytes]

    type: str = 'payment_v2'
    payer: Optional[Address]
    payments: Optional[typing.List[Payment]]
    fee: Optional[int] = None
    nonce: Optional[int] = None
    signature: Optional[bytes]

    def __init__(
            self,
            payer: Optional[Address],
            payments: Optional[typing.List[Payment]],
            fee: Optional[int] = None,
            nonce: Optional[int] = None,
            signature: Optional[bytes] = None,
    ):
        """Replace Placeholder Docstring."""
        self.payer = payer
        self.payments = payments if payments else []
        self.nonce = nonce
        self.fee = fee if fee is not None else self.calculate_fee()
        self.signature = signature

    @classmethod
    def deserialize(cls, serialized_transaction: bytes) -> 'PaymentV2':
        """Replace Placeholder Docstring."""
        payment_proto = proto.BlockchainTxn.FromString(serialized_transaction).payment_v2

        payer = Address.from_bin(payment_proto.payer) if payment_proto.payer else None
        payments = [
            cls.Payment(
                payee=Address.from_bin(payment.payee),
                amount=payment.amount,
                memo=base64.b64encode(bytes(payment.memo.to_bytes(64, 'little', signed=False))))
            for payment in payment_proto.payments]
        fee = payment_proto.fee
        nonce = payment_proto.nonce

        return cls(
            payer=payer,
            payments=payments,
            fee=fee,
            nonce=nonce,
        )

    @typing.no_type_check
    def to_proto(self, for_signing=False) -> proto.BlockchainTxn:
        """Replace Placeholder Docstring."""
        payments = [
            proto.Payment(
                payee=payment.payee.bin,
                amount=payment.amount,
                memo=int.from_bytes(base64.b64decode(payment.memo), byteorder='little', signed=False))
            for payment in self.payments]

        return proto.BlockchainTxn(payment_v2=proto.BlockchainTxnPaymentV2(
            payer=self.payer.bin if self.payer else None,
            payments=payments,
            fee=self.fee if self.fee and self.fee > 0 else None,
            nonce=self.nonce if self.nonce else None,
            signature=self.signature if self.signature and not for_signing else None
        ))

    def sign(
            self,
            payer: Optional[Keypair] = None,
    ) -> 'PaymentV2':
        """Replace Placeholder Docstring."""
        if not payer:
            raise ValueError('Payer argument required for signing')
        self.signature = payer.sign(self.serialize())
        return self

    def calculate_fee(self):
        """Replace Placeholder Docstring."""
        self.signature = EMPTY_SIGNATURE
        return super().calculate_fee()
