# Champernowne 
# An irrational decimal fraction is created by concatenating the positive integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def champernowne():
    i = 1
    while True:
        digits = str(i)
        for d in digits:
            yield int(d)
        i += 1

keepers = []
prod = i = 1
for d in champernowne():
    if i == 1 or i == 10 or i == 100 or i == 1000 or i == 10000 or i == 100000 or i == 1000000:
        keepers.append(d)
        prod *= d
        if i == 1000000:
            break
    i += 1
print(keepers)
print(prod)