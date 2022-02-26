"""Replace placeholder docstrings."""
from inspect import Parameter, signature
from typing import Optional

from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair


def transaction_class(cls):
    """Replace placeholder docstrings."""
    ANNOTATION_MAP = {
        'addresses': Optional[Address],
        'signatures': Optional[bytes],
        'integers': Optional[int],
    }

    class TransactionClass(cls):
        """Replace placeholder docstrings."""

        pass

    parameters = tuple()
    for field_type in cls.fields:
        parameters += tuple(
            Parameter(
                field,
                Parameter.KEYWORD_ONLY,
                annotation=ANNOTATION_MAP[field_type],
                default=None,
            )
            for field in cls.fields[field_type]
        )
    TransactionClass.__init__.__signature__ = signature(cls.__init__).replace(parameters=parameters)
    TransactionClass.sign.__signature__ = signature(cls.sign).replace(parameters=tuple(
        Parameter(
            field,
            Parameter.KEYWORD_ONLY,
            annotation=Optional[Keypair],
            default=None,
        )
        for field in cls.keypairs.keys()
    ))
    return TransactionClass
