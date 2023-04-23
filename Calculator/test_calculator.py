import pytest

from polish_notation import ExpressionEvaluator

def test_calculate():
    calculator = ExpressionEvaluator()
    assert calculator.compile_calculate("2 + 2") == 4
    assert calculator.compile_calculate("2 * 2") == 4
    assert calculator.compile_calculate("2 / 2") == 1
    assert calculator.compile_calculate("2 - 2") == 0
    assert calculator.compile_calculate("2 ^ 4") == 16
    assert calculator.compile_calculate("2 + 2 * 2") == 6
    assert calculator.compile_calculate("( 5 + 10 * ( 2 + 4 ) )") == 65
    assert calculator.compile_calculate("( 2 + 2 ^ 4 ) + 16 / 4") == 22
    assert calculator.compile_calculate("2 * 2 ^ 4") == 32
