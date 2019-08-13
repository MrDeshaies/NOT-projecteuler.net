# What is the sum of the digits of the number 2^1000 ?
# Again, this must be harder in some languages without native big integer support (e.g. C)
digits = [int(x) for x in str(2**1000)]
print(str(digits) + " has digit sum " + str(sum(digits)))
