# clone graph
# Use DFS to traverse the graph and use a dictionary to maintain a
# copy from vertex to vertex copy.

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')

a.edges = [b,c]
b.edges = [d]
c.edges = [d]
d.edges = [e]
e.edges = [c]

def clone_graph(vertex):
    vertex_copy = Vertex(vertex.label)
    clone_graph_helper(vertex, vertex_copy, {vertex: vertex_copy})
    return vertex_copy

def have_same_edges(vertex, vertex_copy, dictionary):
    if len(vertex.edges) != len(vertex_copy.edges):
        return False
    return all(vertex_copy.edges.index(dictionary[edge]) >= 0 for edge in vertex.edges)

def clone_graph_helper(vertex, vertex_copy, dictionary):
    if have_same_edges(vertex, vertex_copy, dictionary): return
    for edge in vertex.edges:
        if edge in dictionary:
            if not(dictionary[edge] in vertex_copy.edges):
                vertex_copy.edges.append(dictionary[edge])
        else:
            dictionary[edge] = Vertex(edge.label)
            vertex_copy.edges.append(dictionary[edge])
            clone_graph_helper(edge, dictionary[edge], dictionary)

a_copy = clone_graph(a)
b_copy = [edge for edge in a_copy.edges][0]
c_copy = [edge for edge in a_copy.edges][1]
d_copy = b_copy.edges[0]
assert(b_copy.edges[0] == c_copy.edges[0])
e_copy = d_copy.edges[0]
