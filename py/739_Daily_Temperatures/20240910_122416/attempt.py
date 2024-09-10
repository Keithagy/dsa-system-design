from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                found_warmer_day = stack.pop()
                result[found_warmer_day[0]] = day - found_warmer_day[0]
            stack.append((day, temp))
        return result

