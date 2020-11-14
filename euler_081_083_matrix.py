# common matrix functions for 081, 082 and 083
from dijkstra import Node

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

def convert_matrix_to_graph(m,
    include_right=False,include_left=False,include_down=False,include_up=False):
    nd = {} # node dictionary, key = "1,5" index in matrix
    all_nodes = []
    for x,row in enumerate(m):
        for y,value in enumerate(row):
            curr = node_at(nd, x, y, value)
            all_nodes.append(curr)
            if include_right and y < len(row)-1:
                right = node_at(nd, x, y+1, m[x][y+1])
                curr.add_neighbor(right)
            if include_left and y > 0:
                left = node_at(nd, x, y-1, m[x][y-1])
                curr.add_neighbor(left)
            if include_down and x < len(m)-1:
                down = node_at(nd, x+1, y, m[x+1][y])
                curr.add_neighbor(down)
            if include_up and x > 0:
                up = node_at(nd, x-1, y, m[x-1][y])
                curr.add_neighbor(up)
    return all_nodes
