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

def gon_to_string(gon_list):
    g = gon_list # heh
    smallest = min([g[3],g[4],g[5]])
    if g[3] == smallest:
        return ''.join([str(i) for i in [g[3],g[0],g[1],g[5],g[1],g[2],g[4],g[2],g[0]]])
    elif g[4] == smallest:
        return ''.join([str(i) for i in [g[4],g[2],g[0],g[3],g[0],g[1],g[5],g[1],g[2]]])
    else:
        return ''.join([str(i) for i in [g[5],g[1],g[2],g[4],g[2],g[0],g[3],g[0],g[1]]])

n = 0
as_strings = set()
for i in permutations(range(1,7),3):
    #print(str(list(i)))
    for j in permutations(set(range(1,7)) - set(i)):
        x = list(i) + list(j)
        s1, s2, s3 = sum([x[0],x[1],x[3]]), sum([x[0],x[2],x[4]]), sum([x[1],x[2],x[5]])
        if s1 == s2 and s2 == s3:
            as_strings.add(gon_to_string(x))
            print("{} with total {}, str={}".format(x, s1,gon_to_string(x)))
            n += 1
print(n)
print(max(as_strings))