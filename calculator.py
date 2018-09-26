import numpy as np
from collections import deque

def calculate(end, start=1, memoize=None):
    memoize = memoize or [float('inf') for i in range(0, end + 1)]
    memoize[0] = 0
    memoize[1] = 0
    print(end, start)
    if start == end:
        print(memoize)
        return memoize[end]
    doubled = start * 2
    tripled = start * 3
    inced = start + 1
    if doubled <= end:
        memoize[doubled] = min(memoize[doubled], memoize[start] + 1)
        calculate(end, doubled, memoize)
    if tripled <= end:
        memoize[tripled] = min(memoize[tripled], memoize[start] + 1)
        calculate(end, tripled, memoize)
    if inced <= end:
        memoize[inced] = min(memoize[inced], memoize[start] + 1)
        calculate(end, inced, memoize)
    return memoize[end]

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

