# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def inner(left: int, right: int) -> Optional[TreeNode]:
            if not left < right:
                return None
            middle = left + ((right - left) // 2)
            node = TreeNode(
                val=nums[middle],
                left=inner(left, middle),
                right=inner(middle + 1, right),
            )
            return node

        return inner(0, len(nums))

