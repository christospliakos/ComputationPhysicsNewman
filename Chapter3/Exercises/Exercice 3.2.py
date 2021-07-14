import numpy as np
import matplotlib.pyplot as plt


def deltoid(theta_min, theta_max):
    theta = np.linspace(theta_min, theta_max, 100)
    print(theta)
    x = (2 * np.cos(theta)) + (np.cos(2 * theta))
    y = (2 * np.sin(theta)) - (np.sin(2 * theta))

    plt.axhline(y=0, xmin=min(x), xmax=max(x), color='k')
    plt.axvline(x=0, ymin=min(y), ymax=max(y), color='k')
    plt.plot(x, y, color='r')


def galilean_spiral(theta_min, theta_max):
    theta = np.linspace(theta_min, theta_max, 1000)
    r = theta ** 2
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.axhline(y=0, xmin=min(x), xmax=max(x), color='k')
    plt.axvline(x=0, ymin=min(y), ymax=max(y), color='k')
    plt.plot(x, y, color='r')


def fey_function(theta_min, theta_max):
    theta = np.linspace(theta_min, theta_max, 10000)
    r = np.exp(np.cos(theta)) - (2 * np.cos(4 * theta)) + ((np.sin(theta / 12)) ** 5)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.axhline(y=0, xmin=min(x), xmax=max(x), color='k')
    plt.axvline(x=0, ymin=min(y), ymax=max(y), color='k')
    plt.plot(x, y, color='r')


# deltoid(0, 2 * np.pi)
# galilean_spiral(0, 10 * np.pi)
fey_function(0, 24 * np.pi)
plt.show()