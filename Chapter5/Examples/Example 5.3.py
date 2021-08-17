from Chapter5.DataFiles.gaussxw import gaussxw
from Chapter5.IntegrationMethods import GaussianQuad
import numpy as np
import matplotlib.pyplot as plt


def f(z):
    return np.exp((-z ** 2) / (1 - z) ** 2) / (1 - z) ** 2


N = 50
a = 0.0
b = 1.0
gauss = GaussianQuad(N)
x, w = gauss.x, gauss.w
integral = gauss.integrate(f, a, b)
print(integral)