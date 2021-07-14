import numpy as np
import matplotlib.pyplot as plt

# Hertzsprung - Russel diagram
T, magn = np.loadtxt('DataFiles/stars.txt', unpack=True)

plt.scatter(T, magn)
plt.xlim(13000, 0)
plt.ylim(20, -5)
plt.xlabel('Temperature')
plt.ylabel('Magnitude')
plt.title('Hertzsprung - Russel diagram')

plt.show()