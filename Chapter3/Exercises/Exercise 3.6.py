import numpy as np
import matplotlib.pyplot as plt
import datetime


begin_time = datetime.datetime.now()
r = np.arange(1, 4, 0.01)
x = np.ones(r.shape) * 0.5

for i in range(1000):
    x = r * x * (1 - x)
    plt.scatter(r, x, marker='.', color='k')


print("Execution time: ", datetime.datetime.now() - begin_time)
plt.xlabel('r')
plt.ylabel('x')
plt.title("Feigenbaum plot for r (1, 4, 0.01)")
plt.show()
