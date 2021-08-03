from Chapter5.DataFiles.gaussxw import gaussxw
from Chapter5.IntegrationMethods import GaussianQuad
import numpy as np
import matplotlib.pyplot as plt


def C(t):
    return np.cos(0.5 * np.pi * (t ** 2))


def S(t):
    return np.sin(0.5 * np.pi * (t ** 2))


x_dim = np.linspace(-5, 5, 100)
length = 1      # meter
z = 3           # point
N = 50         # sample points
I_list = []
u = x_dim * np.sqrt(2 / (length * z))

gauss_integration = GaussianQuad(N)
t, w = gauss_integration.x, gauss_integration.w

for i in range(len(x_dim)):
    C_integral = gauss_integration.integrate(C, 0, u[i])
    S_integral = gauss_integration.integrate(S, 0, u[i])

    intensity = (1 / 8) * (((2 * C_integral + 1) ** 2) + ((2 * S_integral + 1) ** 2))
    I_list.append(intensity)


plt.plot(x_dim, I_list)
plt.xlabel("X dimensions")
plt.ylabel("Intensity")
plt.show()