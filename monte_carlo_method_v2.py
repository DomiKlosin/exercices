import random
import math
import numpy as np
import matplotlib.pyplot as plt

ns = [1000, 10000, 100000, 1000000, 10000000]
pi_values = []
pi_values_am = []
pi = math.pi

for n in ns:
    pi_values_n = []
    po = 0
    p = 0
    for i in range(0, n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        d = x**2 + y**2
        if d < 1:
            po += 1
            p += 1
        else:
            p += 1
        value_pi = 4 * (po / p)
        pi_values_n.append(value_pi)
    pi_values.append(pi_values_n)
    pi_values_am.append(np.mean(pi_values_n))

plt.scatter(ns, pi_values_am, color='red')
plt.xscale('log')
plt.xlabel('Number of iterations of π value')
plt.ylabel('π value')
plt.show()
