from math import ceil
class MaxHeap:

    def __init__(self):
        self.array = []
    
    def _sift_up(self, index):
        if index == 0:
            return
        while self.array[index] > self.array[self.parent(index)]:
            parent = self.parent(index)
            # print('sifting up : ', (index, self.array[index]), (parent, self.array[parent]))
            tmp = self.array[parent]
            self.array[parent] = self.array[index]
            self.array[index] = tmp
            index = parent
            # print('swapped ', tmp, self.array[parent])
            # print('after swap', self.array)

    def _sift_down(self, index=0):
        while 2 * index + 1 < len(self.array):
            left = 2 * index + 1
            right = 2 * index + 2
            j = left
            if right < len(self.array) and self.array[right] > self.array[left]:
                j = right
            # print('sifting down: ', self.array[index], self.array[right], self.array[left])
            if self.array[index] >= self.array[j]:
                break
            tmp = self.array[index]
            self.array[index] = self.array[j]
            self.array[j] = tmp
            # print('swapped ', tmp, self.array[index])
            # print('after swap', self.array)
            index = j
            
                
    def parent(self, i):
        if i in [0, 1, 2]:
            return 0
        return (i - 1) // 2

    def insert(self, x):
        self.array.append(x)
        # print('inserted: ', x)
        # print('before sift up: ', self.array)
        self._sift_up(len(self.array) - 1)
        # print('after sift up: ', self.array)

    def extract_max(self):
        maximum = self.array[0]
        leaf = self.array.pop()
        # print('extracted: ', maximum)
        # print('leaf to top: ', leaf)
        if self.array:
            self.array[0] = leaf
        # print('before sift down: ', self.array)
        self._sift_down()
        # print('after sift down: ', self.array)
        return maximum

    def __repr__(self):
        return str(self.array)

heap = MaxHeap()
for i in range(0, int(input())):
    command = input()
    if command.startswith('Insert'):
        unused, value = command.split(' ')
        heap.insert(int(value))
    else:
        print(heap.extract_max())

# heap.insert(7)
# heap.insert(12)
# heap.insert(1)
# heap.insert(41)
# heap.insert(2)
# heap.insert(18)
# heap.insert(9)
# heap.insert(11)
# print(heap)
# print(heap.extract_max())
# print(heap)
# print(heap.extract_max())
# print(heap)
# print(heap.extract_max())
# print(heap)

# Тестовый тривиальный алгоримт
# T = []
# def t_insert(x):
#     T.append(x)
# def t_extract_max():
#     m = 0
#     for i in range(1, len(T)):
#         if T[i] > T[m]:
#             m = i
#     result = T[m]
#     del T[m]
#     return result

# hhh = MaxHeap()

# n = 1000
# for i in range(n):
#     hhh.insert(i)
#     t_insert(i)
# for i in range(n):
#     a = hhh.extract_max()
#     b = t_extract_max()
#     if a == b:
#         print(i, a)
#     else:
#         print(i, a, b, "ERROR")
#         break
