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

def test_multiplication_after_addition():
    assert calculator.compile_calculate("2 + 2 * 2") == 6

def test_bracket():
    assert calculator.compile_calculate("( 5 + 10 ) * ( 2 + 4 )") == 90

def test_duo_bracket():
    assert calculator.compile_calculate("( ( 5 + 10 ) * 2 ) * 5") == 150

def test_degree_in_bracket():
    assert calculator.compile_calculate("( 2 + 2 ^ 4 ) + 16 / 4") == 22

def test_degree_after_multiplication():
    assert calculator.compile_calculate("2 * 2 ^ 4") == 32

def test_division_multiplication():
    assert calculator.compile_calculate("2 * 2 / 4") == 1

def test_without_space():
    assert calculator.compile_calculate("3+3") == 6

def test_with_two_spaces():
    assert calculator.compile_calculate("3  +  3") == 6
