input = [
    "75",
    "95 64",
    "17 47 82",
    "18 35 87 10",
    "20 04 82 47 65",
    "19 01 23 75 03 34",
    "88 02 77 73 07 63 67",
    "99 65 04 28 06 16 70 92",
    "41 41 26 56 83 40 80 70 33",
    "41 48 72 33 47 32 37 16 94 29",
    "53 71 44 65 25 43 91 52 97 51 14",
    "70 11 33 28 77 73 17 78 39 68 17 57",
    "91 71 52 38 17 14 91 43 58 50 27 29 48",
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23" ]

triangle = []
for row in input:
    triangle.append([int(x) for x in row.split(" ")])

def findBestPos(level,pos,howDeep):
    """Return the best position in the level that's either pos or pos+1,
       based on the sum of the elements below, going down howDeep levels"""
    # base case, howDeep is 1 (only look at current level)
    row = triangle[level]
    if howDeep == 1 or level >= len(triangle)-1:
        if row[pos] < row[pos+1]:
            pos = pos+1
        return pos
    
    # recurse, one level down
    nextRow = triangle[level+1]
    nextVal = nextRow[findBestPos(level+1,pos,howDeep-1)]
    nextValPlus = nextRow[findBestPos(level+1,pos+1,howDeep-1)]
    if row[pos] + nextVal < row[pos+1] + nextValPlus:
        pos = pos+1
    return pos

# start at the top, and do the sum going down, updating pos as we go
# pos is the index within the level
pos=0
result=triangle[0][0]
for level in range(1,len(triangle)):
    row = triangle[level]
    pos = findBestPos(level,pos,20)
    result += row[pos]

print(result)
