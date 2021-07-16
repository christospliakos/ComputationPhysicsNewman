from vpython import sphere, vector, color, rate
import numpy as np
import matplotlib.pyplot as plt


s = sphere(pos=vector(1, 0, 0), radius=0.1)
for theta in np.arange(0, 10*np.pi, 0.1):
    rate(30)
    x = np.cos(theta)
    y = np.cos(theta)
    s.pos = vector(x, y, 0)
