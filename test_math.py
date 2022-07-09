
import re


def sum(first, second):
    return first + second

def test_sum():
    a = 2
    b = 3
    result = sum(a, b)
    assert result == 5, "Simple sum not working"

def test_sum_0():
    result = sum(2, 0)
    assert result == 2, "Sum with 0 not working"

def test_sum_negative():
    result = sum(2, -2)
    assert result == 0, "Sum with negative not working"

test_sum()
test_sum_0()
test_sum_negative()
print("Sum good!")


def median(first, second):
    return (first + second)/2


def test_median():
    a = 10
    b = 20
    assert median(a, b) == 15, "Median is not doing the right thing"

def test_median_negative():
    a = 10
    b = -10
    assert median(a, b) == 0, "Median is not doing the right thing"


def test_median_fails():
    a = 10
    b = 0
    assert median(a, b) == 0, "Median is not doing the right thing"

test_median()
test_median_negative()
# test_median_fails()
print("Median good!")

def mul(first, second):
    return first * second

def test_multiplication():
    a = 3
    b = 4
    assert mul(a, b) == 12, "Multiplication doesn't work properly"

def test_multiplication_negative():
    a = 3
    b = -4
    assert mul(a, b) == -12, "Multiplication doesn't work properly"

def test_multiplication_identity():
    a = 3
    b = 1
    assert mul(a, b) == 3, "Multiplication doesn't work properly"

def test_multiplication_zero():
    a = 3
    b = 0
    assert mul(a, b) == 0, "Multiplication doesn't work properly"

test_multiplication()
test_multiplication_negative()
test_multiplication_identity()
test_multiplication_zero()
print("Multiplication is good!")
