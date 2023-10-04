import pytest

def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # do not change this line until prompted to do so.

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, 4, 7), (5, 6, 11)])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(5, 2, 3),(0, -4, -4),(3, 10, -7)])
def test_subtract(a, b, expected):
    assert(subtract(a, b) == expected)