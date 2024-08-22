from typing_extensions import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(start: int) -> None:
            if start == n:
                result.append(nums[:])
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result

