def power_bad(x, n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    return power(x, n // 2) * power(x, n - (n // 2))


def power(x, n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    return power(x, n // 2) ** 2 * power(x, n - (n // 2) * 2)
