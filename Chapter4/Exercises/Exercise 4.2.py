import math


def quadratic(a, b, c):
    x1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    return x1, x2


def quadratic_alternative(a, b, c):
    x1 = (2 * c) / (-b - math.sqrt((b ** 2) - (4 * a * c)))
    x2 = (2 * c) / (-b + math.sqrt((b ** 2) - (4 * a * c)))
    return x1, x2


def quadratic_correction(a, b, c):
    """
    The problem with both methods is that the computer only represents 10^16
    digits of any number for operations; when you are substracting numbers,
    the computer truncates any trailing digits after this limit and an accuracy
    that used to be of 10^16 could now be as low as two digits.
    by combining both methods, one can get more accurate answers.

    This explanation is derived from the information given in pages 131-32 from
    the book.
    """
    x1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    x2 = (2 * c) / (-b + math.sqrt((b ** 2) - (4 * a * c)))
    return x1, x2


print(quadratic(0.001, 1000, 0.001))
print(quadratic_alternative(0.001, 1000, 0.001))
print(quadratic_correction(0.001, 1000, 0.001))