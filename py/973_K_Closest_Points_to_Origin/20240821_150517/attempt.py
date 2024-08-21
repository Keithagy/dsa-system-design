from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        def dist(point: List[int]) -> int:
            return point[0] ** 2 + point[1] ** 2

        for point in points:
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist(point), point))
            else:
                eu = -dist(point)
                if eu > max_heap[0][0]:
                    heapq.heapreplace(max_heap, (eu, point))
        return [item[1] for item in max_heap]

