# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual 
# in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations 
# of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this sequence?

import itertools
from euler import find_primality

def find_primes(numbers,primality):
    primes = [x for x in numbers if primality[x]]
    primes.sort()
    if len(primes) >= 3:
        for k in primes:
            for incr in range(1,3331):
                trio = [k+incr*i for i in range(3)]
                if all([x in primes for x in trio]):
                    print("{0} => {1}{2}{3}".format(trio,trio[0],trio[1],trio[2]))

primality = find_primality(100000)
count = 0
checked = set()
for c in range(1111,9999):
    as_sorted_string = "".join(sorted(str(c)))
    if as_sorted_string in checked or "0" in as_sorted_string:
        continue
    checked.add(as_sorted_string)
    permutations = [int("".join(x)) for x in itertools.permutations(str(c))]
    find_primes(permutations,primality)