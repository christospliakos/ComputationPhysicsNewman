from Chapter5.DataFiles.gaussxw import gaussxw
from Chapter5.IntegrationMethods import GaussianQuad
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import datetime


time_now = datetime.datetime.now()
###############################################################################
# part a
###############################################################################


def H(n, x):
    if n == 0:
        return 1
    if n == 1:
        return 2 * x
    return (2 * x * H(n - 1, x)) - (2 * n * H(n - 2, x))


def psi(n, x):
    nominator = 1 * np.exp((-x ** 2) / 2) * H(n, x)
    denominator = np.sqrt((2 ** n) * math.factorial(n) * np.sqrt(np.pi))
    return nominator / denominator


x_range = np.linspace(-4, 4, 100)
plt.figure()
for n_ in range(0, 4):
    psi_list = []
    for x_ in x_range:
        psi_list.append(psi(n_, x_))

    plt.plot(x_range, psi_list, label=f'n={n_}')

plt.legend()


###############################################################################
# part b
###############################################################################
plt.figure()
psi_list_new = []
x_range2 = np.linspace(-10, 10, 100)
for x_ in x_range2:
    psi_list_new.append(psi(30, x_))

plt.plot(x_range2, psi_list_new, label=f'n=30')
plt.legend()
time_after = datetime.datetime.now()
print("Time for n=30: ", time_after - time_now)
plt.show()