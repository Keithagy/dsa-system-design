from typing import List


class Solution:
    """
    Have to start from first wall -> skip until first non-zero
    Volume of a sub-container is given by min(height[ left ],height[ right ]) * (right-left)
    Important considerations:
    [edge] no right wall
    [edge] single wall only
        - suppose you track left and right as variables
        - left starts at none, set left to val upon first wall
            - upon finding left, find right, calculate and add volume, set left to right
            - How do you know you have a right?
                - when the volume function gives you > 0?
                - When you find a wall that is at least as high
                - If you don't have a wall after you that is at least as high?
                    - Keep track of the two highest walls, set the earlier one to be left and later one to be right

    [case] irregular container shape
        - You need to compute the area of water to add as the complement of the black section to the area.
        - wallHeight = min(height[right],height[left])
        - water += ( wallHeight * (right-left) ) - (2*wallHeight + sum(height[left+1:right]
    you have a brute force approach which eseentially runs in O(v^2) time, where v is the total sum of wall material used
    """

    def trap(self, height: List[int]) -> int:
        def waterBtw(left: int, right: int) -> int:
            wallHeight = min(height[right], height[left])
            return (wallHeight * (right - left + 1)) - (
                2 * wallHeight + sum(height[left + 1 : right])
            )

        def validLeftWall(left: int) -> bool:
            return left < len(height) - 1 and height[left] != 0

        def validRightWall(right: int, left: int) -> bool:
            return (
                (0 <= left < len(height) - 1)
                and (left < right < len(height))
                and height[right] >= height[left]
            )

        water = 0
        left = 0
        while left < len(height) - 1:
            while not validLeftWall(left):
                left += 1  # find first wall
            right = left
            while not validRightWall(right, left):
                right += 1  # find second wall; exit when find wall equal or higher
                if right >= len(height):
                    break

            if validRightWall(right, left):
                water += waterBtw(left, right)
                left = right
            else:
                # keep the tail and test for a smaller subvessel
                left = left + 1
                right = left
        return water
