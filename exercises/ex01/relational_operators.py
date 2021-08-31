"""relational_operators.py."""

__author__= "730228106"

name: str = input("Left-hand side:")
name2: str = input("Right-hand side:")
number1: bool = bool(name)
number2: bool = bool(name2) 
print(name + " < " + name2 + " is " + str(number1 < number2))
print(name + " >= " + name2 + " is " + str(number1 >= number2))
print(name + " == " + name2 + " is " + str(number1 == number2))
print(name + " != " + name2 + " is " + str(number1 != number2))