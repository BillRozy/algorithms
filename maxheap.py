import math
class MaxHeap:

    def __init__(self):
        self.array = []
    
    def _sift_up(self, index):
        if self.array[index - 1] > self._parent(index):
            parent = self._parent(index)
            self.array[self._parent_index(index) - 1] = self.array[index - 1]
            self.array[index - 1] = parent
            self._sift_up(self._parent_index(index))
    
    def _sift_down(self, index):
        child_indexes = self._childs_indexes(index)
        childs = self._childs(index)
        if childs:
            max_child = max(childs)
            max_child_index = child_indexes[childs.index(max_child)]
            if self.array[index - 1] < max_child:
                sinker = self.array[index - 1]
                self.array[index - 1] = max_child
                self.array[max_child_index - 1] = sinker
                self._sift_down(max_child_index)

    def _childs_indexes(self, parent_index):
        childs = []
        try:
            assert 2 * parent_index < len(self.array)
            childs.append(2 * parent_index)
            assert 2 * parent_index + 1 < len(self.array)
            childs.append(2 * parent_index + 1)
        finally:
            return childs

    def _childs(self, parent_index):
        return list(map(lambda x: self.array[x - 1], self._childs_indexes(parent_index)))

    def _parent_index(self, child_index):
        if child_index == 1:
            return 1
        return child_index // 2

    def _parent(self, child_index):
        return self.array[self._parent_index(child_index) - 1]

    def insert(self, x):
        self.array.append(x)
        self._sift_up(len(self.array))

    def extract_max(self):
        assert self.array
        leaf = self.array.pop()
        if not self.array:
            return leaf
        maximum = self.array[0]
        self.array[0] = leaf
        self._sift_down(1)
        return maximum

    def __repr__(self):
        return str(self.array)

# heap = MaxHeap()
# for i in range(0, int(input())):
#     command = input()
#     if command.startswith('Insert'):
#         unused, value = command.split(' ')
#         heap.insert(int(value))
#     else:
#         print(heap.extract_max())

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
T = []
def t_insert(x):
    T.append(x)
def t_extract_max():
    m = 0
    for i in range(1, len(T)):
        if T[i] > T[m]:
            m = i
    result = T[m]
    del T[m]
    return result

hhh = MaxHeap()

n = 100000
for i in range(n):
    hhh.insert(i)
    t_insert(i)
for i in range(n):
    a = hhh.extract_max()
    b = t_extract_max()
    if a == b:
        print(i, a)
    else:
        print(i, a, b, "ERROR")
        break
