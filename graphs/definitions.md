# Graphs: Useful Definitions and Terminology

## Vertex
A **vertex** (or node) is a fundamental part of a graph. It can have a **key** and it can hold additional information (**payload**).

## Edge
An **edge** (or arc) connects two vertices to represent a relationship between them. Edges may be **one-way or two-way**. If the edges in a graph are all one-way, we say that the graph is a **directed graph**, or a digraph.
Edges may be **weighted** to show that there is a cost to go from one vertex to another.

## Graph Representation
A graph G can be represented as *G = (V,E)* where *V* is a set of vertices and *E* is a set of edges.
Each edge is a tuple *(v,w)* where *v,w ∈ V*. A third element can be added to the tuple to represent the weight.

## Path
A **path** is a sequence of vertices connected by edges. Formally:
*w_1,w_2,...,w_n* such that *(w_i,w_i+1) ∈ E* for all *1 <= i <= n-1*
The **unweighted path length** is the number of edges in the path. The **weighted path length** is the sum of the weights of all the edges in the path.

## Cycle
A **cycle** in a directed graph is a path that starts and ends at the same vertex. A graph with no cycles is called **acyclic graph**. A directed graph with no cycles is called a **directed acyclic graph** or a **DAG**.



Reference:
_Miller, B. and Ranum, D., 2013. Problem solving with algorithms and data structures (Release 3.0)._
