from collections import deque
from typing import Counter, List
import heapq


class Solution:
    class HeapItem:
        def __init__(self, count: int, word: str) -> None:
            self.count = count
            self.word = word

        def __lt__(self, other: "Solution.HeapItem") -> bool:
            return self.count < other.count or (
                self.count == other.count and self.word > other.word
            )

    # You want a fixed-sized heap for the leaderboard
    # Expect that you need a custom sorting function here
    # you want a min-heap. top of heap is kth most frequent word, and comes last in the dict.
    # a should be less than b, if a's count is less than b, and a's lex order is greater than b (comes later than b in dict)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        h = []
        for word, count in counts.items():
            e = Solution.HeapItem(count, word)
            if len(h) < k:
                heapq.heappush(h, e)
            else:
                if e > h[0]:
                    heapq.heapreplace(h, e)

        # you can't just return the heap, because the heap is only weakly sorted (i.e children are less than parent, but not recursively true for every subtree)
        # return [item.word for item in h][::-1]
        result = deque()
        while k:
            result.appendleft(heapq.heappop(h).word)
            k -= 1

        return result

