from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i, t))
            else:
                while stack and stack[-1][1] < t:  # i.e t is a warmer day
                    found_warmer = stack.pop()
                    result[found_warmer[0]] = i - found_warmer[0]
                else:
                    stack.append((i, t))
        return result

