import math
import matplotlib.pyplot as plt
import numpy as np
from Chapter5.IntegrationMethods import trapezoidal_rule, simpsons_rule


a = 0
b = np.pi
N = 1000
x_series = np.linspace(0, 20, N)

# ----------------------------------------------------- #
#                   Part a
# ----------------------------------------------------- #

J_values = {
    "J_0_values": [np.zeros(x_series.shape), 'r'],
    "J_1_values": [np.zeros(x_series.shape), 'g'],
    "J_2_values": [np.zeros(x_series.shape), 'b']
}

for i, x in enumerate(x_series):
    for m in [0, 1, 2]:
        value = simpsons_rule(lambda theta: np.cos((m  * theta) - (x * np.sin(theta))), a, b, N)
        J_values[f'J_{m}_values'][0][i] = (1 / np.pi) * value

# for item, value in J_values.items():
#     plt.plot(x_series, value[0], color=value[1], label=item)
#
# plt.axhline(y=0, xmin=0, xmax=b, color='k')
# plt.legend()
# plt.show()

# ----------------------------------------------------- #
#                   Part b
# ----------------------------------------------------- #
l_ = 0.5  # light source
k = (2 * np.pi) / l_
r = np.linspace(0, 1, N)
I = (J_values['J_1_values'])
