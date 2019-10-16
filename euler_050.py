# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, 
# and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from euler import find_primality,list_primes

UPPER_LIMIT = 1000000
primes = list_primes(UPPER_LIMIT)
primality = find_primality(UPPER_LIMIT)

max_length = 0
max_prime = 0
for i in range(0,len(primes)):
    for j in range(i+i,len(primes)):
        if primes[i] * max_length > UPPER_LIMIT:
            # end earlier when there are no more possible solutions
            # we know primes[i+] > primes[i], and the sum will bust
            break
        s = sum(primes[i:j])
        if s > UPPER_LIMIT:
            break
        l = j-i
        if primality[s] and l > max_length:
            print("{0}: {1} = {2}".format(l,s,primes[i:j]))
            max_length = l
            max_prime = s
print(max_prime)