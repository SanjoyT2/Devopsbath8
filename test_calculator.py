import pytest
from calculator import add
def test_add():
    assert add(5,4)==9
    assert add(0,0)==0
    assert add (-5,4)==-1

def test_add():
    assert add(5,4)==9
    assert add(0,0)==0
    assert add (-5,4)==-1

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (-5, -7, -12)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

#def test_parameterized_add(a, b, expected):
#    assert add(a, b) == expected