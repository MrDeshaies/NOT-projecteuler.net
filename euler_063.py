# (Euler 063)
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?
#
# My notes: 10^x will have x+1 digits... So the base must always be <= 9.

def find_digital_power(n):
    count = 0
    for i in range(1,10):
        k = str(i**n)
        if len(k) == n:
            count += 1
    print("{}: count={}".format(n,count))
    return count

count = 0
for n in range(1,25): #limit to 25 since n>=22 is always 0
    num_for_n = find_digital_power(n)
    count += num_for_n
print("TOTAL COUNT: " + str(count))