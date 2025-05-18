def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 0) == 0

# def test_add_floats():
#     assert add(1.5, 2.5) == 4.0