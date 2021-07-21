# This class implements the Binary Heap structure.
# binary heaps have the structure of a binary tree with the following constraints:
#  - the tree is complete. all levels are filled, with the possible exception of last one. if the last level
#    is not full it is filled from left to right
#  - the key stored in each node is either always >= (max-heaps) or always <= (min-heaps) respect to the node's children key
#
# This structure stores items in a list.
# Binary heaps are used to implement priority queues: inserting an item and removing the item with the max (min) key
# is O(log(n)). Operations on the list representation are performed wit simple math because the tree is complete and
# we know that the left child of a node P at position p will be at position 2*p and the right child at 2*p+1.
# In this implementation the item with the smaller key will always be at the front of the queue (min-heap).

class BinaryHeap:

    def __init__(self):
        self.internal_list = [0]    # root of the tree, temporary value to allow arithmetic operations
        self.current_size = 0

    # helper function that moves up items that break min-heap compliance (used when inserting)
    def move_up(self, i):
        while i // 2 > 0:
            #compare with parent
            if self.internal_list[i] < self.internal_list[i // 2]:
                #swap if parent > child
                self.internal_list[i], self.internal_list[i // 2] = self.internal_list[i // 2], self.internal_list[i]
            i = i // 2  #set counter to parent position

    # find the index of smallest child, called by move_down()
    def min_child(self, i):
        # check if right child exists
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            # compare left and right child, return index of min
            if self.internal_list[i * 2] < self.internal_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # helper function that moves down items that break min-heap compliance (used when removing items from queue)
    def move_down(self, i):
        while i * 2 <= self.current_size:
            #get min child index
            min_c = self.min_child(i)
            #compare with min child
            if self.internal_list[i] > self.internal_list[min_c]:
                self.internal_list[i], self.internal_list[min_c] = self.internal_list[min_c], self.internal_list[i]
            i = min_c

    def insert(self, new_k):
        self.internal_list.append(new_k)    # append the new item
        self.current_size = self.current_size + 1   # increase the size variable
        self.move_up(self.current_size)     # call helper function to swap the new item with its parent until it is in the right place

    def del_min(self):
        return_v = self.internal_list[1]    # set the return value to the first item excluding the root (which will be popped)
        self.internal_list[1] = self.internal_list[self.current_size]    # copy the last item to the first position (excluding root)
        self.current_size = self.current_size - 1   # decrease current size
        self.internal_list.pop()    # remove last item
        self.move_down(1)   # restore the order of the items by moving the item at index 1 down appropriately
        return return_v

    # this function builds a binary heap directly from a full input list
    # the list is appended to the root and then the items are moved down to the appropriate position
    def build_heap(self, l):
        i = len(l) // 2
        self.current_size = len(l)
        self.internal_list = [0] + l[:]
        while i > 0:
            self.move_down(i)
            i = i - 1
