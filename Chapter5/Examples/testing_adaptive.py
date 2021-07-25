import math
import numpy as np
from Chapter5.IntegrationMethods import trapezoidal_rule, simpsons_rule


def f(x):
    return (x ** 4) - (2 * x) + 1


a, b = 0, 1
N = 1
acc = 1e-10
real_value = 4.4

error, steps = trapezoidal_rule(f, a, b, N, approx_error=False, adaptive=[True, acc])
error2, steps2 = simpsons_rule(f, a, b, N, approx_error=False, adaptive=[True, acc])


print(f"Final error that terminated the trapezoidal algorithm: {error} and required"
      f" acurracy: {acc}. \nDifference: {error - acc}")
print(f"Amount of steps required: {steps}")

estimate = trapezoidal_rule(f, a, b, steps)
print(f"Estimation with {steps} steps: {estimate}. The difference from real value is:"
      f" {abs(real_value - estimate)}.")

print("\n#############Simpsons##################")
print(f"Final error that terminated the Simpsons algorithm: {error2} and required"
      f" acurracy: {acc}. \nDifference: {error2 - acc}")
print(f"Amount of steps required: {steps2}")

estimate2 = simpsons_rule(f, a, b, steps)
print(f"Estimation with {steps2} steps: {estimate2}. The difference from real value is:"
      f" {abs(real_value - estimate2)}.")