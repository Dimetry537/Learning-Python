from calculator import Calculator

exprasion = [2, '+', 2, "*", 2]
calc = Calculator(exprasion)

print(calc.reverse_polish_notation()) # 2 2 * 2 +
print(calc.calculate()) # 6


# TDD
# Test driven development
# BDD
# Behavior driven development
# postgres