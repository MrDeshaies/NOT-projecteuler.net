# Euler 82
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in 
# the left column and finishing in any cell in the right column, and only 
# moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
#
# Find the minimal path sum from the top left to the bottom right by only 
# moving right and down in p81_matrix.txt, a 31K text file containing an 
# 80 by 80 matrix.

from dijkstra import dijkstra_compute_distances,value_sum
import euler_081_083_matrix as matrix

m = matrix.load_matrix_from_file("p082_matrix.txt")
nodes = matrix.convert_matrix_to_graph(
    m, include_right=True, include_down=True, include_up=True)

row_length = len(m[0])
min_overall = 999999999999
for x in range(len(m)):
    source = nodes[x*row_length]
    dist, prev = dijkstra_compute_distances(nodes, source)
    
    min_right_dist = 999999999999
    min_right_node = None
    for rx in range(len(m)):
        right = nodes[rx*row_length + row_length-1]
        if dist[right] < min_right_dist:
            min_right_dist = dist[right]
            min_right_node = right
    print("Row {} has min value on right with {} for sum {}".format(x,min_right_node.value,min_right_dist))
    if min_right_dist < min_overall:
        min_overall = min_right_dist
print("And the answer is... {}".format(min_overall))