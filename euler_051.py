# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 
# 13, 23, 43, 53, 73, and 83, are all prime.
# 
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example 
# having seven primes among the ten generated numbers, yielding the family: 
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this 
# family, is the smallest prime with this property.
# 
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
# with the same digit, is part of an eight prime value family.
import itertools
from euler import find_primality,filter_primes

UPPER_LIMIT = 1000000
primality = find_primality(UPPER_LIMIT)
primes = filter_primes(primality)

def generate_digit_replacement(number,positions):
    result = []
    digits = list(str(number))
    for new_digit in [str(x) for x in range(10)]:
        if new_digit == '0' and 0 in positions:
            continue # don't substitute 0 at the beginning, e.g. turning 13 to simply 3
        # substitute new_digit at positions
        for i in positions:
            digits[i] = new_digit
        result.append(int("".join(digits)))
    return result

def find_prime_family_for_positions(prime,positions,primality):
    family = [x for x in generate_digit_replacement(prime,positions) if primality[x]]
    return family

def find_prime_families(prime,primality):
    prime_str = str(prime)
    # increase the number of digit replacement up to len(prime)-1 (gotta keep at least 1 original digit!)
    for digits_to_replace in range(1,len(prime_str)):
        # find the positions to replace
        for positions in itertools.combinations(range(len(prime_str)),digits_to_replace):
            prime_family = find_prime_family_for_positions(prime,positions,primality)
            if len(prime_family) >= 8:
                print("{0} = {1} {3}: {2}".format(prime, len(prime_family), prime_family,positions))
                exit()

for prime in primes:
    find_prime_families(prime,primality)