import pytest

from polish_notation import ExpressionEvaluator

def test_calculate():
    calculator = ExpressionEvaluator()
    assert calculator.calculate("5 10 2 * 5 / 10 15 + * +") == 105
    assert calculator.calculate("2 4 ^") == 16
    assert calculator.calculate("5 2 4 ^ + 10 5 * 4 / +") == 33.5
    assert calculator.calculate("4 4 10 + + 11 4 * +") == 62

if __name__ == "__main__":
    pytest.main()