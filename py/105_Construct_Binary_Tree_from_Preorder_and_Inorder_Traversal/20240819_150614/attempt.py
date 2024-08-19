# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    # preorder: root, left, right
    # inorder: left, root ,right
    # Assume a tree with 3 nodes, root 1 left 2 right 3:
    # preorder: [1,2,3]
    # inorder: [2,1,3]
    #
    # Assume a tree with 2 nodes, root 1 left 2:
    # preorder: [1,2]
    # inorder: [2,1]
    #
    # Assume a tree with 2 nodes, root 1 right 3:
    # preorder: [1,3]
    # inorder: [1,3]
    # >> in the case of an unbalanced tree, the child goes on the right if preorder and inorder line up.
    def treeFromPreOrder(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        return TreeNode(val=preorder[0], left=None)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 3:
            return self.treeFromPreOrder(preorder, inorder)

