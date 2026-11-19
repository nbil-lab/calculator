import pytest
from calculator import Calculator


class TestCalculator:
    def test_sum(self):
        calculator = Calculator(op1=2, op2=1)
        assert calculator.sum() == 3

    def test_subtract(self):
        calculator = Calculator(op1=2, op2=1)
        assert calculator.subtract() == 1

    def test_multiply(self):
        calculator = Calculator(op1=1, op2=2)
        assert calculator.multiply() == 2

    def test_divide(self):
        calculator = Calculator(op1=3, op2=6)
        assert calculator.divide() == 0.5

    def test_divide_by_zero(self):
        calculator = Calculator(op1=3, op2=0)
        with pytest.raises(ZeroDivisionError):
            calculator.divide()

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, -2, -3),
        (2.5, 3.5, 6.0),
    ])
    def test_add_parametrized(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.sum() == expected
