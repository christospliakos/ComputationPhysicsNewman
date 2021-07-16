from vpython import sphere, vector, color
import numpy as np
import matplotlib.pyplot as plt


def exercise_a():
    L = 6
    R = 0.3
    for i in range(-L, L + 1, 2):
        for j in range(-L, L + 1, 2):
            for k in range(-L, L + 1, 2):
                sphere(pos=vector(i, j, k), radius=R, color=color.red)

    for i in range(-L + 1, L, 2):
        for j in range(-L + 1, L, 2):
            for k in range(-L + 1, L, 2):
                sphere(pos=vector(i, j, k), radius=R * 2, color=color.cyan)


def exercise_b():
    L = 2
    R = 0.2

    for i in range(0, L + 2, 2):
        for j in range(0, L + 2, 2):
            for k in range(0, L + 2, 2):
                sphere(pos=vector(i, j, k), radius=R, color=color.cyan)

                if i + 1 < L and j + 1 < L:
                    sphere(pos=vector(i + 1, j + 1, k), radius=R, color=color.white)

                if k + 1 < L and j + 1 < L:
                    sphere(pos=vector(i, j + 1, k + 1), radius=R, color=color.white)

                if k + 1 < L and i + 1 < L:
                    sphere(pos=vector(i + 1, j, k + 1), radius=R, color=color.white)


exercise_b()
