import numpy as np
import time

def median(array):
    first = (0, array[0])
    second = (len(array) // 2, array[len(array) // 2])
    third = (len(array) - 1, array[len(array) - 1])
    return sorted([first, second, third], key=lambda x: x[0])[1][0]

def partition(array):
    if len(array) > 2:
        target_index = median(array)
        target_el = array[target_index]
        j = target_index
        i = 0
        end = len(array)
        while i < end:
            if array[i] > target_el
            if array[i] < 
        while
    return 0


def quick_sort(array, start=0, end=None):
    end = end or len(array)
    print(start, end)
    while start < end:
        m = start + partition(array[start:end])
        time.sleep(0.2)
        print('array: ', array)
        print('selected: ', m, array[m])
        size_first = m - start
        size_second = end - m
        if size_first < size_second:
            quick_sort(array, start, m - 1)
            start = m + 1
        else:
            quick_sort(array, m + 1, end)
            end = m - 1
        



def input_to_ints():
    return list(map(int, input().split(' ')))



def main():
    n, m = input_to_ints()
    lines = []
    while n > 0:
        lines.append(input_to_ints())
        n -= 1
    points = input_to_ints()

def test():
    input1 = [4, 2, 6, 3, 89, 34, 1]
    accurate1 = sorted(input1)
    quick_sort(input1)
    assert np.array_equal(input1, accurate1)

if __name__ == '__main__':
    test()