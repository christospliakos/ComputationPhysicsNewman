from Chapter5.DataFiles.gaussxw import gaussxw
from Chapter5.IntegrationMethods import GaussianQuad
import numpy as np
import matplotlib.pyplot as plt


def f(z):
    nominator = (z / (1 - z)) ** 3
    denominator = (np.exp(z / (1 - z)) - 1) * ((1 - z) ** 2)
    return nominator / denominator


# Constants
k = 1.38064852E-23
c = 299792458
h = 6.62607004E-34/(2 * np.pi)
T = 300

N = 100
a = 0.0
b = 1.0
gauss = GaussianQuad(N)
x, w = gauss.x, gauss.w
integral = gauss.integrate(f, a, b)
energy = (((k ** 4) * (T ** 4)) / (4 * (np.pi ** 2) * (c ** 2) * (h ** 3))) * integral
print("Energy W: ", energy)
print("Stefan Boltzmann constant computed: ", energy / (T ** 4))
print("Real Stefan constant: ", 5.670374419E-8)