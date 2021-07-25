from vpython import sphere, vector, color, rate
import numpy as np
import matplotlib.pyplot as plt


parameters = {
    "Mercury": [2440, 57.9, 88.0, color.red],
    "Venus": [6052, 108.2, 224.7, color.magenta],
    "Earth": [6371, 149.6, 365.3, color.blue],
    "Mars": [3386, 227.9, 687.0, color.orange],
    "Jupiter": [69173, 778.5, 4331.6, color.magenta],
    "Saturn": [57316, 1433.4, 10759.2, color.green],
    "Sun": [695500, 0, 0, color.yellow]
}
planets = np.empty(7, sphere)

i = 0
for planet, values in parameters.items():
    if planet == 'Sun':
        s = sphere(radius=values[0] * 0.1, pos=vector(0, 0, 0), color=values[3])
        planets[i] = s
    elif planet in ['Mercury', 'Mars', 'Earth', 'Venus']:
        sphere(radius=values[0] * 3, pos=vector(0, 1000 * values[1], 0), color=values[3])
    else:
        sphere(radius=values[0], pos=vector(0, 1000 * values[1], 0), color=values[3])
    i += 1

