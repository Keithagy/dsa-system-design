# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # preorder: root left right
    # inorder: left root right
    # properties:
    # for any subtree, its preorder traversal has the root at the head
    # for any subtree, its inorder traversal has all the left subtree nodes, then the root, then the right subtree nodes
    # Start by making a hash map of all in order nodes to know which index preorder[0] will map onto >> O(n)
    # call inorder.indexOf(preorder[0]) k
    # len( inorder[:k] ) is number of nodes in left sub
    # that lets you recursively call the same function against the same subtree by passing in the indices of the subtrees for both indexes
    # O(n) recursive calls since we need to visit every node
    # log n?
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {num: idx for (idx, num) in enumerate(inorder)}

        # pre start 0
        # pre end 4
        # in start 0
        # in end 4
        #
        #       pre start 1
        #       pre end 1
        #       in start 0
        #       in end 0
        #              pre start 2
        #              pre end 1
        #              in start 0
        #              in end -1 >> None
        #       pre start 2
        #       pre end 4
        #       in start 2
        #       in end 4
        #              pre start 4
        #              pre end 4
        #              in start 4
        #              in end 4 >>
        def build(
            pre_start: int, pre_end: int, in_start: int, in_end: int
        ) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None
            root = TreeNode(val=preorder[pre_start])  # 20
            root_inorder_idx = inorder_map[preorder[pre_start]]  # 3
            left_sub_node_count = root_inorder_idx - in_start  # 1
            root.left = build(
                pre_start + 1,
                pre_start + left_sub_node_count,
                in_start,
                root_inorder_idx - 1,
            )
            root.right = build(
                pre_start + left_sub_node_count + 1,
                pre_end,
                root_inorder_idx + 1,
                in_end,
            )
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

