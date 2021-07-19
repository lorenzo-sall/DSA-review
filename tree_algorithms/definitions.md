# Trees: Useful Definitions

## Definition One (with nodes and edges)
A **tree** consist of a set of **nodes** and a set of **edges** that connect pairs of nodes.
A tree has the following properties:
- One node of the tree is designated as the **root node**.
- Every node _n_, except the root node, is connected by an edge from exactly one **parent node** _p_.
- A **unique path** traverses from the root to each node.
- If each node in the tree has no more than two children, we say that the tree is a **binary tree**.

## Definition Two (recursive definition)
A **tree** is either empty or consists of a **root** and zero or more **subtrees**, each of which is also a tree. The root of each subtree is connected to the root of the parent tree by an **edge**.

Reference:
_Miller, B. and Ranum, D., 2013. Problem solving with algorithms and data structures (Release 3.0)._
