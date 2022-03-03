"""Decorators for use in transactions classes."""
from inspect import Parameter, signature
from typing import List, Optional

from helium_py.crypto.address import Address
from helium_py.crypto.keypair import Keypair
from helium_py.transactions.payment import Payment


def transaction_class(cls):
    """Decorate transaction classes to dynamically generate method signatures."""
    ANNOTATION_MAP = {
        'addresses': Optional[Address],
        'signatures': Optional[bytes],
        'integers': Optional[int],
        'strings': Optional[str],
        'payment_lists': Optional[List[Payment]],
    }

    class TransactionClass(cls):
        """Class to be returned post-modification."""

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
    init_sig = signature(cls.__init__)
    init_sig.replace(return_annotation=cls)
    TransactionClass.__init__.__signature__ = init_sig.replace(parameters=parameters)
    sign_sig = signature(cls.sign)
    sign_sig.replace(return_annotation=cls)
    TransactionClass.sign.__signature__ = sign_sig.replace(parameters=tuple(
        Parameter(
            field,
            Parameter.KEYWORD_ONLY,
            annotation=Optional[Keypair],
            default=None,
        )
        for field in cls.keypairs.keys()
    ))
    return TransactionClass
