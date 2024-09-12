import random


class RandomizedSet:

    def __init__(self):
        self.hm = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        self.hm[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hm:
            return False
        idx, last = self.hm[val], self.l[-1]
        self.l[idx], self.hm[last] = last, idx
        self.l.pop()
        del self.hm[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

