"""Tests for OUIs client."""

import logging

import pytest

from helium_py.api import OUIs

logger = logging.getLogger(__name__)


@pytest.mark.integration
def test_ouis():
    """Initial integration tests for ouis.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    ouis = OUIs()

    assert 'oui' in next(ouis.all())

    assert 'oui' in ouis.get_last()

    assert 'oui' in ouis.get_oui(1)

    assert 'count' in ouis.get_stats()
