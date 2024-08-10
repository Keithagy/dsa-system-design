from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals):
            while (
                i < len(intervals) and intervals[i][1] < newInterval[0]
            ):  # should come before in result
                result.append(intervals[i])
                i += 1
            while (
                i < len(intervals) and not intervals[i][0] > newInterval[1]
            ):  # need to merge with newInterval
                newInterval[0], newInterval[1] = min(
                    newInterval[0], intervals[i][0]
                ), max(newInterval[1], intervals[i][1])
                i += 1
            result.append(newInterval)
            while i < len(intervals):
                result.append(intervals[i])
                i += 1
        return result or [newInterval]

