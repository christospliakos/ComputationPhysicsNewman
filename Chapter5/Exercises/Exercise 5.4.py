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
l_ = 5e-7  # light source
k = (2 * np.pi) / l_
I = (J_values['J_1_values'])

side = 1e-6             # Size of the square in m
points = 250             # Number of grid points along each side
spacing = side / points  # Spacing of points in cm

# Calculate the positions of the centers of the circles
x1 = side / 2
y1 = side / 2

# Make an array to store the heights
xi = np.empty([points, points], float)

for i in range(points):
    y = spacing * i
    for j in range(points):
        x = spacing * j

        m = 1
        r1 = np.sqrt(((x - x1) ** 2) + ((y - y1) ** 2))
        value = (1 / np.pi) * simpsons_rule(lambda theta: np.cos((m  * theta) - ((k * r1) * np.sin(theta))), a, b, 100)

        xi[i, j] = (value / (k * r1)) ** 2

# Make the plot
plt.imshow(xi, origin='lower', extent=[0, side, 0, side], vmax=0.1)
plt.hot()
plt.show()