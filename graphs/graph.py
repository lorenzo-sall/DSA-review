# The "adjaceny list" implementation of the graph is more space-efficient in comparison to an "adjacency matrix",
# especially when the number of edges to represent is << |V|**2 (the matrix is "sparse")
# This implementation will use a dict to keep track of the vertices and each vertex will use a dictionary to record
# the vertices it is connected to (the keys will be the vertices and the values the weights)

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    # add a neighbor to the connected vertices dict with default weight 0
    def add_neighbor(self, n_id, w = 0):
        self.connections[n_id] = w

    # returns the id of the vertex
    def get_id(self):
        return self.id

    #returns the weight of an edge using the connected vertex
    def get_weight(self, v_id):
        return self.connections[v_id]

    # returns the ids of the connected vertices
    def get_connections(self):
        return self.connections.keys()

    # this will allow us to print information about the vertex and its connections
    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connections])


class Graph:
    def __init__(self):
        self.vertices = {}
        self.v_counter = 0

    def add_vertex(self, key):
        self.v_counter = self.v_counter + 1
        new_v = Vertex(key)
        self.vertices[key] = new_v
        return new_v

    # add a new edge (arguments are source vertex, destination vertex, weight)
    def add_edge(self, s, d, w = 0):
        # create and add vertices if not existing
        if s not in self.vertices:
            new_v = self.add_vertex(s)
        if d not in self.vertices:
            new_v = self.add_vertex(d)
        # add the new edge using the Vertex class method add_neighbor
        self.vertices[s].add_neighbor(self.vertices[d], w)

    # get all the vertices in the graph
    def get_vertices(self):
        return self.vertices.keys()

    # get a specific vertex if it exists
    def get_vertex(self, id):
        if id in self.vertices:
            return self.vertices[id]
        else:
            return None

    def __contains__(self, v):
        return v in self.vertices

    # return an iterator
    def __iter__(self):
        return iter(self.vertices.values())
