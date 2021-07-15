# Testing the performance of pop() vs. pop(0)
# we should see that popping the last item of an array is O(1), while calling pop on the
# 1st item (pop(0)) is O(n)
# we will test this on lists of increasing size, with a size big enough to avoid that popping
# an item affects the performance significantly

import timeit
from timeit import Timer
import matplotlib.pyplot as plt

tpop_time = []
tpop0_time = []

for k in range(100000,10000001,100000):
    l = list(range(k))
    print("1", k)
    t1 = Timer('l.pop()', 'from __main__ import l')
    tpop_time.append(t1.timeit(number=100))

for k in range(100000,10000001,100000):
    l = list(range(k))
    print("2", k)
    t2 = Timer('l.pop(0)', 'from __main__ import l')
    tpop0_time.append(t2.timeit(number=100))

# PLOT THE RESULTS

plt.plot(range(1000,100001,1000), tpop_time, 'r.', label='pop()')
plt.plot(range(1000,100001,1000), tpop0_time, 'g.', label='pop(0)')
plt.legend()
plt.show()
