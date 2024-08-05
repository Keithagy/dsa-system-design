class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0  # this always sweeps forward by 1.
        # this only works because non_zero_pos, which searches forward for the first zero, starts at the same value as i, which searches forward for the first non-zero.
        # for contiguous blocks of non zero numbers, i falls behind non_zero_pos. when we encounter zero series, then i runs ahead of non_zero_pos, which does not get incremented.
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != non_zero_pos:
                    nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1

