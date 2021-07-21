from binaryheap import *
import random

# just a simple print function to quickly see the tree structure.
# do not use with too many elements
def print_bh(h):
    l = h.internal_list[1:] # remove the [0] placeholder
    s = h.current_size
    t = h.current_size * 2 # counter for tabs
    i = 0
    lb = 0  # lower bound
    ub = 1  # upper bound
    while ub < s:
        for e in l[lb:ub]:
            print(" "*t, end="")
            print("%2d" % e, end="")
            print(" "*t, end="")
        print("")
        lb = ub
        i = i + 1
        ub = ub + (2**i)
        t = t // 2
    for e in l[lb:]:
        print(" "*t, end="")
        print("%2d" % e, end="")
        print(" "*t, end="")
    print("")


bh = BinaryHeap()

for i in range(0,15):
    bh.insert(random.randint(1,50))

print("bh:\t\t", bh.internal_list[1:])
print("pop:\t\t", bh.del_min())
print("pop:\t\t", bh.del_min())
print("bh:\t\t", bh.internal_list[1:])

source_list = [random.randint(1, 50) for x in range(0,15)]
print("source_list:\t", source_list)
bh2 = BinaryHeap()
bh2.build_heap(source_list)
print("from_list:\t", bh2.internal_list[1:])

source_list = [x for x in range(1,16)]
print("source_list:\t", source_list)
bh3 = BinaryHeap()
bh3.build_heap(source_list)
print("from_list:\t", bh3.internal_list[1:])
print_bh(bh3)
