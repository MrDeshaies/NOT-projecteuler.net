# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral 
# is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# ben's notes: the two diagonals contain the numbers:
# top-left-to-bottom-right diagonal: (A) 1-3-7-13-21-31-43-57-73-...
# bottom-left-to-top-right diagonal: (B) 1-5-9-17-25-37-49-65-81-...
#
# For a 5x5 grid, you sum up A[0:5]+B[0:5]-1  (-1 because you counted the "1" at the centre twice)
#
# A) is pretty straightforward to generate: the difference grows by 2n:
#       3-1 = 2
#       7-3 = 4
#      13-7 = 6 etc.

GRID_SIZE = 1001

def generateNextA(previousVal, position):
    return previousVal + 2*position

seriesA = [1]
for i in range(1,GRID_SIZE):
    seriesA.append(generateNextA(seriesA[-1],i))
sumSeriesA = sum(seriesA)

# B) is a little more tricky. The increment between the terms is 4,4,8,8,12,12,16,16,...
# Repeats twice, then jumps by 4... So (n//2)*4
def generateNextB(previousVal, position):
    return previousVal + 4*((position+1)//2)

seriesB = [1]
for i in range(1,GRID_SIZE):
    seriesB.append(generateNextB(seriesB[-1],i))
sumSeriesB = sum(seriesB)

# and the answer for a is...
print(sumSeriesA+sumSeriesB-1)