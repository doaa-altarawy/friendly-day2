"""
Testing for the math.py module
"""

import friendly_day2 as fc
import pytest

def test_add():
    assert fc.math.add(5, 3) == 8
    assert fc.math.add(-3, 5) == 2
