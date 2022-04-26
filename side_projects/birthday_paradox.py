# in a group of 23 people, you have 50% chance of
# two of them having the same birthday. Really?
# https://en.wikipedia.org/wiki/Birthday_problem
# You can calculate the probalities, or simulate it like here!

import random

NUMBER_OF_PEOPLE = 23
NUMBER_OF_SETS = 10_000
NUMBER_OF_MATCH = 0

def has_duplicate(l) -> bool:
    """return a boolean, whether the array contains a duplicate element"""
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                return True
    return False

for i in range(NUMBER_OF_SETS):
    # represent birthdate as int between 0 and 365
    bithday_list = [random.randrange(365) for i in range(NUMBER_OF_PEOPLE)]
    if has_duplicate(bithday_list):
        NUMBER_OF_MATCH += 1

print("Ratio with {} people is {}".format(NUMBER_OF_PEOPLE, (NUMBER_OF_MATCH/NUMBER_OF_SETS)))