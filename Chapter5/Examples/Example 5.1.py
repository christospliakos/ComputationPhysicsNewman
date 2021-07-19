import math
import numpy as np


def f(x):
    return (x ** 4) - (2 * x) + 1


a = 0
b = 2
N = 10
h = (b - a) / N
integral = (0.5 * f(a)) + (0.5 * f(b))

for i in range(1, N):
    integral += f(a + (i * h))

integral = h * integral
print("Integral is equal to: ", integral)