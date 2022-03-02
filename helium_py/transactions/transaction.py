"""Replace placeholder docstrings."""
import base64
import copy
import math
import typing

import betterproto

from helium_py import proto
from helium_py.crypto.address import Address
from helium_py.transactions.payment import Payment
from helium_py.transactions.utils import EMPTY_SIGNATURE


class Transaction:
    """Replace placeholder docstrings."""

    type: str
    proto_model_class: typing.Type[betterproto.Message]
    proto_txn_field: str
    payment_class: typing.Type = Payment

    # Configuration
    transaction_fee_multiplier: int = 0
    dc_payload_size: int = 24
    staking_fee_txn_assert_location_v1: int = 1
    staking_fee_txn_add_gateway_v1: int = 1

    def __init__(self, **kwargs):
        """Replace Placeholder Docstring."""
        self.orig_kwargs = copy.deepcopy(kwargs)
        for field_type in self.fields:
            for field_name in self.fields[field_type]:
                value = kwargs.get(field_name)
                setattr(self, field_name, value)
        for field_name in self.defaults:
            if field_name not in kwargs:
                setattr(self, field_name, getattr(self, self.defaults[field_name]))

    def serialize(self) -> bytes:
        """Replace Placeholder Docstring."""
        breakpoint()
        return bytes(self.to_proto())

    def to_b64(self) -> bytes:
        """Replace placeholder docstrings."""
        return base64.b64encode(self.serialize())

    @classmethod
    def from_b64(cls, serialized_transaction: bytes):
        """Replace placeholder docstrings."""
        return cls.deserialize(base64.b64decode(serialized_transaction))

    @classmethod
    def config(
            cls,
            transaction_fee_multiplier: typing.Optional[int] = None,
            dc_payload_size: typing.Optional[int] = None,
            staking_fee_txn_assert_location_v1: typing.Optional[int] = None,
            staking_fee_txn_add_gateway_v1: typing.Optional[int] = None,
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

    @classmethod
    def get_deserialized_addresses(cls, proto_model):
        """Replace placeholder docstrings."""
        return {
            key: Address.from_bin(getattr(proto_model, key))
            for key in cls.fields.get('addresses', [])
        }

    @staticmethod
    def getattr_none(obj, attr):
        """getattr() but return `None` for any attr that is empty bytes."""
        value = getattr(obj, attr)
        return value if value != b'' else None

    @classmethod
    def _get_deserialized_memo(cls, proto_model):
        memo = cls.getattr_none(proto_model, 'memo')
        return memo.to_bytes(64, 'little', signed=False) if memo else None

    @classmethod
    def _get_deserialized_plain(cls, proto_model, attr_names):
        """Replace placeholder docstrings."""
        return {
            key: cls._get_deserialized_memo(proto_model)
            if key == 'memo' else cls.getattr_none(proto_model, key)
            for key in attr_names
        }

    @classmethod
    def get_deserialized_signatures(cls, proto_model):
        """Replace placeholder docstrings."""
        return cls._get_deserialized_plain(proto_model, cls.fields.get('signatures', []))

    @classmethod
    def get_deserialized_integers(cls, proto_model):
        """Replace placeholder docstrings."""
        return cls._get_deserialized_plain(proto_model, cls.fields.get('integers', []))

    @classmethod
    def get_deserialized_strings(cls, proto_model):
        """Replace placeholder docstrings."""
        return cls._get_deserialized_plain(proto_model, cls.fields.get('strings', []))

    @classmethod
    def get_deserialized_payment_lists(cls, proto_model):
        """Replace placeholder docstrings."""
        return {
            key: cls.payment_class.deserialize_payment_list(getattr(proto_model, key))
            for key in cls.fields.get('payment_lists', [])
        }

    def get_addresses(self):
        """Replace placeholder docstrings."""
        return {key: getattr(getattr(self, key), 'bin', None) for key in self.fields.get('addresses', [])}

    def get_signatures(self, for_signing=False):
        """Replace placeholder docstrings."""
        return {
            key: None if for_signing else getattr(self, key) or None
            for key in self.fields.get('signatures', [])
        }

    def get_integers(self):
        """Replace placeholder docstrings."""
        return {key: getattr(self, key, None) for key in self.fields.get('integers', [])}

    def _get_memo(self):
        memo = getattr(self, 'memo', None)
        breakpoint()
        return int.from_bytes(base64.b64decode(memo), byteorder='little', signed=False) if memo else None

    def get_strings(self):
        """Replace placeholder docstrings."""
        return {
            key: self._get_memo()
            if key == 'memo' else getattr(self, key, None)
            for key in self.fields.get('strings', [])
        }

    def get_payment_lists(self):
        """Replace placeholder docstrings."""
        return {
            key: self.payment_class.payment_list_to_proto(getattr(self, key) or None)
            for key in self.fields.get('payment_lists', [])
        }

    def orig_kwarg_gt0_or_none(self, key):
        """Replace Placeholder Docstring."""
        if (key not in self.orig_kwargs or (
                self.orig_kwargs[key] is not None and
                self.orig_kwargs[key] <= 0)):
            return None
        return self.orig_kwargs[key]

    def get_calculate_fee_kwargs(self):
        """Replace placeholder docstrings."""
        fee_kwargs = copy.deepcopy(self.orig_kwargs)
        fee_kwargs.update({
            key: EMPTY_SIGNATURE for key in self.get_signatures()
        })
        fee_kwargs['fee'] = self.orig_kwarg_gt0_or_none('fee')
        return fee_kwargs

    @property
    def calculated_fee(self):
        """Replace placeholder docstrings."""
        return self.calculate_fee(**self.get_calculate_fee_kwargs())

    @classmethod
    def calculate_fee(cls, **init_kwargs) -> int:
        """Replace placeholder docstrings."""
        payload = cls(**init_kwargs).serialize()
        return math.ceil(len(payload) / cls.dc_payload_size) * cls.transaction_fee_multiplier

    @classmethod
    def deserialize(cls, serialized_transaction: bytes):
        """Replace Placeholder Docstring."""
        proto_model = getattr(
            proto.BlockchainTxn.FromString(serialized_transaction), cls.proto_txn_field,
        )

        return cls(
            **cls.get_deserialized_addresses(proto_model),
            **cls.get_deserialized_signatures(proto_model),
            **cls.get_deserialized_integers(proto_model),
            **cls.get_deserialized_strings(proto_model),
            **cls.get_deserialized_payment_lists(proto_model)
        )

    @typing.no_type_check
    def to_proto(self, for_signing=False) -> proto.BlockchainTxn:
        """Replace Placeholder Docstring."""
        proto_model_kwargs = {
            **self.get_addresses(),
            **self.get_integers(),
            **self.get_strings(),
            **self.get_signatures(for_signing),
            **self.get_payment_lists(),
        }
        proto_txn_kwargs = {
            self.proto_txn_field: self.proto_model_class(**proto_model_kwargs)
        }

        return proto.BlockchainTxn(**proto_txn_kwargs)

    def sign(self, **kwargs):
        """Replace Placeholder Docstring."""
        serialized = bytes(self.to_proto(for_signing=True))
        for key, attr_name in self.keypairs.items():
            keypair = kwargs.get(key)
            if keypair:
                setattr(self, attr_name, keypair.sign(serialized))
        return self
