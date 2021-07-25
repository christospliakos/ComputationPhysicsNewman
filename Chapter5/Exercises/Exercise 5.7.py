import math
import numpy as np
from Chapter5.IntegrationMethods import trapezoidal_rule, simpsons_rule, romberg_integration


def f(x):
    return np.sin(np.sqrt(100 * x)) ** 2


a, b = 0, 1
N = 2
acc = 1e-6
real_value = 0.45

error, steps = trapezoidal_rule(f, a, b, N, approx_error=False, adaptive=[True, acc])
error2, steps2 = simpsons_rule(f, a, b, N, approx_error=False, adaptive=[True, acc])
error3, steps3, R= romberg_integration(f, a, b, N, approx_error=False, adaptive=[True, acc, steps2])


print("\n#############Trapezoidal##################")
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

print("\n#############Romberg##################")
print(f"Final error that terminated the Romberg algorithm: {error3} and required"
      f" acurracy: {acc}. \nDifference: {error3 - acc}")
print(f"Amount of steps required: {steps3}")

estimate2 = simpsons_rule(f, a, b, steps)
print(f"Estimation with {steps3} steps: {R}. The difference from real value is:"
      f" {abs(real_value - R)}.")