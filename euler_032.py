# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n 
# exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
# multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written 
# as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once 
# in your sum.

import itertools

products_found = set()

def find_product(digits):
    # digits is an array of digits 1-9 in whatever order. Find two positions, p and e,
    # 0 < p < e, to break the string such that digits[0:p] x digits[p:e] = digits[e:]
    # 'p' = product position, 'e' = equal position

    for p in range(1,8): # max of 7 leaves 2 digits at the end, one for multiplier, one for product
        for e in range(p+1,9):
            multiplicand = int("".join(digits[0:p]))
            multiplier = int("".join(digits[p:e]))
            product = int("".join(digits[e:]))
            if multiplicand * multiplier == product:
                if product in products_found:
                    continue
                print("{0} = {1} x {2}".format(product,multiplicand,multiplier))
                products_found.add(product)

for i in itertools.permutations([str(x) for x in range(1,10)]):
    find_product(i)
print(sum(products_found))
