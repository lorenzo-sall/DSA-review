#####
# From 'Problem Solving with Algorithms and Data Structures, Release 3.0'
# Self check activity from chapter 2.2.1
#
# Write two Python functions to find the minimum number in a list. The first function should
# compare each number to every other number on the list. O(n**2). The second function should be
# linear O(n).
# Added a counter for the number of comparisons and played with some delay to make the comparison
# function more expensive

import time
import matplotlib.pyplot as plt
import numpy as np

time_data_2 = []
time_data_3 = []
comparison_counter_2 = [0]
comparison_counter_3 = [0]

def comparison(a, b, count):
    #time.sleep(0.001)
    count[0] = count[0] + 1
    if a < b:
        return a
    else:
        return b
# Simple solution for the minimum value of an array ( O(n) )
#
def min_in_list_2(l):
    min = l[0]
    start_time = time.time()

    for i in range(1,len(l)):
        min = comparison(l[i], min, comparison_counter_2)

    end_time = time.time()
    return min, end_time - start_time

# Testing
def min_in_list_recur(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return comparison(l[0], l[1], comparison_counter_3)
    else:
        a = min_in_list_recur(l[:len(l)//2])
        b = min_in_list_recur(l[len(l)//2:])
        return comparison(a, b, comparison_counter_3)

def min_in_list_3(l):
    min = l[0]
    start_time = time.time()

    min = min_in_list_recur(l)

    end_time = time.time()
    return min, end_time - start_time

# Generating arrays of increasing lenght and calling the functions
for i in range(2, 10000, 1000):
    rand_array = np.random.randint(1, 100000, i)
    #print(rand_array)
    #a = min_in_list_1(rand_array)
    b = min_in_list_2(rand_array)
    c = min_in_list_3(rand_array)
    #time_data_1.append(a[1])
    #print(len(rand_array) , ' #1 ', a[0], ' -> ', a[1])
    time_data_2.append(b[1])
    print(len(rand_array) , ' #2 ', b[0], ' -> ', b[1], ' in ', comparison_counter_2, 'comp.')
    comparison_counter_2 = [0]
    time_data_3.append(c[1])
    print(len(rand_array) , ' #3 ', c[0], ' -> ', c[1], ' in ', comparison_counter_3, 'comp.')
    comparison_counter_3 = [0]

#plt.plot(range(2, 10000, 1000), time_data_1, 'ro', label='method 1 (red)')
plt.plot(range(2, 10000, 1000), time_data_2, 'bo', label='method 2 (blue)')
plt.plot(range(2, 10000, 1000), time_data_3, 'go', label='method 3 (green)')
plt.legend()
plt.show()
