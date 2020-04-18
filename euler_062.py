# The cube, 41063625 (345^3), can be permuted ([ben: its digits]) to produce two other cubes: 
# 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations 
# of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

def is_permutation(x,y):
    x,y = list(str(x)),list(str(y))
    if len(x) != len(y):
        return False
    # check if all the characters of x are in y
    for i in x:
        if i in y:
            y.remove(i)
        else:
            return False
    return True

def find_cube_with_permutations(number_of_permutations):
    all_cubes = [i**3 for i in range(10000)]
    for i,c in enumerate(all_cubes):
        c = i**3
        print("Testing {} with value {}".format(i,c))
        cubic_permutations = find_cubic_permutations(all_cubes,c)
        if len(cubic_permutations) == number_of_permutations:
            return c

def find_cubic_permutations(all_cubes, number):
    # goes through the cubes, and finds those are are digit permutation of number.
    # to avoid having to go through all of them, we stop once we reach a cube whose
    # length is greater than our number. Assumes all_cubes is sorted
    cubic_permutations = []
    max_length = len(str(number))
    for x in all_cubes:
        if len(str(x)) > max_length:
            return cubic_permutations
        if is_permutation(x, number):
            cubic_permutations.append(x)
    return cubic_permutations

if __name__ == '__main__':
    smallest_cube = find_cube_with_permutations(5)
    print(smallest_cube)