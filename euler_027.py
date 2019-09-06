from euler import isPrime

# Considering quadratics of the form:
#n^2+an+b, where |a|<1000 and |b|≤1000
# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n,
# starting with n=0.

def evaluatePair(a,b):
    """determine how many consecutive primes are generated"""
    n = 0
    count = 0
    while True:
        fx = n**2 + a*n + b
        if isPrime(fx):
            count += 1
            n += 1
        else:
            break
    return count

# b will always be a prime, since when n=0, the equation simplifies to just b, which needs to be prime
# start by finding all the primes up to 1000
primes = [1]
for x in range(3,1000,2):
    if isPrime(x):
        primes.append(x)
# also include the negative of the primes
primes.extend([x * -1 for x in primes])

maxA = 0
maxB = 0
maxPrimes = 0

for a in primes:
    for b in primes:
        numPrimes = evaluatePair(a,b)
        if numPrimes > maxPrimes:
            maxPrimes = numPrimes
            maxA = a
            maxB = b

print( "(a,b)=" + str([maxA,maxB]) + " yielded " + str(maxPrimes) + " primes")
print("a*b = " + str(maxA*maxB))