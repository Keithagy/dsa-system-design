from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [0 for _ in range(len(height))]
        max_rights = [0 for _ in range(len(height))]
        result = 0
        for i in range(len(height)):
            if i == 0:
                continue
            max_lefts[i] = max(max_lefts[i - 1], height[i - 1])
        for j in range(len(height) - 2, -1, -1):
            max_rights[j] = max(max_rights[j + 1], height[j + 1])
        for k, wall in enumerate(height):
            result += max(0, min(max_lefts[k], max_rights[k]) - wall)
        return result

