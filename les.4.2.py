from sys import stdin
from collections import deque

def les42(items, volume):
    sum = 0
    l = sorted(items, key=lambda x: x[1]/(x[0] or 0.00001))
    for price, weight in l:
        if volume > weight:
            sum += price
            volume -= weight
            continue
        elif volume == weight:
            sum += price
            break
        else:
            sum += volume / weight * price
            break
    return sum





if __name__ == '__main__':
    count, volume = list(map(lambda x: int(x), stdin.readline().split(' ')))
    items = []
    for i in range(count):
        items.append(list(map(lambda x: int(x), stdin.readline().split(' '))))
    print(format(les42(items, volume), '.3f'))
