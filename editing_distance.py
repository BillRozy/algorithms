def ed(first_arr, second_arr):
    n = len(first_arr)
    m = len(second_arr)
    d = [[i for i in range(0, n + 1)], *[[j, *[0 for h in range(0, n)]] for j in range(1, m + 1)]]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + (1 if first_arr[j - 1] != second_arr[i - 1] else 0)
            )
    return d[m][n]


def test():
    assert ed('ganimed', 'ima') == 5
    assert ed('', '') == 0
    assert ed('a', 'a') == 0
    assert ed('ab', 'ab') == 0
    assert ed('short', 'ports') == 3


def main():
    print(ed(input(), input()))

if __name__ == '__main__':
    test()