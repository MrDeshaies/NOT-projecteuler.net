# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

UPPER_LIMIT = 1000
total = 0
for i in range(1,UPPER_LIMIT+1):
    total += i**i
print(str(total)[-10:])

# as a one liner... ;-)
print(str(sum(i**i for i in range(1,1001)))[-10:])