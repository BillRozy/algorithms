import numpy as np

test_data = [2, 3, 9, 2, 9]

def counted_sort(array):
    size = len(array)
    digits = [0 for i in range(0, 11)]
    indexes = [0 for i in range(0, 11)]
    numbers = [0 for i in range(0, size)]
    for digit in array:
        digits[digit] += 1
    last_available_index = size - 1
    i = len(digits) - 1
    while i >= 0:
        if digits[i] > 0:
            indexes[i] = last_available_index
            last_available_index -= digits[i]
        i -= 1
    n = size - 1
    while n >= 0:
        index = indexes[array[n]]
        numbers[index] = array[n]
        indexes[array[n]] -= 1
        n -= 1
    return numbers

def test():
    assert np.array_equal(counted_sort(test_data), sorted(test_data))

def main():
    n = int(input())
    data = list(map(int, input().split(' ')))
    print(counted_sort(test_data))

main()