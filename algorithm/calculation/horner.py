"""
### 霍纳法则

> 用于快速计算多项式

#### 原理:


"""


def horner(seq, base):
    _sum = 0
    if isinstance(seq, str):
        handle = ord
    elif isinstance(seq, list):
        handle = int
    elif isinstance(seq, int):
        seq = [seq]
        handle = int
    else:
        handle = lambda x: x
    for i in range(len(seq)):
        _sum = _sum * base + handle(seq[i])
    return _sum


if __name__ == '__main__':
    seq = [1, 2, 3]
    base = 32
    # example : k[i] * ( base ^ (seq.size - 1 - i))
    print(horner(seq, base))
