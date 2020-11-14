# Euler 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is indicated in bold 
# red and is equal to 2427.
#
# Find the minimal path sum from the top left to the bottom right by only 
# moving right and down in p81_matrix.txt, a 31K text file containing an 
# 80 by 80 matrix.

from dijkstra import dijkstra,value_sum
import euler_081_083_matrix as matrix

m = matrix.load_matrix_from_file("p081_matrix.txt")
nodes = matrix.convert_matrix_to_graph(
    m, include_right=True, include_down=True)
short_path = dijkstra(nodes, nodes[0], nodes[-1])
total = value_sum(short_path)
print(total)