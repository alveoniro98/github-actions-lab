from app import add, multiply


def test_add():
    assert add(5, 5) == 10

def test_add_zero():
    assert add(5, 0) == 5

def test_add_negative():
    assert add(-2, 2) == 0

def test_multiply():
    assert multiply(2, 3) == 7

def test_multiply_zero():
    assert multiply(10, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6