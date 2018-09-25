def main():
    inp = lambda: list(map(int, input().split(' ')))
    W, n = inp()
    items = inp()
    print(knapsak(W, n, items, items))

def test():
    assert knapsak(10, 1, [20], [20]) == 0
    assert knapsak(1, 0, [], []) == 0
    assert knapsak(1, 1, [1], [1]) == 1
    assert knapsak(10, 3, [1, 4, 8], [1, 4, 8]) == 9

def knapsak(W, n, weights, costs):
    d = [[0 for ni in range(0, n + 1)] for w in range(0, W + 1)]
    for w in range(1, W + 1):
        for i in range(1, n + 1):
            d[w][i] = d[w][i - 1]
            if weights[i - 1] <= w:
                d[w][i] = max(
                    d[w][i],
                    d[w - weights[i - 1]][i - 1] + costs[i - 1]
                )
    return d[W][n]

if __name__ == '__main__':
    main()