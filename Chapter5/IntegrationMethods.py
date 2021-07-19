import math
import numpy as np


def trapezoidal_rule(f, a, b, N):
    h = (b - a) / N
    sum_ = (0.5 * f(a)) + (0.5 * f(b))

    for i in range(1, N):
        sum_ += f(a + (i * h))

    return h * sum_


def simpsons_rule(f, a, b, N):
    h = (b - a) / N
    sum_ = f(a) + f(b)

    odd_sum = 0
    for i in range(1, N, 2):
        odd_sum += f(a + (i * h))

    even_sum = 0
    for i in range(2, N - 1, 2):
        even_sum += f(a + (i * h))

    sum_ = (1 / 3) * h * (sum_ + (4 * odd_sum) + (2 * even_sum))
    return sum_

