import itertools

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
i = 1
for x in itertools.permutations(range(10)):
    if i == 1000000:
        print(x)
        break
    i += 1