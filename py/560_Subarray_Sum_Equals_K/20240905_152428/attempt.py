from collections import defaultdict
from typing import List


class Solution:
    # Core question: what subarrays can i chop off from the front to lose a certain amount?
    # [1, -1, 1] ; k = 0
    def subarraySum(self, nums: List[int], k: int) -> int:
        # {
        #   0: 2
        #   1: 2
        # }
        prefix_sums = defaultdict(int)
        prefix_sums[0] += 1  # 1 prefix, the empty array, sums to 0
        sum = 0  # 1
        result = 0  # 2
        for i in range(len(nums)):  # 2
            sum += nums[i]
            excess = sum - k  # 1
            if excess in prefix_sums:
                result += prefix_sums[excess]
            prefix_sums[sum] += 1
        return result

