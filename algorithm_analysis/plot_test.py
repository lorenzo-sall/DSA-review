####
# A remainder of basic pyplot functions for quick plotting
#

import matplotlib.pyplot as plt
import numpy as np

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# Returns num evenly spaced samples, calculated over the interval [start, stop]
x = np.linspace(0, 10, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.plot(x, 2**x, label='exponential')

# scatter plot with red circles markers (same size)
plt.plot([1, 2, 3], [100, 300, 600], 'ro', label='scatter')

plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()

plt.show()
