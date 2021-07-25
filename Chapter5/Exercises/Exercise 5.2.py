def f(x):
    return (x ** 4) - (2 * x) + 1


a, b = 0, 2
N = 10
h = (b - a) / N
sum_ = f(a) + f(b)

odd_sum = 0
for i in range(1, N, 2):
    odd_sum += f(a + (i * h))

even_sum = 0
for i in range(2, N - 1, 2):
    even_sum += f(a + (i * h))

sum_ = (1 / 3) * h * (sum_ + (4 * odd_sum) + (2 * even_sum))
real_value = 4.4

print("Integral: ", sum_)
print("Fractional error: ", 100 * abs(real_value - sum_) / real_value, "%")