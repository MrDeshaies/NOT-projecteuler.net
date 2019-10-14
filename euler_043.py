# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of 
# the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# 
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# 
# Find the sum of all 0 to 9 pandigital numbers with this property.
import itertools

def substring_divisibility(tup):
    if len(tup) != 10:
        raise AssertionError("tuple needs to be of length 10")
    
    def dd(start,end,factor):
        sub_str = tup[start-1:end]
        if sub_str[0] == "0":
            sub_str = sub_str[1:]
        return int(sub_str) % factor == 0

    return dd(2,4,2) and dd(3,5,3) and dd(4,6,5) and dd(5,7,7) and dd(6,8,11) and dd(7,9,13) and dd(8,10,17)

matches = []
# generate all 10 digits pandigital permutations
for i in itertools.permutations([str(x) for x in range(10)]):
    i = "".join(i) # convert tuple to string
    if substring_divisibility(i):
        matches.append(int(i))
print("And the sum is: {0}".format(sum(matches)))