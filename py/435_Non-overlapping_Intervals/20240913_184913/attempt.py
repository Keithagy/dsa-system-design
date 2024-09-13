from typing import List


class Solution:
    # you can sort intervals by start, then push intervals onto another list if they don't overlap.
    # if intervals have the same start time, choose the smallest one. (this does not work)
    # an alternative way to frame this: what is the longest possible sequence of non-overlapping intervals?
    # once you have that, you can subtract length of intervals - lenght of this longest non overlapping sequence
    # a monotonic stack works. if overlap with latest, prefer the one with smaller duration
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        stack = []
        intervals.sort(key=lambda x: x[0])  # >> n log n

        def overlap(sooner: List[int], later: List[int]) -> bool:
            return not (later[0] >= sooner[1])

        def shorterThan(this: List[int], other: List[int]) -> bool:
            return (this[1] - this[0]) < (other[1] - this[0])

        def equalDuration(sooner: List[int], later: List[int]) -> bool:
            return (sooner[1] - sooner[0]) == (later[1] - later[0])

        for interval in intervals:
            if stack and overlap(stack[-1], interval):
                if equalDuration(stack[-1], interval):
                    continue
                while stack and shorterThan(stack[-1], interval):
                    stack.pop()
            stack.append(interval)
        return len(intervals) - len(stack)

