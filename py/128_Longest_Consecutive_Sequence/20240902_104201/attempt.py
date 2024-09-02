from typing import List


class Solution:
    # Can i use counting sort and then iterate through counts to find longest sequence of non-zero?
    # I think i can...
    # input :  [0,3,7,2,5,8,4,6,0,1]
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_nums, max_nums = min(nums), max(nums)  # 0, 8
        counts = [0 for _ in range(max_nums - min_nums + 1)]
        # [1,0,1,1,0,1,0,1,0]
        for num in nums:
            counts[num - min_nums] += 1
        cur_run = min(counts[0], 1)
        longest_run = cur_run
        for i in range(1, len(counts)):
            if counts[i - 1] != 0 and counts[i] != 0:
                cur_run += 1
                longest_run = max(longest_run, cur_run)
            else:
                cur_run = min(counts[i], 1)
        return longest_run

