# Dijkstra's algorithm is an algorithm that determines the shortest path from a source node
# to each other node in the graph.

# there are a number of variants of dijkstra's algorithm.
# One variant involves finding the shortest path from the source node to all other nodes.
# Another variant stops when they find the destination node.
# Other variants load the entire graph at once.  others load only the source and add items to the pq as they go along.

# This variant stops when it finds the destination node and only loads nodes as it explores the lowest cost node.

# first initialize all vertices distance to infinity.
# set th start distance from start to 0
# add start to a priority queue
# for each vertex in the priority queue,
# check if the vertex is the ending vertex we are looking for.  if so break out of the while loop
# otherwise for each of the vertex's neighboars,
# and update the distances from start if the new distance is smaller and the predecessor

import collections
import heapq

DistanceVertexTuple = collections.namedtuple('DistanceVertexTuple', ('distance', 'vertex'))

class Vertex:
    def __init__(self, id=0):
        self.id = id
        self.distance_from_start = float("inf") # Distance from start node in dijkstra
        self.edges = [] # DistanceVertexTuples
        self.pred = None # graph vertex

    def __lt__(self, other):
        if self.id != other.id:
            return self.distance_from_start < other.distance_from_start
        return self.id < other.id

def dijkstra(start, end):
    # initialize the starting vertex's distance_from_start to 0
    start.distance_from_start = 0

    # we are going to use a priority queue with the distance_from_start as the property used to order the vertices
    pq = [DistanceVertexTuple(start.distance_from_start, start)]
    heapq.heapify(pq)

    while len(pq) > 0:
        next_closest_v = heapq.heappop(pq)
        print('next_closest_v', next_closest_v.vertex.id, [tuple.vertex.id for tuple in pq])
        for v in next_closest_v.vertex.edges:
            new_distance_from_start = next_closest_v.vertex.distance_from_start + v.distance

            if new_distance_from_start < v.vertex.distance_from_start:
                try:
                    indexOfDuplicate = pq.index(DistanceVertexTuple(v.vertex.distance_from_start, v.vertex))
                    pq[indexOfDuplicate] = pq[-1]
                    pq.pop()
                    heapq.heapify(pq)
                except:
                    pass

                v.vertex.distance_from_start = new_distance_from_start
                v.vertex.pred = next_closest_v.vertex
                heapq.heappush(pq, DistanceVertexTuple(v.vertex.distance_from_start, v.vertex))
                # doesn't this put nodes back in repeatedly? shouldn't we remove nodes that are already in here with updated priority?
                # need to remove the any tuple with same vertex.


    def outputPath(vertex):
        if vertex is None:
            return
        else:
            print(vertex.id, end=' ')
            outputPath(vertex.pred)

    outputPath(end)

u = Vertex('u')
v = Vertex('v')
x = Vertex('x')
w = Vertex('w')
y = Vertex('y')
z = Vertex('z')

u.edges = [DistanceVertexTuple(2, v), DistanceVertexTuple(5, w), DistanceVertexTuple(1, x)]
v.edges = [DistanceVertexTuple(2, u), DistanceVertexTuple(2, x), DistanceVertexTuple(3, w)]
x.edges = [DistanceVertexTuple(1, u), DistanceVertexTuple(2, v), DistanceVertexTuple(3, w), DistanceVertexTuple(1, y)]
y.edges = [DistanceVertexTuple(1, x), DistanceVertexTuple(1, w), DistanceVertexTuple(1, z)]
w.edges = [DistanceVertexTuple(3, v), DistanceVertexTuple(5, u), DistanceVertexTuple(3, x), DistanceVertexTuple(1, y), DistanceVertexTuple(5, z)]
z.edges = [DistanceVertexTuple(5, w), DistanceVertexTuple(1, y)]

dijkstra(u, z)
