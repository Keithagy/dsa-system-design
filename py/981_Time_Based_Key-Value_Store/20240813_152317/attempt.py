from collections import defaultdict
from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
        self.inner: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp strictly increasing across all calls to set, so list of values for each key always sorted by timestamp
        self.inner[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # if no exact match with timestamp, we want to find the largest timestamp that is before the given timestamp
        # suppose [1,5,7], search 6, want 5
        # left 0, right 2, mid 1
        # left 2, right 2 >> return left - 1
        #
        # suppose [1,5,7], search 5, want 5
        # left 0, right 2, mid 1
        # left 1, right 2 , mid 1
        # left 2, right 2 , mid 1
        #
        # suppose [1,3,5,7], search 6, want 5
        # left 0, right 3, mid 1
        # left 2, right 3, mid 2
        # left 3, right 3, >> return left-1
        #
        # suppose [1,3,5,7], search 3, want 3
        # left 0, right 3, mid 1
        # left 0, right 1, mid 0
        # left 1, right 1, >> return left
        search_space = self.inner[key]
        if not search_space:
            return ""
        left, right = 0, len(search_space) - 1
        while left < right:
            mid = left + ((right - left) // 2)
            if search_space[mid][0] == timestamp:
                return search_space[mid][1]
            if search_space[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        return search_space[left][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

