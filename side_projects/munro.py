from itertools import permutations,combinations,product

print("--- product ---")
for (x,y) in product(range(1,3), repeat=2):
    print("{}, {}".format(x,y))

print("--- permutations ---")
for (x,y) in permutations(range(1,3), 2):
    print("{}, {}".format(x,y))

print("--- combinatons ---")
for (x,y) in combinations(range(1,3), 2):
    print("{}, {}".format(x,y))

# for (x,y,z) in permutations(range(20), 3):
#     volume = x*y*z
#     area = 2*x*y + 2*x*z + 2*y*z
#     if volume == 630 and area == 482:
#         print("x: {}, y: {}, z: {}".format(x,y,z))
#         exit(0)



