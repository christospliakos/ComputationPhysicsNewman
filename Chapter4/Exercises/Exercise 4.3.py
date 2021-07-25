import math
import numpy as np


def f(x):
    return x * (x - 1)


def lim(x, d_x):
    return (f(x + d_x) - f(x)) / d_x


d = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]
for d_ in d:
    print(f"d_x value is: {d_} and the limit: {lim(1, d_)}")

