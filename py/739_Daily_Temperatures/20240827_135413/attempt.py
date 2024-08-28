from typing import List


class Solution:
    # use a stack to track monotically decreasing elements
    # for some temperature, pop all elements of the stack that are smaller than temperature, and write the difference of indexes to result array
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for day, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                (cooler_earlier_day, _) = stack.pop()
                result[cooler_earlier_day] = day - cooler_earlier_day
            stack.append((day, temperature))
        return result

