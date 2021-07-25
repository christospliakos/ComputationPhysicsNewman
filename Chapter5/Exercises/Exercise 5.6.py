import math
import numpy as np
from Chapter5.IntegrationMethods import trapezoidal_rule, simpsons_rule


def f(x):
    return (x ** 4) - (2 * x) + 1


N   = 20  # slices
a   = 0
b   = 2

integral, error = trapezoidal_rule(f, a, b, N, approx_error=True)
integral2, error2 = simpsons_rule(f, a, b, N, approx_error=True)


print("Trapezoidal Rule: ")
print(f"Integral of f with {N} slices: {integral}")
print(f"Approximation error of trapezoidal rule with N1 = {int(N / 2)}"
      f" and N2 = {N} is: {abs(error)}")
print(f"Difference between integral with N = {N} slices and real value"
      f" of 4.4 is: {abs(4.4 - integral)}")

print("Simpsons Rule: ")
print(f"Integral of f with {N} slices: {integral2}")
print(f"Approximation error of Simpsons rule with N1 = {int(N / 2)}"
      f" and N2 = {N} is: {abs(error2)}")
print(f"Difference between integral with N = {N} slices and real value"
      f" of 4.4 is: {abs(4.4 - integral2)}")