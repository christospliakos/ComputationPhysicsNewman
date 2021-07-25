import math
import datetime


begin = datetime.datetime.now()
terms = 100000000
beta = 1 / 100
S = 0.0
Z = 0.0
for n in range(terms):
    E = n + 0.5
    weight = math.exp(-beta * E)
    S += weight * E
    Z += weight

print(S / Z)
print(datetime.datetime.now() - begin)