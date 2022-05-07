"""Base Transaction Class."""
import base64
import copy
import math
import typing

import betterproto

from helium_py import proto
from helium_py.api import ChainVariables
from helium_py.crypto.address import Address
from helium_py.crypto.utils import EMPTY_SIGNATURE
from helium_py.transactions.payment import Payment


class Transaction:
    """Base Transaction Class."""

    type: str
    fields: dict
    defaults: dict
    keypairs: dict
    proto_model_class: typing.Type[betterproto.Message]
    proto_txn_field: str
    payment_class: typing.Type[Payment] = Payment

    # Configuration
    transaction_fee_multiplier: int = 5000
    dc_payload_size: int = 24
    staking_fee_txn_assert_location_v1: int = 1000000
    staking_fee_txn_add_gateway_v1: int = 4000000

    def __init__(self, **kwargs):
        """Initialize a new Transaction instance."""
        self.orig_kwargs = copy.deepcopy(kwargs)
        for field_type in self.fields:
            for field_name in self.fields[field_type]:
                value = kwargs.get(field_name)
                setattr(self, field_name, value)
        for field_name in self.defaults:
            if field_name not in kwargs:
                setattr(self, field_name, getattr(self, self.defaults[field_name]))

    def serialize(self) -> bytes:
        """Return the bytes representation of a Transaction instance."""
        return bytes(self.to_proto())

    def to_b64(self) -> bytes:
        """Return base64 encoded byte value for serialized protocol buffer data."""
        return base64.b64encode(self.serialize())

    @classmethod
    def from_b64(cls, serialized_transaction: bytes) -> 'Transaction':
        """Return a Transaction instance from the provided base64 bytes."""
        return cls.deserialize(base64.b64decode(serialized_transaction))

    @classmethod
    def fetch_config(cls):
        """Update chain variables via API and return configuration values for chain variables."""
        chain_vars = ChainVariables().get_all()
        return cls.config(
            transaction_fee_multiplier=chain_vars['txn_fee_multiplier'],
            dc_payload_size=chain_vars['dc_payload_size'],
            staking_fee_txn_assert_location_v1=chain_vars['staking_fee_txn_assert_location_v1'],
            staking_fee_txn_add_gateway_v1=chain_vars['staking_fee_txn_add_gateway_v1'],
        )

    @classmethod
    def config(
            cls,
            transaction_fee_multiplier: typing.Optional[int] = None,
            dc_payload_size: typing.Optional[int] = None,
            staking_fee_txn_assert_location_v1: typing.Optional[int] = None,
            staking_fee_txn_add_gateway_v1: typing.Optional[int] = None,
    ) -> typing.Dict[str, int]:
        """Optionally update and return configuration values for chain variables."""
        if transaction_fee_multiplier is not None:
            cls.transaction_fee_multiplier = transaction_fee_multiplier

        if dc_payload_size is not None:
            cls.dc_payload_size = dc_payload_size

        if staking_fee_txn_assert_location_v1 is not None:
            cls.staking_fee_txn_assert_location_v1 = staking_fee_txn_assert_location_v1

        if staking_fee_txn_add_gateway_v1 is not None:
            cls.staking_fee_txn_add_gateway_v1 = staking_fee_txn_add_gateway_v1

        return {
            'transaction_fee_multiplier': cls.transaction_fee_multiplier,
            'dc_payload_size': cls.dc_payload_size,
            'staking_fee_txn_assert_location_v1': cls.staking_fee_txn_assert_location_v1,
            'staking_fee_txn_add_gateway_v1': cls.staking_fee_txn_add_gateway_v1
        }

    @staticmethod
    def string_type(transaction_string: bytes) -> str:
        """Return the protocol buffer string type of the Transaction instance from bytes repr."""
        buf = base64.b64decode(transaction_string)
        decoded = proto.BlockchainTxn.FromString(buf)
        return list(decoded.to_dict().keys())[0]

    @staticmethod
    def getattr_none(obj: typing.Any, attr: str) -> typing.Any:
        """getattr() but return `None` for any attr that is empty bytes."""
        value = getattr(obj, attr)
        return value if value != b'' else None

    @classmethod
    def get_deserialized_addresses(cls, proto_model: betterproto.Message) -> typing.Dict[str, typing.Optional[Address]]:
        """Return all deserialized Address instances for Transaction instances address fields."""
        return {
            key: Address.from_bin(getattr(proto_model, key)) if getattr(proto_model, key) else None
            for key in cls.fields.get('addresses', [])
        }

    @classmethod
    def _get_deserialized_memo(cls, proto_model: betterproto.Message) -> bytes:
        """Return the memo bytes from the int64 memo value if exists."""
        memo = cls.getattr_none(proto_model, 'memo')
        return memo.to_bytes((memo.bit_length() + 7) // 8, 'little', signed=False) if memo else None

    @classmethod
    def _get_deserialized_plain(
            cls,
            proto_model: betterproto.Message,
            attr_names: typing.List[str]
    ) -> typing.Dict[str, typing.Any]:
        """Return the deserialized values for the given attribute names."""
        return {
            key: cls._get_deserialized_memo(proto_model)
            if key == 'memo' else cls.getattr_none(proto_model, key)
            for key in attr_names
        }

    @classmethod
    def get_deserialized_signatures(cls, proto_model: betterproto.Message) -> typing.Dict[str, bytes]:
        """Return deserialized signatures."""
        return cls._get_deserialized_plain(proto_model, cls.fields.get('signatures', []))

    @classmethod
    def get_deserialized_integers(cls, proto_model: betterproto.Message) -> typing.Dict[str, int]:
        """Return deserialized integers."""
        return cls._get_deserialized_plain(proto_model, cls.fields.get('integers', []))

    @classmethod
    def get_deserialized_strings(cls, proto_model: betterproto.Message) -> typing.Dict[str, str]:
        """Return deserialized strings."""
        return cls._get_deserialized_plain(proto_model, cls.fields.get('strings', []))

    @classmethod
    def get_deserialized_payment_lists(cls, proto_model: betterproto.Message) -> typing.Dict[str, typing.List[Payment]]:
        """Return deserialized payment lists."""
        return {
            key: cls.payment_class.deserialize_payment_list(getattr(proto_model, key))
            for key in cls.fields.get('payment_lists', [])
        }

    def get_addresses(self):
        """Return addresses for protocol buffer initialization."""
        return {key: getattr(getattr(self, key), 'bin', None) for key in self.fields.get('addresses', [])}

    def get_signatures(self, for_signing: bool = False):
        """Return signatures for protocol buffer initialization."""
        return {
            key: None if for_signing else getattr(self, key) or None
            for key in self.fields.get('signatures', [])
        }

    def _get_memo(self):
        """Return memo value for protocol buffer initialization."""
        memo = getattr(self, 'memo', None)
        if memo and len(memo) > 8:
            raise ValueError('Memo cannot contain more than 8 bytes.')
        return int.from_bytes(memo, 'little', signed=False) if memo else None

    def get_integers(self):
        """Return integers for protocol buffer initialization."""
        return {
            key: self._get_memo()
            if key == 'memo' else getattr(self, key, None)
            for key in self.fields.get('integers', [])
        }

    def get_strings(self):
        """Return strings for protocol buffer initialization."""
        return {key: getattr(self, key, None) for key in self.fields.get('strings', [])}

    def get_payment_lists(self):
        """Return payment lists for protocol buffer initialization."""
        return {
            key: self.payment_class.payment_list_to_proto(getattr(self, key) or None)
            for key in self.fields.get('payment_lists', [])
        }

    def orig_kwarg_gt0_or_none(self, key) -> typing.Optional[int]:
        """Return the original kwarg value if greater than zero and not None."""
        if (key not in self.orig_kwargs or (
                self.orig_kwargs[key] is not None and
                self.orig_kwargs[key] <= 0)):
            return None
        return self.orig_kwargs[key]

    def get_calculate_fee_kwargs(self) -> dict:
        """Return kwargs to use for calculating fee."""
        fee_kwargs = copy.deepcopy(self.orig_kwargs)
        fee_kwargs.update({
            key: EMPTY_SIGNATURE for key in self.get_signatures()
        })
        fee_kwargs['fee'] = self.orig_kwarg_gt0_or_none('fee')
        return fee_kwargs

    @property
    def calculated_fee(self) -> int:
        """Property for calculated fee for Transaction in current state."""
        return self.calculate_fee(**self.get_calculate_fee_kwargs())

    @classmethod
    def calculate_fee(cls, **init_kwargs: dict) -> int:
        """Return fee for transaction based on payload size and chain variables."""
        payload = cls(**init_kwargs).serialize()
        return math.ceil(len(payload) / cls.dc_payload_size) * cls.transaction_fee_multiplier

    @classmethod
    def deserialize(cls, serialized_transaction: bytes) -> 'Transaction':
        """Return a Transaction instance from the provided serialized transaction bytes."""
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
    def to_proto(self, for_signing: bool = False) -> betterproto.Message:
        """Return a protocol buffer BlockchainTxn instance from this Transaction instance."""
        proto_model_kwargs = {
            **self.get_addresses(),
            **self.get_integers(),
            **self.get_strings(),
            **self.get_signatures(for_signing),
            **self.get_payment_lists(),
        }
        transaction_proto_model = self.proto_model_class(**proto_model_kwargs)

        if for_signing:
            return transaction_proto_model

        proto_txn_kwargs = {
            self.proto_txn_field: transaction_proto_model
        }

        return proto.BlockchainTxn(**proto_txn_kwargs)

    def sign(self, **kwargs) -> 'Transaction':
        """Sign a Transaction instance using available keypairs."""
        serialized = bytes(self.to_proto(for_signing=True))
        for key, attr_name in self.keypairs.items():
            keypair = kwargs.get(key)
            if keypair:
                setattr(self, attr_name, keypair.sign(serialized))
        return self
