import types


def fun(i):
    if i == 1:
        yield 1
    yield fun(i - 1)


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g


print(tramp(fun, 10050000))
