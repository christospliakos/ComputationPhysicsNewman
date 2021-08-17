from Chapter5.DataFiles.gaussxw import gaussxw
from Chapter5.IntegrationMethods import trapezoidal_rule, simpsons_rule, romberg_integration
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return ((x ** 4) * np.exp(x)) / ((np.exp(x) - 1) ** 2)


def cv(T):
    rho = 6.022E28      # density
    V = 1000E-6         # m3
    theta = 428         # K
    k = 1.38064E-23     # Boltzman

    # Sample points
    N = 50
    a = 0
    b = theta / T

    x, w = gaussxw(N)
    xp = (0.5 * (b - a) * x) + (0.5 * (b - a))
    wp = 0.5 * (b - a) * w

    # Integral computation
    s = 0.0
    for j in range(N):
        s += wp[j] * f(xp[j])

    return s * (9 * V * rho * k * ((T / theta) ** 3))


T = np.linspace(5, 500, 1000)
capacity = np.empty(T.shape)
for i in range(T.shape[0]):
    capacity[i] = cv(T[i])

plt.plot(T, capacity)
plt.show()
