# Team photo day 2
# Generalize your solution to Team Photo day 1 to determine the largest number
# of teams that can photographed simultaneously subject to the same constraints

# do a topological sort

class GraphVertex:
    def __init__(self):
        self.edges = []
        self.max_distance = 0

def build_topological_ordering(graph):
    vertex_order = []
    def dfs(cur):
        cur.max_distance = 1
        for next in cur.edges:
            if not next.max_distance:
                dfs(next)
        vertex_order.append(cur)

    for vertex in graph:
        if not vertex.max_distance:
            dfs(vertex)
    return vertex_order

def find_longest_path(vertex_order):
    max_distance = 0

    while vertex_order:
        u = vertex_order.pop()
        max_distance = max(max_distance, u.max_distance)
        for v in u.edges:
            v.max_distance = max(v.max_distance, u.max_distance + 1)
    return max_distance

def find_largest_number_teams(graph):
    vertex_order = build_topological_ordering(graph)
    return find_longest_path(vertex_order)

G = [GraphVertex() for _ in range(3)]
G[0].edges.append(G[2])
G[1].edges.append(G[2])
assert 2 == find_largest_number_teams(G)
