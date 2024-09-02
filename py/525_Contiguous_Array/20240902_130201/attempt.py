from typing import List


class Solution:
    # Approach is to slide window of len 2 till alternating 1,0
    # then walk out window to while 0 to one side and 1 to another
    # then, merge window if start - 1 == some end
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        stack = []  # [(0,1)]
        for i in range(len(nums) - 1):  # [0]
            left_centre, right_centre = nums[i], nums[i + 1]  # 0, 1
            if set([left_centre, right_centre]) != set([1, 0]):
                continue
            start, end = i, i + 1  # 0,1
            while (
                start - 1 >= 0
                and end + 1 < len(nums)
                and set([nums[start - 1], nums[end + 1]]) == set([1, 0])
            ):
                start -= 1
                end += 1
            if stack and start - 1 == stack[-1][1]:
                prev = stack.pop()
                start = min(start, prev[0])
                end = max(end, prev[1])
            stack.append((start, end))

        if not stack:
            return 0
        return max([window[1] - window[0] + 1 for window in stack])

