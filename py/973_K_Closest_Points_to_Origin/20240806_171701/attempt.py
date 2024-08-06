import heapq
import math
from typing import List


class KeyWrapper:
    def __init__(self, point, eu_dis) -> None:
        self.point = point
        self.eu_dis = eu_dis

    def __lt__(self, other):
        return self.eu_dis < other.eu_dis


class CustomKeyHeap:
    def __init__(self):
        self.heap = []

    def push(self, point, eu_dis):
        heapq.heappush(self.heap, KeyWrapper(point, eu_dis))

    def pop(self):
        return heapq.heappop(self.heap).point

    def peek(self):
        return self.heap[0].item if self.heap else None


class Solution:
    def euDist(self, point):
        return math.sqrt((point[0] ** 2) + (point[1] ** 2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = CustomKeyHeap()
        for point in points:
            eu_dis = self.euDist(point)
            heap.push(point, eu_dis)

        result = []
        for _ in range(k):
            point = heap.pop()
            result.append(point)
        return result

