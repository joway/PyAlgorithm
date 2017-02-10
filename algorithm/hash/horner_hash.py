from algorithm.calculation.horner import horner


def horner_hash(key, size):
    _BASE = 32
    return horner(key, _BASE) % size

if __name__ == '__main__':
    print(horner_hash('test', 10))
