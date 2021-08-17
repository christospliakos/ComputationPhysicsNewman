import math
import numpy as np
from Chapter5.DataFiles.gaussxw import gaussxw


def trapezoidal_rule(f, a, b, N, approx_error=False, adaptive=None):
    if adaptive is None:
        adaptive = [False, 0]
        accuracy = None
    else:
        accuracy = adaptive[1]
    if not approx_error and not adaptive[0]:
        h = (b - a) / N
        sum_ = (0.5 * f(a)) + (0.5 * f(b))

        for i in range(1, N):
            sum_ += f(a + (i * h))
        return h * sum_
    elif approx_error and not adaptive[0]:
        N1 = int(N / 2)
        N2 = N
        I1 = trapezoidal_rule(f, a, b, N1, approx_error=False)
        I2 = trapezoidal_rule(f, a, b, N2, approx_error=False)

        return [I2, (1 / 3) * (I2 - I1)]
    elif adaptive[0]:
        N1 = N
        error = np.inf
        integrals = []
        integrals.append(trapezoidal_rule(f, a, b, N1, approx_error=False, adaptive=None))

        c_ = 0
        while error > accuracy:
            N1 = 2 * N1
            h1 = ((b - a) / N1)
            n_range = np.arange(1, N1, 2)
            integrals.append((0.5 * integrals[c_]) + h1 * np.sum(f(a + n_range * h1)))
            error = abs((1 / 3) * (integrals[c_ + 1] - integrals[c_]))
            c_ += 1
        return error, N1


def simpsons_rule(f, a, b, N, approx_error=False, adaptive=None):
    if adaptive is None:
        adaptive = [False, 0]
        accuracy = None
    else:
        accuracy = adaptive[1]
    if not approx_error and not adaptive[0]:
        h = (b - a) / N
        sum_ = f(a) + f(b)

        odd_sum = 0
        for i in range(1, N, 2):
            odd_sum += f(a + (i * h))

        even_sum = 0
        for i in range(2, N - 1, 2):
            even_sum += f(a + (i * h))

        sum_ = (1 / 3) * h * (sum_ + (4 * odd_sum) + (2 * even_sum))
        return sum_
    elif approx_error and not adaptive[0]:
        N1 = int(N / 2)
        N2 = N
        I1 = simpsons_rule(f, a, b, N1, approx_error=False)
        I2 = simpsons_rule(f, a, b, N2, approx_error=False)

        return [I2, (1 / 15) * (I2 - I1)]
    elif adaptive[0]:
        N1 = N
        n_range_odd = np.arange(1, N1, 2)
        n_range_even = np.arange(2, N1 - 1, 2)
        h1 = ((b - a) / N1)
        error = np.inf
        integrals = []
        S = []
        T = []

        S.append((1 / 3) * (f(a) + f(b) + 2 * (np.sum(f(a + n_range_even * h1)))))
        T.append((2 / 3) * np.sum(f(a + n_range_odd * h1)))
        integrals.append(h1 * (S[0] + 2 * T[0]))

        c_ = 0
        while error > accuracy:
            N1 = 2 * N1
            h1 = ((b - a) / N1)
            n_range_odd = np.arange(1, N1, 2)
            n_range_even = np.arange(2, N1 - 1, 2)

            T.append((2 / 3) * np.sum(f(a + n_range_odd * h1)))
            S.append(S[c_] + T[c_])
            integrals.append(h1 * (S[c_ + 1] + 2 * T[c_ + 1]))
            error = abs((1 / 15) * (integrals[c_ + 1] - integrals[c_]))
            c_ += 1
        return error, N1


def romberg_integration(f, a, b, N, approx_error=False, adaptive=None):
    if adaptive is None:
        adaptive = [False, 0, 0]
        accuracy = None
    else:
        accuracy = adaptive[1]
        trapz_steps = adaptive[2]

    if adaptive[0]:
        error = np.inf
        N1 = N
        I = []
        R = np.zeros((trapz_steps, trapz_steps))

        I.append(trapezoidal_rule(f, a, b, N1))
        R[0][0] = I[0]
        N1 = 2 * N1
        I.append(trapezoidal_rule(f, a, b, N1))

        i = 1
        while error > accuracy:
            m = len(I)
            new_arr = np.zeros((1, trapz_steps))
            new_arr[0, 0] = I[-1]
            for j in range(1, m):
                new_arr[0, j] = new_arr[0, j - 1] + (1 / ((4 ** m) - 1)) * (new_arr[0, j - 1] - R[i - 1, j - 1])
                if j == m - 1:
                    error = abs((1 / ((4 ** m) - 1)) * (new_arr[0, j - 1] - R[i - 1, j - 1]))
            R[i, :] = new_arr

            N1 = 2 * N1
            I.append(trapezoidal_rule(f, a, b, N1))

            i += 1

        return error, N1 / 2, R[i - 1, len(I) - 2]


class GaussianQuad:

    def __init__(self, N):
        self.N = N
        self.x, self.w = gaussxw(N)

    def integrate(self, f, a, b):
        xp = (0.5 * (b - a) * self.x) + (0.5 * (b - a))
        wp = 0.5 * (b - a) * self.w

        integral = 0
        for j in range(self.N):
            integral += wp[j] * f(xp[j])

        return integral

