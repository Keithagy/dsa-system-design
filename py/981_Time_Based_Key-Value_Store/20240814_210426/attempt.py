from typing import Dict, List, Tuple
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.inner: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.inner[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        search_space = self.inner[key]

        def predicate(k: int) -> bool:
            return search_space[k][0] > timestamp

        if not search_space:
            return ""
        left, right = 0, len(search_space)
        while left < right:
            mid = left + (right - left) // 2
            # when loop ends, left should be minimal k s.t. predicate(k) is True
            if predicate(mid):
                right = mid
            else:
                left = mid + 1

        # here, left would be first value after timestamp
        if not 1 <= left <= len(search_space):
            return ""
        if left == 0:
            return "" if search_space[left][0] > timestamp else search_space[left][1]
        return (
            "" if search_space[left - 1][0] > timestamp else search_space[left - 1][1]
        )


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

