"""Payment helper class for use in building payloads for the Payment V2 transaction."""
from dataclasses import dataclass
from typing import List, Optional

from helium_py import proto
from helium_py.crypto.address import Address


@dataclass
class Payment:
    """Payment Class providing protocol buffer serialization and deserialization of Payments."""

    payee: Address
    amount: int
    memo: Optional[bytes]

    @staticmethod
    def deserialize_payment_list(protocol_buffer_payment_list: List[proto.Payment]) -> List['Payment']:
        """Deserialize a list of Protocol Buffer Payment objects into a list of this Payment Dataclass."""
        payments = []
        for payment in protocol_buffer_payment_list:
            payee = Address.from_bin(payment.payee)
            if payee is not None:
                payments.append(Payment(
                    payee=payee,
                    amount=payment.amount,
                    memo=payment.memo.to_bytes(
                        (payment.memo.bit_length() + 7) // 8, 'little', signed=False)
                    if payment.memo else None
                ))
        return payments

    @staticmethod
    def payment_list_to_proto(payment_list: List['Payment']) -> List[proto.Payment]:
        """Serialize a list of this Payment Dataclass into a list of Protocol Buffer Payment objects."""
        payments = []
        for payment in payment_list:
            if payment.memo and len(payment.memo) > 8:
                raise ValueError('Memo cannot contain more than 8 bytes.')
            kwargs = {}
            if payment.memo:
                kwargs['memo'] = int.from_bytes(payment.memo, byteorder='little', signed=False)
            payments.append(
                proto.Payment(
                    payee=payment.payee.bin,
                    amount=payment.amount,
                    **kwargs
                ))
        return payments
