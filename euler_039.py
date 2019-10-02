# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p ≤ 1000, is the number of solutions maximised?

import math

def exists_triplet(base, perimeter):
    for height in range(1,perimeter-base):
        hypothenuse = math.sqrt(base**2 + height**2)
        if math.modf(hypothenuse)[0] != 0.0:
            continue
        if base+height+hypothenuse == perimeter:
            print("Perimeter: {0}, found sides ({1},{2},{3})".format(perimeter,base,height,int(hypothenuse)))
            return True
    return False

def count_triplets_for_perimeter(perimeter):
    count = 0
    for base in range(1,perimeter//3):
        if exists_triplet(base, perimeter):
            count += 1
    return count

max_peri = 0
max_count = 0
for i in range(1,1000):
    c = count_triplets_for_perimeter(i)
    if c > max_count:
        max_count = c
        max_peri = i
print("Largest count is {0} with perimeter {1}".format(max_count,max_peri))