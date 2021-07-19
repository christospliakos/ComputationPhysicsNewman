import math
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('../DataFiles/velocities.txt', usecols=[0, 1], unpack=True)

a = data[0, 0]
b = data[0, -1]
N  = len(data[1, :])
h = (b - 1) / N

integral = (0.5 * data[1, 0]) + (0.5 * data[1, -1])
for i in range(1, N):
    integral += data[1, i]

integral = h * integral
distance_traveled = np.linspace(0, integral, N)
plt.plot(data[0, :], data[1, :], label='Velocity')

plt.plot(data[0, :], distance_traveled, color='r', label='Distance Traveled')

print("integral: ", integral)

plt.legend()
plt.show()