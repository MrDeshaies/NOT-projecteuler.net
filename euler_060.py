# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating 
# them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 
# are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with 
# this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
from euler import list_primes,isPrime,mIsPrime,find_primality

PRIMALITY_LIMIT=10000000
primality = find_primality(PRIMALITY_LIMIT)
def is_prime(x):
    if x >= PRIMALITY_LIMIT:
        return mIsPrime(x)
    else:
        return primality[x]

def concatenate_number(x,y):
    return int( str(x) + str(y) )

def pair_check_last(pgroup):
    """return True/False

    Accepts a list of number. Check each of them for pair-wise primality against the last number
    in the list. Presumably the numbers other than the last have been checked together already
    as they were added to the group
    """
    if len(pgroup) < 2:
        return True #only one number, we're all good
    p2 = pgroup[-1]
    for p1 in pgroup[:-1]:
        # concatenate the two numbers
        x = concatenate_number(p1,p2)
        y = concatenate_number(p2,p1)
        if not is_prime(x) or not is_prime(y):
            return False
    return True

# UPPER_LIMITS = [7000,7000,10000,10000,30000,35000] # exploratory run (long!)
UPPER_LIMITS = [100,100,6000,6000,7500,8500] # winning run, optimized from result [13, 5197, 5701, 6733, 8389]
GROUP_SIZE = 5
# initialize level 1...
primes = list_primes(UPPER_LIMITS[0])
previous_groups = [[x] for x in primes]
for i in range(2,GROUP_SIZE+1):
    print("----- Level {} ------".format(i))
    primes = list_primes(UPPER_LIMITS[i])
    print("Initialized... with {} primes up to {}. Min/max {}/{}".format( \
        len(primes), UPPER_LIMITS[i], min(primes), max(primes)))
    print("Testing {} groups against {} primes".format(len(previous_groups),len(primes)))
    new_groups = []
    for g in previous_groups:
        for p in primes:
            if p <= max(g):
                continue # only consider p greater than the group
            candidate = g + [p]
            if pair_check_last(candidate):
                new_groups.append(candidate)
    if len(new_groups) == 0:
        print("Nothing found")
    else:
        new_groups.sort(key=sum)
        print("Found {} groups. Smallest is {} with sum {}".format(len(new_groups),new_groups[0], sum(new_groups[0])))
    previous_groups = new_groups