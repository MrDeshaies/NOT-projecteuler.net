# Euler 68
# See https://projecteuler.net/problem=68 -- there are graphics!
# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
#
# Working clockwise, and starting from the group of three with the numerically lowest external node 
# (4,3,2 in this example), each solution can be described uniquely. For example, the above solution 
# can be described by the set: 4,3,2; 6,2,1; 5,1,3.
#
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
#
# Total	Solution Set
# 9	4,2,3; 5,3,1; 6,1,2
# 9	4,3,2; 6,2,1; 5,1,3
# 10	2,3,5; 4,5,1; 6,1,3
# 10	2,5,3; 6,3,1; 4,1,5
# 11	1,4,6; 3,6,2; 5,2,4
# 11	1,6,4; 5,4,2; 3,2,6
# 12	1,5,6; 2,6,4; 3,4,5
# 12	1,6,5; 3,5,4; 2,4,6
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
# 
# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. 
# What is the maximum 16-digit string for a "magic" 5-gon ring?

from itertools import combinations, permutations

def start_tuple_idx(gon, tuples):
    min_val = 999999999
    min_idx = -1
    for i,t in enumerate(tuples):
        if gon[t[0]] < min_val:
            min_val = gon[t[0]]
            min_idx = i
    return min_idx

def gon_to_string(gon, tuples):
    start_tuple = start_tuple_idx(gon, tuples)
    num_tuples = len(tuples)
    result = ""
    for t in [(x+start_tuple)%num_tuples for x in range(num_tuples)]:
        result += "".join([str(gon[i]) for i in tuples[t]])
    return result

def is_magic(gon, tuples):
    sums = [sum([gon[i] for i in t]) for t in tuples]
    return min(sums) == max(sums)

n = 0
m = 0
gon5_tuples = [(5,0,1), (9,1,2), (8,2,3), (7,3,4), (6,4,0)]
as_strings = set()
for i in permutations(range(1,11),5):
    for j in permutations(set(range(1,11)) - set(i)):
        x = list(i) + list(j)
        n += 1
        if n % 100_000 == 0:
            print(n)
        if not is_magic(x, gon5_tuples):
            continue
        m += 1
        gs = gon_to_string(x, gon5_tuples)
        as_strings.add(gs)
        print("{}, str={}".format(x, gs))
print("Found {} magic".format(m))
print(max(as_strings))