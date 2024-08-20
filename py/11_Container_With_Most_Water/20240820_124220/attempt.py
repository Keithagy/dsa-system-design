from typing import List


class Solution:
    # Container is 2d, so we care about the area, width * height
    # for 2 values i1 and i2:
    # width is given by i2 - i1
    # height is given by min(height[i2],height[i1])
    # notice that question requires the max area, not the specific walls of the container >> similarities to best time to buy/sell stock
    # Possibility of checking through one by one
    # You always want the earliest left wall, and higher is always better
    # right wall needs a max volume check
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left_wall_idx, right_wall_idx = 0, len(height) - 1
        while right_wall_idx > left_wall_idx:
            area = (right_wall_idx - left_wall_idx) * min(
                height[right_wall_idx], height[left_wall_idx]
            )
            result = max(area, result)
            if height[left_wall_idx] < height[right_wall_idx]:
                left_wall_idx += 1
                continue
            right_wall_idx -= 1

        return result

