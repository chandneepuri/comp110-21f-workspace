"""numeric_operators.py."""

__author__ = "730228106"

left: str = input("Left-hand side:")
right: str = input("Right-hand side:")
number1: int = int(left)
number2: int = int(right) 
print(left + " ** " + right + " is " + str(number1 ** number2))
print(left + " / " + right + " is " + str(number1 / number2))
print(left + " // " + right + " is " + str(number1 // number2))
print(left + " % " + right + " is " + str(number1 % number2))