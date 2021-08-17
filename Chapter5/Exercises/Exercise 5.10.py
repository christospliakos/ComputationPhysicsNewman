from Chapter5.DataFiles.gaussxw import gaussxw
from Chapter5.IntegrationMethods import GaussianQuad
import numpy as np
import matplotlib.pyplot as plt


def f(x, a_):
    return 1 / (np.sqrt((a_ ** 4) - (x ** 4)))


a = np.linspace(0, 2.0, 100)
period = np.empty(a.shape)
m = 1
N = 20

# Gaussian calcs
gauss_integration = GaussianQuad(N)
x, w = gauss_integration.x, gauss_integration.w

for i in range(len(a)):
    s = gauss_integration.integrate(lambda x: f(x, a[i]), 0, a[i])

    period[i] = np.sqrt(8 * m) * s


plt.plot(a, period)
plt.title('Amplitude vs period')
plt.ylabel("Period T")
plt.xlabel("Amplitude")
plt.show()
