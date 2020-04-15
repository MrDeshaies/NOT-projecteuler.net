# a * b = c., where 0 < a,b < 100. 
# Are there values of a for which all c have the same digital sum?

def digital_sum(number):
    return sum([int(i) for i in str(number)])

for a in range(1,10000):
    if all([digital_sum(a*b) == digital_sum(a) for b in range(1,a+1)]):
        print(a)
