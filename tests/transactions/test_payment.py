"""Tests for PaymentV1."""
from helium_py.transactions.payment import Payment


def test_payment_list_to_proto_raises_on_memo_too_long(users):
    """Test create transaction."""
    try:
        Payment.payment_list_to_proto(
            [
                Payment(
                    payee=users.bob.keypair.address,
                    amount=10,
                    memo=b'1234',
                ),
                Payment(
                    payee=users.bob.keypair.address,
                    amount=10,
                    memo=b'123456789',
                )]
        )
    except ValueError:
        pass
    else:
        raise Exception('Test expected ValueError on memo too long.')
