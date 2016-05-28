import numpy


def fibonacci_log_n(n):
    mat = numpy.matrix([[1, 1], [1, 0]])
    return mat ** n
