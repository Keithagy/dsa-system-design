# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx_mapping = {num: idx for (idx, num) in enumerate(inorder)}

        def build(
            preStart: int, preEnd: int, inStart: int, inEnd: int
        ) -> Optional[TreeNode]:
            if preStart > preEnd:
                return None
            root_val = preorder[preStart]
            root = TreeNode(val=root_val)
            root_idx_in_inorder = inorder_idx_mapping[root_val]
            left_subtree_size = root_idx_in_inorder - inStart
            root.left = build(
                preStart + 1,
                preStart + left_subtree_size,
                inStart,
                root_idx_in_inorder - 1,
            )
            root.right = build(
                preStart + left_subtree_size + 1, preEnd, root_idx_in_inorder + 1, inEnd
            )
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

