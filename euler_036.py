# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def to_binary_string(number):
    return bin(number)[2:]

def reverse(str):
    return str[::-1]

def is_palindrome_two_bases(number):
    binary = to_binary_string(number)
    return str(number) == reverse(str(number)) and binary == reverse(binary)

palindromic_numbers = []
for i in range(1000000):
    if is_palindrome_two_bases(i):
        palindromic_numbers.append(i)
print("There are {0} palindromic numbers and they sum to {1}".format(len(palindromic_numbers), sum(palindromic_numbers)))
