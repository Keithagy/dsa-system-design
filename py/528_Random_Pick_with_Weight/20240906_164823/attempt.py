from typing import List
from collections import deque
import random


class Solution:

    def __init__(self, w: List[int]):
        self.inner = deque()
        alternate = False
        for idx, weight in enumerate(w):
            while weight > 0:
                self.inner.append(idx) if alternate else self.inner.appendleft(idx)
                alternate = not alternate
                weight -= 1

    def pickIndex(self) -> int:

        return self.inner[random.randint(0, len(self.inner) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
