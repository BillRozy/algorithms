class HuffmanTree:
    def __init__(self, array):
        self.nodes = array or []

    def add_node(self, node):
        self.nodes.append(node)

    def __repr__(self):
        return str(self.nodes)

class HuffmanNode:
    def __init__(self, letter, frequency):
        self.frequency = frequency
        self.letter = letter
        self.nodes = []
    def add_node(self, node):
        self.nodes.append(node)

    def __repr__(self):
        return str((self.letter, self.frequency, self.nodes))


class PriorityQueue:
    def __init__(self, tuples):
        self.storage = sorted(tuples, key=lambda x: x[1])
    def extract_min(self):
        assert self.storage
        it = self.storage[0]
        self.storage = self.storage[1:] if len(self.storage) > 1 else []
        return it
    def insert(self, tupl):
        val, priority = tupl
        if self.storage:
            if priority >= self.storage[-1][1]:
                self.storage.append(tupl)
            elif priority < self.storage[0][1]:
                self.storage = [tupl, *self.storage]
            else:
                split_at = self._find_index(tupl)
                self.storage = [*self.storage[:split_at], tupl, *self.storage[split_at:]]

    def _find_index(self, tupl):
        ind = len(tupl)
        for index, item in enumerate(self.storage):
            if item[1] <= tupl[1]:
                ind = index + 1
            else:
                break
        return ind

    def __repr__(self):
        return str(self.storage)


def haffman(string):
    tree = HuffmanTree([])
    letters = {}
    for letter in string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    uniques = len(letters.keys())
    queue = PriorityQueue(letters.items())
    print(queue)
    codes = {}
    for k in range(len(queue.storage) + 1, 2 * len(queue.storage) - 1):
        try:
            min1 = queue.extract_min()
            min2 = queue.extract_min()
            print(queue)
            Fk = (min1[0] + min2[0], min1[1] + min2[1])
            queue.insert(Fk)
            print(queue)
            min1 = HuffmanNode(*min1)
            min2 = HuffmanNode(*min2)
            Fk = HuffmanNode(*Fk)
            Fk.add_node(min1)
            Fk.add_node(min2)
            tree.add_node(Fk)
        except AssertionError:
            break
    try:
        min1 = queue.extract_min()
        min2 = queue.extract_min()
        print(queue)
        Fk = (min1[0] + min2[0], min1[1] + min2[1])
        queue.insert(Fk)
        print(queue)
        min1 = HuffmanNode(*min1)
        min2 = HuffmanNode(*min2)
        Fk = HuffmanNode(*Fk)
        Fk.add_node(min1)
        Fk.add_node(min2)
        tree.add_node(Fk)
    except AssertionError:
        pass
    return tree


some_str = input()
qu = haffman(some_str)
print(qu)
