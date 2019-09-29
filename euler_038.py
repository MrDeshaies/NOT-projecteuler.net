# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
import re

def digit_repeats(number_string):
    return re.search(r"(.).*\1", number_string) != None

def pandigital(number_string):
    return len(number_string) == 9 and all([x in number_string for x in "123456789"])

def try_number(num):
    concat = ""
    for p in range(1,10):
        concat += str(num*p)
        if digit_repeats(concat):
            return -1
        if pandigital(concat):
            return int(concat)
    return -1

max_prod = 0
# i has to be max 4 digits. If i is 5 digits, concat(i*1, i*2) will be 10 digits, greater than 9 allowed
for i in range(10000):
    concat_products = try_number(i)
    if concat_products > max_prod:
        print("{0} => {1}".format(i,concat_products))
        max_prod = concat_products
print(max_prod)