"""
8.7. The Word Ladder Problem
To begin our study of graph algorithms let’s consider the following puzzle called a word ladder.
Transform the word “FOOL” into the word “SAGE”.
In a word ladder puzzle you must make the change occur gradually by changing one letter at a time.
At each step you must transform one word into another word, you are not allowed to transform a word into a non-word.
"""

# We will use the breadth first search algorithm to search a graph representation of the word ladder problem
# Starting from a vertex in the graph, BFS will find all the vertices at a distance k from the start before
# finding any vertex at distance k+1 from the start.
# The Vertex class used to populate the graph has been modified with the attributes "distance" (from the start),
# "predecessor" and "color" ("white" for undiscovered nodes, "grey" for not fully explored and "black" for fully
# explored).
# Also, to keep track of the vertices that need to be explored we will use a queue

import time

class Queue:
    """
    implementation of the queue abstract data type
    using a python list where the elemtent at index 0 is the rear of the queue
    and the elemtent at index (len(queue) -1) is the front
    with this implementation adding an elemtent will be O(n) and removing an
    elemtent will be O(1)
    access to the elemtents is by FIFO (first in first out)
    """

    def __init__(self):
        # the queue is created empty
        self.elemtents = []

    def is_empty(self):
        # returns True if the queue is empty
        return self.elemtents == []

    def enqueue(self, elemtent):
        # add an elemtent to the rear of the queue
        self.elemtents.insert(0, elemtent)

    def dequeue(self):
        # remove one elemtent from the front of the queue
        return self.elemtents.pop()

    def peek(self):
        # it looks at the elemtent at the front of the queue
        return self.elemtents[len(self.elemtents) - 1]

    def size(self):
        # returns the number of elemtents in the queue
        return len(self.elemtents)

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}
        self.dist = 0   # distance from the start vertex
        self.pred = None   # predecessor
        self.color = "white"    # initialize undiscovered

    # add a neighbor to the connected vertices dict with default weight 0
    def add_neighbor(self, v, weight = 0):
        self.connections[v] = weight

    # returns the id of the vertex
    def get_id(self):
        return self.id

    #returns the weight of an edge using the connected vertex stored in connections (argument is a vertex)
    def get_weight(self, v):
        return self.connections[v]

    # returns the ids of the connected vertices
    def get_connections(self):
        return self.connections.keys()

    # this will allow us to print information about the vertex and its connections
    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connections])

    def set_dist(self, d):
        self.distance = d

    def get_dist(self):
        return self.dist

    def set_pred(self, v):
        self.pred = v

    def get_pred(self):
        return self.pred

    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

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

# function to build a graph in memory from a wordlist file.
# the wordlist has been already cleaned and contains only words of the same length.
# returns a graph
def build_graph(wordlist):
    # a dictionary will store the buckets of words that differ by one letter like
    # d = {
    #   "_ine": ["fine", "line", "mine"],
    #   "min_": ["mine", "mint"]
    #   }
    d = {}
    g = Graph()

    # add words to buckets (create buckets if they don't exist already)
    with open(wordlist, 'r') as wlist:
        for l in wlist:
            w = l.strip()
            for i in range(len(w)):
                bucket = w[:i] + "_" + w[i+1:]
                if bucket in d:
                    d[bucket].append(w)
                else:
                    d[bucket] = [w]

    # create edges for words in the same bucket (words that differ by one letter)
    # our implementation of the add_edge() function will automatically create the vertices that don't exist
    for bucket in d.keys():
        for w1 in d[bucket]:
            for w2 in d[bucket]:
                if w1 != w2:
                    g.add_edge(w1, w2)

    return g

# this function runs the breadth first search algorithm on a graph from the provided start vertex
def bf_search(graph, start_v):
    # set initial values for the start vertex
    start_v.set_dist(0)
    start_v.set_pred(None)
    # create queue and enqueue the start vertex
    v_queue = Queue()
    v_queue.enqueue(start_v)

    # until the queue is empty
    while (v_queue.size() > 0):
        current_v = v_queue.dequeue()   # extract elemtent from front of queue

        # iterate on all the current vertex neighbours
        for nbr_v in current_v.get_connections():
            if nbr_v.get_color() == "white":    # if was undiscovered
                nbr_v.set_color("grey")         # set as discovered and not fully explored
                nbr_v.set_dist(nbr_v.get_dist() + 1)    # increase its distance from start by 1 (+1 compared to the current vertex)
                nbr_v.set_pred(current_v)   # set the neighbour's predecessor to the current vertex
                v_queue.enqueue(nbr_v)      # add to the rare of the queue
        current_v.set_color("black")    # after all the neighbours are discovered the current vertex is fully explored

def traverse(target_v):
    v = target_v
    while (v.get_pred()):
        print(v.get_id())
        v = v.get_pred()
    print(v.get_id())

t = time.time()
word_ladder_graph = build_graph("./wordlist_4_clean")
exec_t = time.time() - t
print(f"[ ] Built graph from file in {exec_t} seconds")

t = time.time()
bf_search(word_ladder_graph, word_ladder_graph.get_vertex("fool"))
exec_t = time.time() - t
print(f"[ ] BFS run in {exec_t} seconds. All nodes explored")

t = time.time()
traverse(word_ladder_graph.get_vertex("sage"))
exec_t = time.time() - t
print(f"[ ] Graph traversed in {exec_t} seconds")
