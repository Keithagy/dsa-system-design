from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 1 if nums[0] == k else 0
        sum = nums[0]
        left = 0
        for right in range(1, len(nums)):
            sum += nums[right]
            while sum > k:
                sum -= nums[left]
                left += 1
            if sum == k:
                res += 1
        return res

