# Data Structures and Algorithms with Python
This repository is a collection of notes and exercises I put together while reviewing concepts related to data structures, sorting and search algorithms.

## Disclaimer
Since this resource is intended for my personal study I have no defined plans for it, but I still plan to add some sections while I keep studying and reviewing material (see #TODO section).
While there is no guarantee that this information and the code collected here is completely accurate (non of these has been reviewed by anyone but my self and as I said it is product of self study) I am always happy to receive advice/suggestions/criticism.

## Sections
### algorithm_analysis
This section contains snippets of code related to concepts of algorithm analysis, with an overview of the Big-O notation.
Timing of the functions is performed with the `timeit` module and the visualisation of graphs is implemented with `matplotlib` and `numpy`.

### basic_data_structures
This section contains the python representation of the Stack, Queue and Double-ended Queue abstract data types.

### recursion
This is a collection of scripts that produce different visual effects using recursive functions. The "graphic" components use the python `turtle` module.

### sorting_searching
In this section contains the following:
#### `sorting.py`
Several sorting algorithms as functions:
- Bubble Sort (and Short Bubble Sort)
- Selection Sort
- Insertion Sort
- Shell Sort
- Merge Sort
- Quick Sort
#### `binary_search.py`
Function implementing the Binary Search algorithm
#### `hash_table.py`
The HashTable class represents the Map abstract data type. It is tested in `hash_test.py`
#### `visualize_sorting`
This folder contains the components of a simple GUI application that visualises sorting algorithms in action. The functions used in this application are a modified version of the previously implemented functions with some coded added for the visualisation part. It uses the `tkinter` python module.

### tree_algorithms
This contains code for a BinaryTree class and a BinaryHeap class, each one with a test scripts to verify the functionalities.

### graphs
This section contains `graph.py` which has the definition of a Vertex and a Graph class, used in this section to solve different problems using graphs. `test_graph.py` and `v_test_graph.py` test the basic methods of these classes producing command line and graphic output respectively.
`breadth_first_search_word_ladder.py` uses a graph and the Breadth Fisrt Search algorithm to solve the Word Ladder problem. This script uses a wordlist of 4 letter words which is included as `wordlist_4_clean`.

## References
The main reference for theory and code is
_Miller, B. and Ranum, D., 2013. Problem solving with algorithms and data structures (Release 3.0)._
and the [online version of the book](https://runestone.academy/runestone/books/published/pythonds/index.html)

## TODO
This is a list of things I would like to add and modify, in random order:
- add more sorting algorithms to the `visualize_sorting` application
- Depth First Search algorithm
- Topological sorting
- Strongly connected components
- Shortest Path problems and Dijkstra’s Algorithm
- Prim’s Spanning Tree Algorithm
