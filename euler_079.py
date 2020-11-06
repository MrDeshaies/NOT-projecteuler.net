# Euler 79
# A common security method used for online banking is to ask the user for three random characters 
# from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; 
# the expected reply would be: 317.
# 
# The text file, keylog.txt, contains fifty successful login attempts.
# 
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest 
# possible secret passcode of unknown length.

def load_attempts(filename):
    attempts = []
    f = open(filename, "r")
    for line in f:
        attempts.append(line.strip())
    f.close()
    # filter duplicates
    nodup = list(dict.fromkeys(attempts))
    print("Loaded {} attempts, unique={}, {}".format(len(attempts),len(nodup),nodup))
    return nodup

def is_potential_try(passcode, attempt):
    start = 0
    for k in attempt:
        p = passcode.find(k, start)
        if p == -1:
            return False
        start = p
    return True

def is_potential_passcode(passcode, attempts):
    return all([is_potential_try(passcode,a) for a in attempts])

class Node:
    def __init__(self, value):
        self.value = value
        self.outgoing = {}
        self.incoming = {}
    
    def add_edge_to(self,other):
        self.outgoing[other.value] = other
        other.incoming[self.value] = self

    def is_root(self):
        return len(self.incoming) == 0
    
    def depth_first_longest_path(self):
        string = str(self.value)
        max_sub = max(
            [n.depth_first_longest_path() for n in self.outgoing.values()], 
            key=len, default='')
        return string + max_sub
    
    def __str__(self):
        outgoing_str = []
        for x in self.outgoing.values():
            outgoing_str.append(x.value)
        return "{}: {}".format(self.value, outgoing_str)

nodes = {}
def get_node(value):
    if value not in nodes:
        nodes[value] = Node(value)
    return nodes[value]

def add_edge(from_value, to_value):
    get_node(from_value).add_edge_to(get_node(to_value))

def solve_079():
    # load attempts
    attempts = load_attempts("p079_keylog.txt")
    # build graph from attempts
    for a in attempts:
        add_edge(a[0], a[1])
        add_edge(a[1], a[2])
    # find the root note, and then the longuest path from it
    for n in nodes.values():
        if n.is_root():
            print("Root note: {}".format(n))
            pwd = n.depth_first_longest_path()
            print("{} is potential passcode {}".format(pwd,
                is_potential_passcode(pwd, attempts)))

if __name__ == '__main__':
    solve_079()