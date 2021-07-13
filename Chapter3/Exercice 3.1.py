import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('DataFiles/sunspots.txt', usecols=[0, 1], unpack=True)


def amount_of_sunspots(a=None):
    if not a:
        a = -1
    plt.plot(data[0, :a], data[1, :a], color='b', label='Sunspots')
    plt.xlabel("Months")
    plt.ylabel("Sunspots")


def running_average(r, a):
    r_entries = []
    run_avg = []
    for i in range(a):
        r_entries.append(data[1, i])
        if len(r_entries) == r:
            run_avg.append(sum(r_entries) / r)
            r_entries.pop(0)

    plt.plot(run_avg, color='r', label='Running average')


amount_of_sunspots(3000)
running_average(5, 3000)
plt.legend()
plt.show()