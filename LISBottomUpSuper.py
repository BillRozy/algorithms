import numpy as np

def lds(array):
    sizes = [1 for i in array]
    for index in range(0, len(array)):
        if index == 0:
            continue
        for j in range(0, index):
            if array[index] <= array[j] == 0 and \
               sizes[j] + 1 > sizes[index]:
               sizes[index] = sizes[j] + 1
    ans = 0
    for i in range(0, len(array)):
        ans = max(ans, sizes[i])
    print(sizes)
    return ans
    

def main():
    n = int(input())                             # 1 <= n <= 10_5
    An = list(map(int, input().split(' ')))      # <= 10_9
    print(lds(An))

def test():
    size, seq = lds([5, 3, 4, 4, 2])
    assert size == 4
    assert np.array_equal(seq, [1, 3, 4, 5])

if __name__ == '__main__':
    test() 