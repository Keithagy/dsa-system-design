from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point: List[int]) -> int:
            return point[0] ** 2 + point[1] ** 2

        result = []  # first element will be kth-closest point
        for point in points:
            if len(result) < k:
                heapq.heappush(result, (-dist(point), point))
                continue
            distance = -dist(point)
            if distance > result[0][0]:
                heapq.heapreplace(result, (distance, point))

        return [item[1] for item in result]

