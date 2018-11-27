import Hello


def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_power():
    assert power(2,4) == 16
    assert power(3,3) == 27

def test_power2():
    assert power(4,2) == 16
