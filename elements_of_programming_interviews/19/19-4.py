# degrees of connectedness
# Write a program that takes as input an undirected graph, which you can assume to be connected,
# and checks if the graph is minimally connected.

# Ideas
# Use DFS with visited set and parent.

# Time complexity is the same as DFS O(|V| + |E|)

# Space complexity is O(n) where n is the number of vertices in the graph.


class Vertex:
    def __init__(self,id=0):
        self.id = id
        self.nbrs = []

class Graph:
    def __init__(self):
        self.vertices = []

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')

a.nbrs = [b,c]
b.nbrs = [e,a,d]
d.nbrs = [c,b]
c.nbrs = [a,d]
e.nbrs = [b]

graphWithCycles = Graph()
graphWithCycles.vertices = [b,e, c,d,a]

f = Vertex('f')
g = Vertex('g')
h = Vertex('h')
i = Vertex('i')
j = Vertex('j')
k = Vertex('k')
l = Vertex('l')
m = Vertex('m')

f.nbrs = [g,h]
g.nbrs = [k,l]
h.nbrs = [i, j, m]

minimallyConnectedGraph = Graph()
minimallyConnectedGraph.vertices = [f, g, h, i, j, k, l, m]

def isMinimallyConnected(graph):
    if len(graph.vertices) <= 1: return True
    return isMinimallyConnectedHelper(graph.vertices[0], [], None)

def isMinimallyConnectedHelper(vertex, visited, pred):
    print(vertex.id, [vertex.id for vertex in visited])
    if len(vertex.nbrs) == 1 and vertex.nbrs[0] == pred: return True
    if vertex in visited: return False
    visited.append(vertex)
    return all([isMinimallyConnectedHelper(nbr, visited, vertex) for nbr in vertex.nbrs if nbr != pred])

# how do i do this problem with using all?  how do i do this in a for loop? i could collect them and put it into an array and return true if all th values in the array are true

assert(isMinimallyConnected(graphWithCycles) == False)
assert(isMinimallyConnected(minimallyConnectedGraph) == True)
