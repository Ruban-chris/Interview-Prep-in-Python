# EPI solution
# We can reduce the space complexity of the previous solution and expand its use case to directed graphs
# if we represent the problem using traditional DFS with white, gray, black colorings.

class Vertex:
    white, gray, black = range(3)
    def __init__(self, id):
        self.id = id
        self.color = Vertex.white
        self.edges = []

def has_cycles(vertex):
    if vertex.color == Vertex.gray:
        return True

    vertex.color = Vertex.gray
    if any(has_cycles(neighbor) for neighbor in vertex.edges if neighbor.color != Vertex.black):
        return True
    vertex.color = Vertex.black
    return False

def isMinimallyConnected(graph):
    return not(any(has_cycles(vertex) for vertex in graph if vertex.color == Vertex.white))


a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')

a.edges = [b,c]
b.edges = [e,a,d]
d.edges = [c,b]
c.edges = [a,d]
e.edges = [b]

graphWithCycles = [b,e,c,d,a]

f = Vertex('f')
g = Vertex('g')
h = Vertex('h')
i = Vertex('i')
j = Vertex('j')
k = Vertex('k')
l = Vertex('l')
m = Vertex('m')

f.edges = [g,h]
g.edges = [k,l]
h.edges = [i, j, m]

minimallyConnectedGraph = [f, g, h, i, j, k, l, m]

assert(isMinimallyConnected(graphWithCycles) == False)
assert(isMinimallyConnected(minimallyConnectedGraph) == True)
