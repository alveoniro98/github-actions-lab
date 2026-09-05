from app import add


def test_add():
    assert add(5, 5) == 10

def test_add_zero():
    assert add(5, 0) == 5

def test_add_negative():
    assert add(-2, 2) == 0