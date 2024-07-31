from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = 0
        leading_by = 0
        for num in nums:
            if leading_by == 0:
                majority_element = num
            if majority_element == num:
                leading_by += 1
            else:
                leading_by -= 1
        return majority_element

