from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = []
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] < intervals[i + 1][0]:
                result.append(intervals[i])
                i += 1
            else:
                merged = intervals[i]
                i += 1
                while i < len(intervals) and intervals[i][0] <= merged[1]:
                    merged = [
                        min(intervals[i][0], merged[0]),
                        max(intervals[i][1], merged[1]),
                    ]
                    i += 1
                result.append(merged)
        result.extend(intervals[i:])
        return result

