from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for i in range(len(intervals)):
            if not result:
                result.append(intervals[i])
                continue
            maybe_overlapping = result[-1]
            curr = intervals[i]
            if maybe_overlapping[1] >= curr[0]:
                result[-1] = [maybe_overlapping[0], max(maybe_overlapping[1], curr[1])]
            else:
                result.append(curr)
        return result

