"""Four random, good fortunes."""

__author__ = "730228106"

from random import randint
number: int = randint(1, 4) 
if number == 1:
    print("Your fortune cookie says...")
    print("Practice makes perfect, dont give up on COMP110")
    print("Now, go spread postive vibes!")
if number == 2:
    print("Your fortune cookie says...")
    print("Dont be so quick to judge others, even the wisest can't see from all angles")
    print("Now, go spread positive vibes!")
if number == 3:
    print("Your fortune cookie says...")
    print("You will recieve a promotion at work soon")
    print("Now, go spread positive vibes!")
if number == 4:
    print("Your fortune cookie says...")
    print("Dont stress, things will work out")
    print("Now, go spread positive vibes!")