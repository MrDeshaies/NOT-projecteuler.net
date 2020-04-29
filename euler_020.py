import math

# Find the sum of the digits in the number 100!

number = math.factorial(100)
print( sum([int(d) for d in str(number)]) )