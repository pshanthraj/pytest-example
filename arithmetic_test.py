import pytest
import arithmetic

def test_add():
    assert arithmetic.add(1, 2) == 3

def test_subtract():
    assert arithmetic.subtract(1, 2) == -1

def test_multiply():
    assert arithmetic.multiply(1, 2) == 2

def test_divide():
    assert arithmetic.add(1, 2) == 0.5
