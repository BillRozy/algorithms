# n - steps
# a1 ... an - prices
# step 1 | 2
# start from 0
# need find max sum
def max_steps_price_td(array, i, d=None):
    d = d or [float('inf') for i in range(0, i + 1)]
    if d[i] == float('inf'):
        if i == 0:
            d[i] = 0
        elif i == 1:
            d[i] = array[0]
        else:
            if_prev_optimal = max_steps_price_td(array, i - 1, d) + array[i - 1]
            if_prev_prev_optimal = max_steps_price_td(array, i - 2, d) + array[i - 1]
            d[i] = max(if_prev_optimal, if_prev_prev_optimal)
    return d[i]

def main():
    n = int(input())
    steps = list(map(int, input().split(' ')))
    print(max_steps_price_td(steps, n))

def test():
    assert max_steps_price_td([1, 2], 2) == 3
    assert max_steps_price_td([2, -1], 2) == 1
    assert max_steps_price_td([-1, 2, 1], 3) == 3
    assert max_steps_price_td([-2, 3, 1, 7, -5, 2], 6) == 13

main()