import re
import random
import pandas as pd

with open("testing.py") as f:
    random_word = random.choice(list(f))

print("you have only 6 attempts to win the game i.e., guess the word :")

random_word = random_word.upper()

guess = " _ " * len(random_word)

