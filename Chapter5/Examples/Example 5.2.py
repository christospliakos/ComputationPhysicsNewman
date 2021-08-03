from Chapter5.DataFiles.gaussxw import gaussxw
from Chapter5.IntegrationMethods import trapezoidal_rule, simpsons_rule, romberg_integration

"""
    Calculate the integral (x^4 - 2x + 1) from 0 to 2
    using only 3 points"""


def f(x):
    return x ** 4 - 2 * x + 1


N = 3
a = 0.0
b = 2.0

# Calculate the sample points and weights, then map them
# to the required integration domain
x, w = gaussxw(N)
xp = (0.5 * (b - a) * x) + (0.5 * (b - a))
wp = 0.5 * (b - a) * w

# Perform the integration
s = 0.0
for k in range(N):
    s += wp[k] * f(xp[k])

print(f"Integration using Gaussian Quadrature for {N} points: {s}")

trapz = trapezoidal_rule(f, a, b, N, approx_error=False)
simps = simpsons_rule(f, a, b, N, approx_error=False)

print(f"Integration using trapz rule for {N} points: {trapz}")
print(f"Integration using simpsons for {N} points: {simps}")
