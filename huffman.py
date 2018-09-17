class PriorityQueue:
    def __init__(self, tuples=[]):
        self.storage = sorted(tuples, key=lambda x: x[1])
    def extract_min(self):
        assert self.storage
        it = self.storage[0]
        self.storage = self.storage[1:] if len(self.storage) > 1 else []
        return it
    def insert(self, tupl):
        val, priority, childs = tupl
        if self.storage:
            if priority >= self.storage[-1][1]:
                self.storage.append(tupl)
            elif priority < self.storage[0][1]:
                self.storage = [tupl, *self.storage]
            else:
                split_at = self._find_index(tupl)
                self.storage = [*self.storage[:split_at], tupl, *self.storage[split_at:]]
        else:
            self.storage.append(tupl)

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
    letters = {}
    for letter in string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    queue = PriorityQueue()
    uniques = len(letters)
    for key in list(letters):
        queue.insert((key, letters[key], []))
    for k in range(uniques + 1, 2 * uniques):
        try:
            min1 = queue.extract_min()
            min2 = queue.extract_min()
            Fk = (min1[0] + min2[0], min1[1] + min2[1], [min1, min2])
            queue.insert(Fk)
        except AssertionError:
            break
    tree = queue.extract_min()
    codes = build_codes(tree[2], tree[0], '', '') if tree[2] else {tree[0]: '0'}
    encoded = encode_string(string, codes)
    return ['{} {}'.format(uniques, len(encoded)), *map(lambda tupl: '{}: {}'.format(*tupl), codes.items()), encoded]



def build_codes(nodes, liter, bit, prev):
    codes = {}
    if nodes:
        first, second = nodes
        codes = {
                    **codes,
                    **build_codes(first[2], first[0], '0', prev + bit),
                    **build_codes(second[2], second[0], '1', prev + bit)
                }
    else:
        codes = {**codes, liter: prev + bit}
    return codes

def encode_string(string, codes):
    res = ''
    for liter in string:
        res += codes[liter]
    return res


some_str = input()
qu = haffman(some_str)
for ans in qu:
    print(ans)
