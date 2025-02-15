from src.main import Logic, Tests
import pytest

# obj = Logic()
#
# def test_add():
#     assert obj.add(2, 3) == 5
#
# def test_subtract():
#     assert obj.subtract(3, 2) == 1


tests = Tests()

def test_sum_success():
    a = 5
    b = 6
    result = 11
    assert tests._sum(a, b) == result


def test_sum_failure():
    a = "5"
    b = 6
    pytest.raises(TypeError, tests._sum, a, b)

def test_sum_error():
    a = "5"
    b = "6"
    pytest.raises(TypeError, tests._sum, a, b)




