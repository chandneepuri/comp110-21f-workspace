"""Counting letters in a string."""

__author__ = "730228106"

letter: str = input("What letter do you want to search for? ")
i: int = 0 
word_string: str = input("Enter a word:")
count: int = 0 


while i < len(word_string):
    if letter == word_string[i]:
        count = count + 1
        i = i + 1 
    else: 
        i = i + 1

print("count: " + str(count))