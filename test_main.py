"""
Test goes here

"""

from mylib.calculator import add
from mylib.calculator import subtract
from mylib.calculator import multiply
from mylib.calculator import divide


def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(1, 2) == -1

def test_multiply():
    assert multiply(1, 2) == 2

def test_divide():
    assert divide(2, 1) == 2
