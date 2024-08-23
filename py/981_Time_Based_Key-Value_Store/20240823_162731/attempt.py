from collections import defaultdict
from typing import List, Tuple


class TimeMap:

    # internal data structure should be a hashmap
    # Dict[str key, Tuple[int timestamp, str value]]
    # question promises that timestamp of set calls are strictly increasing, so we can always append to list end
    # constant time lookup and constant time append to list end, so set should be O(1) operation
    # get needs to return the value with the closest timestamp_prev to timestamp, OR ""
    # when might you need to return ""?
    # -> empty list
    # -> first/earliest list element is still timestamp_prev > timestamp
    # List elements would be sorted in ascending timestamp, which means we can use binary search for O(log n) get calls
    # Space complexity: We store all value-timestamp pairs, so that's O(n), where n is the number of `set` calls
    # both get and set do not require additional intermediary state, so they are O(1) function calls
    # Timemap()
    # set["foo","bar",1]
    # get["foo",1] >> return "bar"
    # get["foo",3] >> return "bar"
    # set["foo","bar2",3]
    # get["foo",3]
    # set["foo","bar3",4]
    # get["foo",5] >> "bar3"
    # get["foo",3] >> "bar2"
    # get["baz",5] >> ""
    def __init__(self):
        self.hm = defaultdict(list)  # {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append(
            (timestamp, value)
        )  # {"foo": [(1, "bar"), (3, "bar2"), (4, "bar3")]}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        values = self.hm[key]  # [(1, "bar"), (3, "bar2"), (4, "bar3")]
        left, right = 0, len(values) - 1  # left = 2, right = 2

        def predicate(values: List[Tuple], idx: int) -> bool:
            return values[idx][0] > timestamp  # False

        while left < right:
            mid = left + ((right - left) // 2)  # mid = 1
            # We want to find the smallest idx for which predicate is true
            if predicate(values, mid):
                right = mid
            else:
                left = mid + 1
        # when exit while loop, left is first element to right of bound
        # OR, if only one element, left is the element itself
        if values[left][0] <= timestamp:
            return values[left][1]  # return "bar3"
        return values[left - 1][1] if left >= 1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

