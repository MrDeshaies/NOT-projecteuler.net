triangle = []

def findLargestSumInTriangle() :
    # find 1 row from the bottom. Replace each value with the sum of itself and the max number below it
    # move up and repeat...
    
    for row in range(len(triangle)-2, -1, -1):
        for pos in range(0, len(triangle[row])):
            triangle[row][pos] += max(triangle[row+1][pos], triangle[row+1][pos+1])
    return triangle[0][0]
