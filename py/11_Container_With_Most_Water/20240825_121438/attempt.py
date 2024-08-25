from typing import List


class Solution:
    # width is given by (right - left)
    # height is given by max(height[left], height[right])
    # maximizing for width * height
    #
    # start from outside, with the largest width,
    # then walk in the walls where height[new_wall] > height[wall]
    # walk in the shorteest wall first
    # since walking in the walls will lose width, which might not result in gain in heigh if that wall was not the limiting ftor to begin with
    #
    # walk until left exceeds right, in which case all possible wall combinatiosn would have been considered
    # since we are walking in, solution would be O(len(height)) time
    # constant space since we just need indexes to track walls and variable to track the max area
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            w = right - left
            h = min(height[right], height[left])
            area = w * h
            max_area = max(area, max_area)
            if h == height[right]:
                while left < right and h >= height[right]:
                    right -= 1
            else:
                while left < right and h >= height[left]:
                    left += 1

        return max_area

