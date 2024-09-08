from typing import List


class Solution:
    # nums has at least one element and is potentially long
    # nums is [-10,10] >> it can be negative
    # naive solution is to try every single subarray >> n^2
    # remember that you are looking for a subarray, which means that the product has to of contiguous elements
    # product of any subarray containing a zero has got to be zero.
    # at each step, you can continue a previous subarray or start a new one.
    # when considering if you want to continue a previous subarray, you have to consider possibility of continue a previous negative subarray
    # because multiplying by a future negative number could give you the real max.
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        cur_highest = cur_lowest = nums[0]
        for right in range(1, len(nums)):
            extend = max(
                cur_highest * nums[right], cur_lowest * nums[right], nums[right]
            )
            cur_lowest = min(nums[right], cur_highest * nums[right], cur_lowest * curr)
            cur_highest = max(cur_highest, extend)
            max_product = max(cur_highest, max_product)
        return max_product

        # memo = {}
        #
        # def mps(startIdx: int, endIdx: int) -> int:
        #     if not 0 <= startIdx < endIdx <= len(nums) - 1:
        #         return nums[-1]  # here you only have one element, and that's the mps
        #     if startIdx in memo:
        #         return memo[startIdx]
        #     take = nums[startIdx] * mps(startIdx + 1)
        #     skip = mps(startIdx + 1)
        #     memo[startIdx] = max(take, skip)
        #     return memo[startIdx]
        #
        # return mps(0, len(nums) - 1)

