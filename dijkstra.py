class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
    
    def add_neighbor(self,n):
        self.neighbors.append(n)

def dijkstra_compute_distances(nodes, source):
    dist = {}
    prev = {}
    Q = []

    # initialize
    for n in nodes:
        dist[n] = 999999999
        prev[n] = None
        Q.append(n)
    dist[source] = source.value

    # compute distance from source to all nodes
    while len(Q) > 0:
        u = min(Q, key=lambda u : dist[u])
        Q.remove(u)
        for v in [n for n in u.neighbors if n in Q]:
            alt = dist[u] + v.value
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    
    return dist, prev

def dijkstra(nodes, source, target):
    dist, prev = dijkstra_compute_distances(nodes, source)

    # compute path from target to source
    shortest_path = []
    u = target
    while u is not None:
        shortest_path.append(u)
        u = prev[u]
    shortest_path = shortest_path[::-1] # reverse it, source to target
    return shortest_path

def value_sum(nodes):
    s = 0
    for n in nodes:
        s += n.value
    return s
