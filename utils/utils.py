def compare_with_none(x, y, func):
    if x is None and y is None:
        return None
    elif x is None and y is not None:
        return y
    elif x is not None and y is None:
        return x
    return func(x, y)


def max_with_none(x, y):
    return compare_with_none(x, y, max)


def min_with_none(x, y):
    return compare_with_none(x, y, min)


def get_digits(num):
    if num == 0:
        return 1
    num = abs(num)
    digits = 0
    while num:
        digits += 1
        num //= 10
    return digits
