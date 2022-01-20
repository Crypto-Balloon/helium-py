"""Tests for Blocks client."""
from helium_py import Blocks


def test_blocks():
    """Initial integration tests for blocks.

    TODO: This are PoC tests and integration tests must be separated from unit tests.
    """
    some_height = 1181186
    some_hash = '8tMFcKgjx6AUiJ7T2B-by_-Hi7Mlu2hOnBsIyw2hyBw'
    blocks = Blocks()
    assert 'hash' in next(blocks.all())
    assert isinstance(blocks.get_height()['height'], int)
    assert 'avg' in blocks.get_stats()['last_day']
    assert 'height' in blocks.get_block_descriptor_for_height(some_height)
    assert 'height' in next(blocks.get_transactions_for_height(some_height))
    assert 'height' in blocks.get_block_descriptor_for_hash(some_hash)
    assert 'height' in next(blocks.get_transactions_for_hash(some_hash))
