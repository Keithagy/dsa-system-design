from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_sums = defaultdict(int)
        subarray_sums[0] = 1
        sum = 0
        result = 0
        for num in nums:
            sum += num
            sum_to_drop = sum - k
            result += subarray_sums[sum_to_drop]
            subarray_sums[sum] += 1
        return result

