from typing import List
import math


class Solution:
    # think about the input case "[2,4,0,6]"
    # It's a bit subtle, isn't it? the algorithm doesn't actually hold the values 2,4,6; when the algorithm finishes the value of first is actually 0
    # But... it's fine because you only need to keep track of what subsequent values are to be compared against
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = math.inf, math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            elif num > second:
                return True
        return False
