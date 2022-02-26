"""helium-py pytest conftest.py file."""

import pytest

from helium_py.test.utils import get_test_users


@pytest.fixture
def users():
    """Fixture to provide user objects to test cases."""
    return get_test_users()
