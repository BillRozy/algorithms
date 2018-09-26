import numpy as np
from collections import deque

def calculate(x, start=None, ops=0, memoize=None):
    start = start or 1
    memoize = memoize or [float('inf') for i in range(0, x + 1)]
    print(x, start, ops)
    if start > x:
        return float('inf')
    if memoize[start] != float('inf'):
        return memoize[start]
    if start * 2 <= x:
        memoize[start * 2] = min(memoize[start * 2], calculate(x, start * 2, ops + 1, memoize))
    if start * 3 <= x:
        memoize[start * 3] = min(memoize[start * 3], calculate(x, start * 3, ops + 1, memoize))
    if start + 1 <= x:
        memoize[start + 1] = min(memoize[start + 1], calculate(x, start + 1, ops + 1, memoize))
    memoize[start] = ops
    return memoize[x]

def test():
    ops = calculate(1)
    assert ops == 0
    ops = calculate(5)
    print(ops)
    assert ops == 3
    ops = calculate(96234)
    print(ops)
    assert ops == 14

def main():
    x = int(input())
    ops = calculate(x)
    print(ops)

main()

