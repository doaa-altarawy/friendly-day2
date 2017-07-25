"""
Testing for the math.py module
"""

import friendly_day2 as fc
import pytest

def test_add():
    assert fc.math.add(5, 3) == 8
    assert fc.math.add(-3, 5) == 2

def test_mult():
    assert fc.mult(5, 3) == 15
    assert fc.mult(-3, 5) == -15

testdata = [
    (2, 5, 10),
    (0, 0, 0),
    (-2, 6, -12)
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_mult2(a, b, expected):
    assert fc.mult(a, b) == expected
    assert fc.mult(b, a) == expected
