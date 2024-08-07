from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for point in points:
            distance = -(point[0] ** 2 + point[1] ** 2)
            if len(result) < k:
                heapq.heappush(result, (distance, point))
                continue
            if result[0][0] < distance:
                heapq.heapreplace(result, (distance, point))
        return [x[1] for x in result]

