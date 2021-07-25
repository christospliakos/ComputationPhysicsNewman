import numpy as np
import matplotlib.pyplot as plt

wavelength = 5.0  # lambda [cm]
k = 2 * np.pi / wavelength  # wavevector
xi0 = 1.0                # Amplitude of waves
separation = 20.0        # Separation of the centers in cm
side = 100.0             # Size of the square in cm
points = 500             # Number of grid points along each side
spacing = side / points  # Spacing of points in cm

# Calculate the positions of the centers of the circles
x1 = side / 2 + separation / 2
y1 = side / 2
x2 = side / 2 - separation / 2
y2 = side / 2

# Make an array to store the heights
xi = np.empty([points, points], float)

for i in range(points):
    y = spacing * i
    for j in range(points):
        x = spacing * j
        r1 = np.sqrt(((x - x1) ** 2) + ((y - y1) ** 2))
        r2 = np.sqrt(((x - x2) ** 2) + ((y - y2) ** 2))
        xi[i, j] = (xi0 * np.sin(k * r1)) + (xi0 * np.sin(k * r2))

# Make the plot
plt.imshow(xi, origin='lower', extent=[0, side, 0, side])
plt.gray()
plt.show()