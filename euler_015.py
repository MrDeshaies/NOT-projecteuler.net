# Euler 15
# Starting in the top left corner of a 2×2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right 
# corner.
# 
# How many such routes are there through a 20×20 grid?

# [Basic math, originally solved with calculator as 40C20.
#  40 directions (down or right) to choose from 20]

from math import factorial

def nCk(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))

print(nCk(40,20))