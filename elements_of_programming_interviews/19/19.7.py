class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.visited = False
        self.distance = None

def isOneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 0: return False
    difference = 0
    for i, char in enumerate(s1):
        if difference == 2:
            return False
        if char != s2[i]:
            difference += 1
    return difference == 1


def generateGraph(words):
    graph = []
    for word in words:
        graph.append(Vertex(word))

    for i in range(len(graph) - 1):
        for j in range(i, len(graph)):
            if isOneAway(graph[i].label, graph[j].label):
                graph[i].edges.append(graph[j])
                graph[j].edges.append(graph[i])
    return graph

def sProducesT(s, t, words):
    graph = generateGraph(words)
    start_vertex = [node for node in graph if node.label == s][0]
    start_vertex.distance = 1 # start at one because steps start at 1
    q = []
    q.append(start_vertex)
    while len(q) > 0:
        popped_vertex = q.pop()
        popped_vertex.visited = True
        if popped_vertex.label is t:
            return popped_vertex.distance
        for edge in popped_vertex.edges:
            if edge.distance == None:
                edge.distance = popped_vertex.distance + 1
            if edge.visited == False:
                q.insert(0, edge)

    return -1

assert(sProducesT('cat', 'dog', ['bat', 'cot', 'dog', 'dag', 'dot', 'cat'])  == 4)
