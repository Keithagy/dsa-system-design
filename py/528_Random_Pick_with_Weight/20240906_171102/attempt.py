import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.inner = []
        self.sum = 0
        for weight in w:
            self.sum += weight
            self.inner.append(self.sum)

    def predicate(self, idx: int, target: float) -> bool:
        return self.inner[idx] >= target

    def pickIndex(self) -> int:
        pick = random.random() * self.sum
        left, right = 0, len(self.inner) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if self.predicate(mid, pick):
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

