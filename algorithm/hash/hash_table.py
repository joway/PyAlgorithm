from algorithm.hash.horner_hash import horner_hash
from datastructure.list.list_node import ListNode

HASH_ALGORITHM = {
    'mod': lambda x, base=10: x % base,
    'horner': horner_hash
}


class CONFLICT_ALGO:
    SEPARATE_CHAIN = 1
    OPEN_ADDRESSING = 2


class HashTable(object):
    def __init__(self, size, hash_algo='horner',
                 conflict_algo=CONFLICT_ALGO.SEPARATE_CHAIN):
        self.table = [None] * size
        self.size = size
        self.hash_algo = HASH_ALGORITHM.get(
            hash_algo if hash_algo in HASH_ALGORITHM else 'horner')
        self.conflict_algo = conflict_algo

    def set(self, key, val=None):
        index = self.hash_algo(key, self.size)
        val = val if val else key
        # 冲突解决
        # 1. 分离链接法
        if self.conflict_algo == CONFLICT_ALGO.SEPARATE_CHAIN:
            if self.table[index] is None:
                self.table[index] = ListNode(val)
            else:
                self.table[index].append(ListNode(val))

        # 2. 开放定址法
        elif self.conflict_algo == CONFLICT_ALGO.OPEN_ADDRESSING:
            if self.table[index] is None:
                self.table[index] = val
            else:
                self.table[index].append(ListNode(val))
        else:
            raise Exception('Conflict Algo not Support')

    def get(self, key):
        if self.conflict_algo == CONFLICT_ALGO.SEPARATE_CHAIN:
            pos = self.table[self.hash_algo(key, self.size)]
            print('log : ', pos.post)
            while pos.post:
                if pos.val == key:
                    return pos
                pos = pos.post
        else:
            return self.table[self.hash_algo(key, self.size)]


if __name__ == '__main__':
    table = HashTable(10)
    for i in range(100):
        index = i % 10
        table.set(index)

    print(table.get(18))
