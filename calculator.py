import numpy as np
from collections import deque


def calculate(end):
    memoize = [float('inf') for i in range(0, end)]
    memoize[0] = 0
    trap = set()
    turn_numbers = set()
    turn_numbers.add(1)
    for i in range(1, end + 1):
        print('i', i)
        if memoize[end - 1] != float('inf'):
            print(trap)
            return memoize[end - 1]
        this_turn_numbers = set()
        for num in list(turn_numbers):
            # if memoize[num - 1] != float('inf'):
            #     continue
            doubled = num * 2
            tripled = num * 3
            inced = num + 1
            if doubled <= end and memoize[doubled - 1] == float('inf'):
                memoize[doubled - 1] = i
                this_turn_numbers.add(doubled)
            if tripled <= end and memoize[tripled - 1] == float('inf'):
                memoize[tripled - 1] = i
                this_turn_numbers.add(tripled)
            if inced <= end and memoize[inced - 1] == float('inf'):
                memoize[inced - 1] = i
                this_turn_numbers.add(inced)
        print('new numbers', this_turn_numbers)
        trap.add(max(list(this_turn_numbers)))
        turn_numbers = this_turn_numbers
        this_turn_numbers = set()
    print(memoize)
    print(trap)
    return memoize[end - 1]

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

