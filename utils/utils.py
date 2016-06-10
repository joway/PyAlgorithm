def max_with_none(x, y):
    if x is None and y is None:
        return None
    elif x is None and y is not None:
        return y
    elif x is not None and y is None:
        return x
    return max(x, y)


def min_with_none(x, y):
    if x is None and y is None:
        return None
    elif x is None and y is not None:
        return y
    elif x is not None and y is None:
        return x
    return min(x, y)
