# Project Euler 92
# A number chain is created by continuously adding the square of the digits in a number to form 
# a new number until it has been seen before.
# 
# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# 
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most 
# amazing is that EVERY starting number will eventually arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?

# [Benoit] To speed up the determination, consider the biggest sum possible, that 9,999,999
# which is 9^2 * 7 = 81 * 7 = 567. We can build an array that size, each position indicating
# 1 or 89 depending on the end of that sequence. Then for 1-10M, we sum the digits square ONCE, 
# and look into the array to save computing the entire chain.
# N.B. those that end in 1 are called "magic numbers"

def sum_digits_square(x):
    return sum([int(c)**2 for c in str(x)])

def is_magic(x):
    seen = [x]
    while True:
        s = sum_digits_square(x)
        if s == 1:
            return True
        if s in seen:
            return False
        seen.append(s)
        x = s

def solve_092():
    magic = [None] * 568
    magic[0] = False
    for x in range(1,568):
        magic[x] = is_magic(x)

    count = 0
    for i in range(1,10_000_000):
        x = sum_digits_square(i)
        if not magic[x]:
            count += 1
    print(count)

if __name__ == '__main__':
    solve_092()