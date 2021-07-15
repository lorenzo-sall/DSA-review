#####
# Benchmark test of the execution time of two functions calculating
#  the sum of the first n natural numbers
#

import time
import matplotlib.pyplot as plt

time_data_iter = []
time_data_formula = []

# Iterative method for the sum of the first n natural numbers
def sum_to_n_iterative(n):
    start_time = time.time()

    sum = 0
    for i in range(1, n + 1):
        sum = sum + i

    end_time = time.time()

    return sum, end_time - start_time

# Sum of the first n natural numbers with the formula
def sum_to_n_formula(n):
    start_time = time.time()

    sum = (n * (n + 1))/2

    end_time = time.time()

    return sum, end_time - start_time

# Test the functions and fill the data arrays
for n in range(1, 5000):
    time_data_iter.append(sum_to_n_iterative(n)[1])
    time_data_formula.append(sum_to_n_formula(n)[1])

# Plot the data
plt.plot(range(1, 5000), time_data_iter, 'r,', label='iterative (red)')
plt.plot(range(1, 5000), time_data_formula, 'b,', label='formula (blue)')
plt.legend()
plt.show()
