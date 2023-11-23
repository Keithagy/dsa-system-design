from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # negative numbers when squared become positive
        # negative portion of the array, when squared, becomes all positive, with largest number first
        # positive section of the array will remain sorted smallest first
        squared_negatives = []
        result = []
        for num in nums:
            if num < 0:
                squared_negatives.append(num**2)
            else:
                squared = num**2
                while squared_negatives and squared_negatives[-1] <= squared:
                    result.append(squared_negatives.pop())
                result.append(squared)
        while squared_negatives:
            result.append(squared_negatives.pop())
        return result
