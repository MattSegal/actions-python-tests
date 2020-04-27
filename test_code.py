import pytest

from my_code import add

def test_add_positive():
    assert add(1, 2) == 3

def test_add_zero():
    assert add(1, 0) == 1

def test_add_negative():
    assert add(4, -100) == -96

def test_add_string__expect_exception():
    with pytest.raises(TypeError):
        add(4, 'I DO NOT BELONG HERE')
