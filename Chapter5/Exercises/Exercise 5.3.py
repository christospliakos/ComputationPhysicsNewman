import math

import matplotlib.pyplot as plt
import numpy as np
from Chapter5.IntegrationMethods import trapezoidal_rule, simpsons_rule


def f(x):
    return math.exp(-x ** 2)


a, b = 0, 3
x_series = np.arange(a, b, 0.1)
N = 100

simp_sum = np.zeros(x_series.shape)
trap_sum = np.zeros(x_series.shape)
error = np.zeros(x_series.shape)
for i, x in enumerate(x_series):
    simp_sum[i] = simpsons_rule(f, a, x, N)
    trap_sum[i] = trapezoidal_rule(f, a, x, N)
    error[i] = simp_sum[i] - trap_sum[i]


plt.title(f'Integral with {N} slices')
plt.plot(x_series, simp_sum, label='Simpsons Rule', color='r', linestyle='-.')
plt.plot(x_series, trap_sum, label='Trapezoidal Rule', color='k')
plt.plot(x_series, error, label='Error Simp - Trap', color='g')
plt.legend()
plt.xlabel('x')
plt.ylabel('Integral')
plt.show()