# -*- coding: utf-8 -*-
from lock import RPiLock


def test_init():
    """Test instantiate a RPiLock object."""
    lock = RPiLock('localhost', 8000)
    assert False
