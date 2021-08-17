import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return 1 + (0.5 * math.tanh(2 * x))


x_range = np.linspace(-2, 2, 100)
h = 0.01
derivatives = []
real_der = []
for x_ in x_range:
    der = (f(x_ + (h / 2)) - f(x_ - (h / 2))) / h
    anal_der = (1 / math.cosh(2 * x_)) ** 2
    real_der.append(anal_der)
    derivatives.append(der)

plt.plot(x_range, real_der, linestyle='-')
plt.plot(x_range, derivatives, linestyle='-.')

plt.show()