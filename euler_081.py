# Euler 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is indicated in bold 
# red and is equal to 2427.
#
# Find the minimal path sum from the top left to the bottom right by only 
# moving right and down in p81_matrix.txt, a 31K text file containing an 
# 80 by 80 matrix.

from dijkstra import *

def load_matrix_from_file(filename):
    matrix = []
    f = open(filename, "r")
    for line in f:
        matrix.append([int(x) for x in line.strip().split(",")])    
    f.close()
    return matrix

def node_at(nd,x,y,value):
    key = "{},{}".format(x,y)
    if key in nd:
        return nd[key]
    node = Node(value)
    nd[key] = node
    return node

def convert_matrix_to_graph(m):
    nd = {} # node dictionary, key = "1,5" index in matrix
    all_nodes = []
    for x,row in enumerate(m):
        for y,value in enumerate(row):
            curr = node_at(nd, x, y, value)
            all_nodes.append(curr)
            # add right
            if y < len(row)-1:
                right = node_at(nd, x, y+1, m[x][y+1])
                curr.add_neighbor(right)
            # add down
            if x < len(m)-1:
                down = node_at(nd, x+1, y, m[x+1][y])
                curr.add_neighbor(down)
    return all_nodes

m = load_matrix_from_file("p081_matrix.txt")
nodes = convert_matrix_to_graph(m)
short_path = dijkstra(nodes, nodes[0], nodes[-1])
total = value_sum(short_path)
print(total)