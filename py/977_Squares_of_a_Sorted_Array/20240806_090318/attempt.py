from typing import List


# linear runtime, linear memory
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_negatives = []
        result = []
        for num in nums:
            if num < 0:
                squared_negatives.append(num**2)
                continue
                # the first element in squared_negatives will have largest magnitude
                # squared_negatives.pop() always gives the smallest value
            squared = num**2
            while squared_negatives and squared_negatives[-1] <= squared:
                result.append(squared_negatives.pop())
            result.append(squared)
        while squared_negatives:
            result.append(squared_negatives.pop())
        return result

