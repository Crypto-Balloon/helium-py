"""Replace Placeholder Docstring."""
import base64
from dataclasses import dataclass
from typing import Optional

from helium_py import proto
from helium_py.crypto.address import Address


@dataclass
class Payment:
    """Replace Placeholder Docstring."""

    payee: Address
    amount: int
    memo: Optional[bytes]

    @classmethod
    def deserialize_payment_list(cls, protocol_buffer_payment_list):
        """Replace Placeholder Docstring."""
        payments = []
        for payment in protocol_buffer_payment_list:
            payee = Address.from_bin(payment.payee)
            if payee is not None:
                payments.append(cls(
                    payee=payee,
                    amount=payment.amount,
                    memo=base64.b64encode(bytes(payment.memo.to_bytes(64, 'little', signed=False)))))
        return payments

    @staticmethod
    def payment_list_to_proto(payment_list):
        """Replace Placeholder Docstring."""
        if not payment_list:
            return None
        return [
            proto.Payment(
                payee=payment.payee.bin,
                amount=payment.amount,
                memo=int.from_bytes(base64.b64decode(payment.memo), byteorder='little', signed=False))
            for payment in payment_list]
