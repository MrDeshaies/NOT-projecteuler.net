import math

# Find the sum of the digits in the number 100!

number = math.factorial(100)
sumOfDigits = 0
for digit in str(number):
    sumOfDigits += int(digit)
print(sumOfDigits)