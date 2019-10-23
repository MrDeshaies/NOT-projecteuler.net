# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
# but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def has_same_digits(n1,n2):
    return sorted(list(str(n1))) == sorted(list(str(n2)))

x = 1
POWERS = 6
while True:
    if all([has_same_digits(x,x*i) for i in range(1,POWERS+1)]):
        print("{0}: {1}".format(x, [x*i for i in range(1,POWERS+1)]))
        exit()
    x += 1
