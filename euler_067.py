from triangle_018_067 import triangle
from triangle_018_067 import findLargestSumInTriangle

f = open("p067_triangle.txt", "r")
for line in f:
    line = line.strip()
    if line == "":
        break
    triangle.append([int(x) for x in line.split(" ")])
f.close()

result = findLargestSumInTriangle()
print(result)
# print(triangle[0])
# print(triangle[1])
# print(triangle[2])
# print(triangle[99])
# print(len(triangle))