from typing import List


class Solution:
    def overlaps(self, a: List[int], b: List[int]) -> bool:
        starts_first = min(a[0], b[0])
        if starts_first == a[0]:
            return a[1] >= b[0]
        return b[1] >= a[0]

    def merge(self, a: List[int], b: List[int]) -> List[int]:
        new_start = min(a[0], b[0])
        new_end = max(a[1], b[1])
        return [new_start, new_end]

    def starts_before(self, this: List[int], that: List[int]) -> bool:
        return this[0] < that[0]

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # return [... non_overlap_start_before, overlapping_merged, ...non_overlap_start_after]
        non_overlap_start_before = []
        overlapping_merged = newInterval
        non_overlap_start_after = []
        for interval in intervals:
            if self.overlaps(interval, overlapping_merged):
                overlapping_merged = self.merge(interval, overlapping_merged)
                continue
            if self.starts_before(interval, overlapping_merged):
                non_overlap_start_before.append(interval)
            else:
                non_overlap_start_after.append(interval)

        non_overlap_start_before.append(overlapping_merged)
        return non_overlap_start_before + non_overlap_start_after

