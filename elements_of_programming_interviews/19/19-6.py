# Solution from EPI
# making wired connections
# bipartite graph / two colorable
# write a function that determines if a graphs is two colorable


# idea use bfs, and determine distance from starting point.
# if two vertices, are the same distance away from the starting point and they share an edge,
# return false

class Vertex:
    def __init__(self, id):
        self.id = id
        self.d = None # distance from starting point of bfs
        self.edges = []

def is_two_colorable_helper(vertex):
    vertex.d = 0 # set the starting vertex distance to 0
    queue = []
    queue.append(vertex)

    while len(queue) > 0:
        poppedVertex = queue.pop()
        for edge in poppedVertex.edges:
            # set the distance
            if edge.d is None:
                edge.d = poppedVertex.d + 1
                queue.append(edge) # Add unexplored edges to the queue
            if edge.d == poppedVertex.d:
                return False
    return True

def is_two_colorable(graph):
    return all(is_two_colorable_helper(vertex) for vertex in graph if vertex.d == None)

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')

a.edges = [b, c]
b.edges = [a, c]
c.edges = [a, b]

non_bipartite_graph = [a, b, c]

d = Vertex('d')
e = Vertex('e')
f = Vertex('f')
g = Vertex('g')

d.edges = [e,f]
e.edges = [d,g]
f.edges = [d,g]
g.edges = [e,f]

bipartite_graph = [d,e,f,g]

assert(is_two_colorable(non_bipartite_graph) == False)
assert(is_two_colorable(bipartite_graph) == True)
