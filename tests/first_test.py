from src.main import Logic

obj = Logic()

def test_add():
    assert obj.add(2, 3) == 5

def test_subtract():
    assert obj.subtract(3, 2) == 1
