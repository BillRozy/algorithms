from sys import stdin
from collections import deque

def les41(lines):
    result = []
    marked = set()
    l = sorted(lines, key=lambda x: x[1])
    i = 0
    while i < len(l):
        if i in marked: 
            i += 1
            continue
        cur = l[i][1]
        result.append(cur)
        j = i
        while j < len(l):
            if (l[j][0] <= cur and l[j][1] >= cur):
                marked.add(j)
            j += 1
        i += 1
    return [len(result), result]





if __name__ == '__main__':
    lines = []
    for i in range(int(stdin.readline())):
        lines.append(list(map(lambda x: int(x), stdin.readline().split(' '))))
    count, points = les41(lines)
    print(count)
    print(*points)
