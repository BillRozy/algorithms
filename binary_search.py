def binary_search(what, source):
    start = 0
    end = len(source) - 1
    while start <= end:
        middle = (start + end) // 2
        if source[middle] == what:
            return middle
        elif source[middle] > what:
            end = middle - 1
        elif source[middle] < what:
            start = middle + 1
    return -1



def main():
    n, aNs = input().split(' ', 1)
    k, bKs = input().split(' ', 1)
    n = int(n)
    aNs = list(map(int, aNs.split(' ')))
    k = int(k)
    bKs = list(map(int, bKs.split(' ')))
    indexes = []
    for i in range(0, k):
        found = binary_search(bKs[i], aNs)
        indexes.append(found + 1 if found != -1 else -1)
    print(*indexes)


def test():
    aNs = [1, 5, 8, 12, 13]
    bKs = [8, 1, 23, 1, 11]
    answer = [3, 1, -1, 1, -1]
    for i in range(1, 5):
        found = binary_search(bKs[i], aNs)
        assert answer[i] == found + 1 if found != -1 else -1

def test2():
    aNs = [12, 4, 11, 23]
    bKs = [28, 12, 23, 11]
    answer = [-1, 1, 4, 3]
    for i in range(0, 4):
        found = binary_search(bKs[i], aNs)
        assert answer[i] == found + 1 if found != -1 else -1

if __name__ == '__main__':
    main()
    # test()
    # test2()
   
        