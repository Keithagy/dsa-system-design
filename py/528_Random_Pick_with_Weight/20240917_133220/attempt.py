from typing import List
import bisect
import random


class Solution:

    def __init__(self, w: List[int]):
        self.inner = []
        runningSum = 0
        for num in w:
            runningSum += num
            self.inner.append(runningSum)

    def pickIndex(self) -> int:
        choice = random.random() * self.inner[-1]
        return bisect.bisect_left(self.inner, choice)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

