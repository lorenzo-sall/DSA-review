# Testing the performance of different methods for creating and growing a list

import timeit
from timeit import Timer
import matplotlib.pyplot as plt

k = 1000
t1_time = []
t2_time = []
t3_time = []
t4_time = []

# DEFINING THE FOUR METHODS WE ARE TESTING

# method 1: concatenation
def test1(k):
    l = []
    for i in range(k):
        l = l + [i]

# method 2: append()
def test2(k):
    l = []
    for i in range(k):
        l.append(i)

# method 3: list comprehension
def test3(k):
    l = [i for i in range(k)]

# method 4: list contructor
def test4(k):
    l = list(range(k))

# TEST AND TIME

for k in range(1000,10001,1000):
    print(f'####### {k} #######')

    t1 = Timer('test1(k)', 'from __main__ import test1; from __main__ import k')
    t1_time.append(t1.timeit(number=1000))
    print(f'concatenation:\t {t1_time[k//1000-1]} ms')

    t2 = Timer('test2(k)', 'from __main__ import test2; from __main__ import k')
    t2_time.append(t2.timeit(number=1000))
    print(f'append:\t\t {t2_time[k//1000-1]} ms')

    t3 = Timer('test3(k)', 'from __main__ import test3; from __main__ import k')
    t3_time.append(t3.timeit(number=1000))
    print(f'comprehension:\t {t3_time[k//1000-1]} ms')

    t4 = Timer('test4(k)', 'from __main__ import test4; from __main__ import k')
    t4_time.append(t4.timeit(number=1000))
    print(f'contructor:\t {t4_time[k//1000-1]} ms')

# PLOT THE RESULTS

plt.plot(range(1000,10001,1000), t1_time, 'r', label='t1')
plt.plot(range(1000,10001,1000), t2_time, 'g', label='t2')
plt.plot(range(1000,10001,1000), t3_time, 'b', label='t3')
plt.plot(range(1000,10001,1000), t4_time, 'y', label='t4')
plt.legend()
plt.show()
