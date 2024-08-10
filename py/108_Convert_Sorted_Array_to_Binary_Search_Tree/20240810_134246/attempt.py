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

        def convert(low: int, high: int) -> Optional[TreeNode]:
            if not low <= high:
                return None
            middle = low + ((high - low) // 2)
            return TreeNode(
                val=nums[middle],
                left=convert(low, middle - 1),
                right=convert(middle + 1, high),
            )

        return convert(0, len(nums) - 1)

