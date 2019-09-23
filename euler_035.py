# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, 
# are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?
from euler import isPrime

# if there are even digits, skip it! one of the rotations will be even, therefore non prime.
def contains_even_digits(number):
    even_digits = set('24680')
    return any((d in even_digits) for d in str(number))

def find_rotations(number):
    as_str = str(number)
    result = [number]
    for i in range(0,len(as_str)-1):
        rotation = as_str[1:] + as_str[:1]
        result.append(int(rotation))
        as_str = rotation
    return result

if __name__ == '__main__':
    UPPER_LIMIT = 1000000
    # skip 2, the only EVEN prime...
    number_found = 1 # conting 2
    for i in range(3,UPPER_LIMIT):
        if contains_even_digits(i):
            continue
        if all(isPrime(x) for x in find_rotations(i)):
            number_found += 1
    print(number_found)