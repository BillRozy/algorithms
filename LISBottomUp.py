def LIS(array):
    sizes = [1 for i in array]
    for index in range(0, len(array)):
        if index == 0:
            continue
        for j in range(0, index):
            if array[index] % array[j] == 0 and \
               sizes[j] + 1 > sizes[index]:
               sizes[index] = sizes[j] + 1
    ans = 0
    for i in range(0, len(array)):
        ans = max(ans, sizes[i])
    print(sizes)
    return ans
    



def main():
    n = int(input())                             # 1 <= n <= 10_3
    An = list(map(int, input().split(' ')))      # <= 2 * 10_9
    print(LIS(An))

def test():
    n = 4
    An = [3, 6, 7, 12]
    assert LIS(An) == 3
    assert LIS([]) == 0
    assert LIS([1]) == 1
    assert LIS([1, 4, 4, 6, 7, 9, 12, 14, 14, 15,
                17, 20, 22, 24, 24, 27, 30, 30]) == 6

if __name__ == '__main__':
    test() 