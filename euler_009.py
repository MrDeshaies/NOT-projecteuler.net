import math

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# since the sum is 1000, each number < 500
for a in range(1,500):
    for b in range(a+1,500):
        c = math.sqrt(a**2 + b**2)
        if math.modf(c)[0] != 0.0:
            continue
        if a+b+c == 1000:
            print str(a) + " + " + str(b) + " + " + str(c)
            print a**2 + b**2 == c**2
            print a*b*c
