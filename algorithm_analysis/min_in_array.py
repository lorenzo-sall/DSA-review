#####
# From 'Problem Solving with Algorithms and Data Structures, Release 3.0'
# Self check activity from chapter 2.2.1
#
'''
Write two Python functions to find the minimum number in a list. The first function should
compare each number to every other number on the list. O(n**2). The second function should be
linear O(n).
'''

import time
import matplotlib.pyplot as plt
import numpy as np

time_data_1 = []
time_data_2 = []
time_data_3 = []

# A useless loop is added just to have O(n**2) as required by the exercise
# Find minimum value in array by comparing each value with each value
def min_in_list_1(l):
    min = l[0]
    start_time = time.time()

    for j in l:
        for i in l:
            if i < min:
                min = i

    end_time = time.time()
    return min, end_time - start_time

# Simple solution for the minimum value of an array ( O(n) )
#
def min_in_list_2(l):
    min = l[0]
    start_time = time.time()

    for i in range(1,len(l)):
        if l[i] < min:
            min = l[i]

    end_time = time.time()
    return min, end_time - start_time

# Testing
def min_in_list_recur(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        if l[0] < l[1]:
            return l[0]
        else:
            return l[1]
    else:
        a = min_in_list_recur(l[:len(l)//2])
        b = min_in_list_recur(l[len(l)//2:])
        if a < b:
            return a
        else:
            return b

def min_in_list_3(l):
    min = l[0]
    start_time = time.time()

    min = min_in_list_recur(l)

    end_time = time.time()
    return min, end_time - start_time

# Generating arrays of increasing lenght and calling the functions
for i in range(2, 1000000, 100000):
    rand_array = np.random.randint(1, 100000, i)
    #print(rand_array)
    #a = min_in_list_1(rand_array)
    b = min_in_list_2(rand_array)
    c = min_in_list_3(rand_array)
    #time_data_1.append(a[1])
    #print(len(rand_array) , ' #1 ', a[0], ' -> ', a[1])
    time_data_2.append(b[1])
    print(len(rand_array) , ' #2 ', b[0], ' -> ', b[1])
    time_data_3.append(c[1])
    print(len(rand_array) , ' #3 ', c[0], ' -> ', c[1])

#plt.plot(range(2, 10000, 1000), time_data_1, 'ro', label='method 1 (red)')
plt.plot(range(2, 1000000, 100000), time_data_2, 'bo', label='method 2 (blue)')
plt.plot(range(2, 1000000, 100000), time_data_3, 'go', label='method 3 (green)')
plt.legend()
plt.show()
