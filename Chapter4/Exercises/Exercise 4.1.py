import math

"""
    Function to calculate the factorial of x.
    If we will use float numbers, factorial of x will yield infinity.
    Instead, integer numbers can be stored regularly.
    
    Float number have an upper limit of 10 ** 308
    """


def factorial(x):
    if x == 1:
        return float(1)
    return float(x) * float(factorial(x - 1))


y = 200
print(factorial(y))
print(math.factorial(y))
