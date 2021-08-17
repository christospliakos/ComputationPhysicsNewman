import numpy as np


class GaussElim:

    def __init__(self, A, v):
        self.A = A
        self.v = v
        self.N = len(self.v)
        self.solution = np.empty(self.N, float)

    def solve_x(self):
        self.elimination()
        self.backsubstitution()
        return self.solution

    def elimination(self):
        for m in range(self.N):

            # Divide by the diagonal element
            div = self.A[m, m]
            self.A[m, :] /= div
            self.v[m] /= div

            # Now subtrack from the lower rows
            for i in range(m + 1, self.N):
                mult = self.A[i, m]
                self.A[i, :] -= mult * self.A[m, :]
                self.v[i] -= mult * self.v[m]

    def backsubstitution(self):
        for m in range(self.N - 1, -1, -1):
            self.solution[m] = self.v[m]
            for i in range(m + 1, self.N):
                self.solution[m] = self.solution[m] - self.A[m, i] * self.solution[i]
