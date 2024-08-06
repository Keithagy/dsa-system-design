import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = -(
                point[0] ** 2 + point[1] ** 2
            )  # sqrt is monotonic so skip for ordering
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, point))
                continue
            if dist > max_heap[0][0]:
                heapq.heapreplace(max_heap, (dist, point))
        return [item[1] for item in max_heap]

