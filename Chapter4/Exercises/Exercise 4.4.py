import math
import datetime


begin = datetime.datetime.now()
N = 1500000
h = 2 / N

area = 0
for i in range(N):
    x_k = -1 + (h * i)
    y_k = math.sqrt(1 - (x_k ** 2))
    area += h * y_k

print("approximation value: ", math.pi / 2)
print("accurate value: ", area)
print("difference: ", abs((math.pi / 2) - area))
print("time run: ", datetime.datetime.now() - begin)