"""Repeating a beat in a loop."""

__author__ = "730228106"

i: int = 0
s: str = ""
beat: str = input("What beat do you want to repeat?")
times: int = int(input("How many times do you want to repeat it?"))

if (times <= i):
    print("No Beat...")
else:
    while i < times: 
        s = s + beat 
        i = i + 1  
    print(s)