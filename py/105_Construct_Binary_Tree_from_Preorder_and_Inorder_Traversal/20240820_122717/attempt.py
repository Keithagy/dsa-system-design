# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # preorder: root, left, right
    # inorder: left,root,right
    # Observations for a given subtree:
    # in the preorder, you can always find the root in the first element
    # in the inorder, you can always find left/right subtrees to left/right of the root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx_map = {num: idx for (idx, num) in enumerate(inorder)}

        def build(
            pre_start: int, pre_end: int, in_start: int, in_end: int
        ) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(val=root_val)

            root_idx_in_inorder = inorder_idx_map[root_val]
            root.left = build(
                pre_start + 1,
                pre_start + root_idx_in_inorder - in_start,
                in_start,
                root_idx_in_inorder - 1,
            )
            root.right = build(
                pre_start + root_idx_in_inorder - in_start + 1,
                pre_end,
                root_idx_in_inorder + 1,
                in_end,
            )
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

