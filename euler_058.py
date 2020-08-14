# (Euler 058)
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side 
# length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what 
# is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
# that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with 
# side length 9 will be formed. If this process is continued, 
# what is the side length of the square spiral for which the ratio of primes along both 
# diagonals first falls below 10%?
############################################################################################
# euler_028 is a similar problem. In it, I noted
# the two diagonals contain the numbers:
# top-left-to-bottom-right diagonal: (A) 1-3-7-13-21-31-43-57-73-...
# bottom-left-to-top-right diagonal: (B) 1-5-9-17-25-37-49-65-81-...
# 
# The increments between the terms in series (A) are, 2, 4, 6, 8, ... or 2n
# (B) is a little more tricky. The increment between the terms is 4,4,8,8,12,12,16,16,...
# Repeats twice, then jumps by 4... So (n//2)*4

from euler import isPrime

def generateNextA(previousVal, position):
    return previousVal + 2*position

def generateNextB(previousVal, position):
    return previousVal + 4*((position+1)//2)

# represents the values with grid-size 1.
seriesA = [1]
seriesB = [1]
gridSize = 1

numPrimes = 0

while True:
    gridSize += 2 # grow in both dimensions
    seriesA.append(generateNextA(seriesA[-1], gridSize-2))
    seriesA.append(generateNextA(seriesA[-1], gridSize-1))
    seriesB.append(generateNextB(seriesB[-1], gridSize-2))
    seriesB.append(generateNextB(seriesB[-1], gridSize-1))

    if isPrime(seriesA[-1]):
        numPrimes += 1
    if isPrime(seriesA[-2]):
        numPrimes += 1
    if isPrime(seriesB[-1]):
        numPrimes += 1
    if isPrime(seriesB[-2]):
        numPrimes += 1
    
    percentage = numPrimes*100/(len(seriesA)+len(seriesB)-1)
    
    if percentage < 10.0:
        print("{} grid size = {} primes. {}%".format(gridSize, numPrimes, percentage))
        break

# 26241