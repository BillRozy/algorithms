from sys import stdin
from collections import deque

def les43(number):
    additors = []
    last_additor = 0
    summa = 0
    while summa != number:
        last_additor += 1
        if additors and summa + last_additor > number:
            additors[-1] = number - (summa - additors[-1])
            summa += number - summa
        else:
            additors.append(last_additor)
            summa += last_additor
    return [len(additors), additors]


if __name__ == '__main__':
    count, numbers = les43(int(stdin.readline()))
    print(count)
    print(*numbers)
