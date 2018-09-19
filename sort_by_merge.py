import numpy as np
from collections import deque
acc = 0

def inversions(it, array):
    result, count = merge_count_inversion(array)
    return count

def merge(left, right):
    result = []
    i1 = 0
    i2 = 0
    count = 0
    left_len = len(left)
    while i1 < left_len and i2 < len(right):
        if left[i1] > right[i2]:
            result.append(right[i2])
            i2 += 1
            count += left_len - i1
        else:
            result.append(left[i1])
            i1 += 1
    result += left[i1:]
    result += right[i2:]
    return result, count

def merge_count_inversion(array):
    if len(array) <= 1:
        return array, 0
    middle = len(array) // 2
    left, a = merge_count_inversion(array[:middle])
    right, b = merge_count_inversion(array[middle:])
    result, c = merge(left, right)
    return result, (a + b + c)


def sort_by_merge(array, start=0, end=None):
    end = end or len(array)
    if start < end - 1:
        middle = (start + end) // 2
        return merge(sort_by_merge(array, start, middle), sort_by_merge(array, middle, end))[0]
    if array:
        return [array[start]]
    return []

def sort_by_merge_iterative(array):
    queue = deque()
    i = 0
    while i < len(array):
        queue.append([array[i]])
        i += 1
    while len(queue) > 1:
        queue.append(merge(queue.popleft(), queue.popleft()))
    if queue:
        return queue.popleft()
    return []

def custom_sort(it=False):
    if it:
        return sort_by_merge_iterative
    return sort_by_merge




def main():
    n = int(input())
    array = list(map(int, input().split(' ')))
    print(inversions(True, array))

def test(it):
    global acc
    zero = []
    input0 = [2]
    input1 = [2, 3, 9, 2, 9]
    input2 = [2, 3, 5, 10, 12]
    input3 = [12, 10, 5, 3, 2]
    input4 = [2, 4]
    # assert np.array_equal(merge([1, 5], [2, 23]), [1, 2, 5, 23])
    # assert np.array_equal(custom_sort(it)(zero), zero)
    # assert np.array_equal(custom_sort(it)(input0), input0)
    # assert np.array_equal(custom_sort(it)(input1), sorted(input1))
    # assert np.array_equal(custom_sort(it)(input2), sorted(input2))
    # assert np.array_equal(custom_sort(it)(input3), sorted(input3))
    # assert np.array_equal(custom_sort(it)(input4), input4)
    assert np.array_equal(custom_sort(it)(list(reversed(input4))), input4)
    assert 2 == inversions(it, input1)
    assert 0 == inversions(it, input2)
    assert 10 == inversions(it, input3)
    assert 21 == inversions(it, [7, 6, 5, 4, 3, 2, 1])
    assert 1 == inversions(it, [1, 2, 3, 5, 4])

if __name__ == '__main__':
    main()