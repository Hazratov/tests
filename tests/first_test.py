from src.main import Logic, Tests
import pytest
from contextlib import nullcontext as does_not_raise
from src.algorithm import close_with_zero


# obj = Logic()
#
# def test_add():
#     assert obj.add(2, 3) == 5
#
# def test_subtract():
#     assert obj.subtract(3, 2) == 1


tests = Tests()

class TestClass:
    def test_sum_success(self):
        a = 5
        b = 6
        result = 11
        assert tests._sum(a, b) == result


    def test_sum_failure(self):
        a = "5"
        b = 6
        pytest.raises(TypeError, tests._sum, a, b)

    # def test_sum_error():
    #     a = "5"
    #     b = "6"
    #     pytest.raises(TypeError, tests._sum, a, b)


    def test_passes(self):
        with pytest.raises(Exception) as e_info:
            x = 1 / 0


    @pytest.mark.parametrize(
        "a,b, result, expectation",
        [
            (1, 1, 2, does_not_raise()),
            (2, 2, 4, does_not_raise()),
            (-4,-2,-6, does_not_raise()),
            (1,"3", TypeError, pytest.raises(TypeError)),
        ]
    )
    def test_passes_failure(self,a, b,result, expectation):
        with expectation:
            assert tests._sum(a, b) == result




    @pytest.mark.parametrize(
        "x, expected",
        [
            ([2,3,4,5,-1,3,1],1),
        ]
    )
    def test_passes_success(self,x, expected):
        assert close_with_zero(x) == expected

    @pytest.mark.parametrize(
        "a, b, result, expectation",
        [
            (1,4,-3,does_not_raise()),
            (2,"2", TypeError, pytest.raises(TypeError)),
            (10,5, 5, does_not_raise())
        ]
    )
    def test_minus(self,a,b,result, expectation):
        with expectation:
            assert tests._minus(a,b) == result
