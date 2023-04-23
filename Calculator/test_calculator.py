import pytest

from polish_notation import ExpressionEvaluator

calculator = ExpressionEvaluator()

def test_addition():
    assert calculator.compile_calculate("2 + 2") == 4

def test_multiplication():
    assert calculator.compile_calculate("2 * 2") == 4

def test_division():
    assert calculator.compile_calculate("2 / 2") == 1

def test_substraction():
    assert calculator.compile_calculate("2 - 2") == 0

def test_degree():
    assert calculator.compile_calculate("2 ^ 4") == 16

def test_complex_expression():
    assert calculator.compile_calculate("2 + 2 * 2") == 6
    assert calculator.compile_calculate("( 5 + 10 * ( 2 + 4 ) )") == 65
    assert calculator.compile_calculate("( 2 + 2 ^ 4 ) + 16 / 4") == 22
    assert calculator.compile_calculate("2 * 2 ^ 4") == 32
