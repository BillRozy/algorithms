import numpy as np
from collections import deque

def calculate(x, start=None, accum=None):
    start = start or x
    accum = accum or deque()
    ops = 0
    accum.appendleft(start)
    if start == 1:
        return [ops, accum]
    if start < 1:
        ops = float('inf')
        return [ops, accum]
    if start % 3 == 0:
        [ops, accum] = calculate(x, int(start // 3), accum)
    elif start % 2 == 0 and ((start - 1) % 3) != 0:
        [ops, accum] = calculate(x, int(start // 2), accum)
    else:
        [ops, accum] = calculate(x, start - 1, accum)
    ops += 1
    return [ops, accum]

def test():
    [ops, accum] = calculate(1)
    assert ops == 0 and np.array_equal(list(accum), [1])
    [ops, accum] = calculate(5)
    print(ops, accum)
    assert ops == 3 and (np.array_equal(list(accum), [1, 2, 4, 5]) or np.array_equal(list(accum), [1, 3, 4, 5]))
    [ops, accum] = calculate(96234)
    print(ops, accum)
    assert ops == 14 and np.array_equal(list(accum), [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234 ])

def main():
    x = int(input())
    [ops, accum] = calculate(x)
    print(ops)
    print(*list(accum))

main()

