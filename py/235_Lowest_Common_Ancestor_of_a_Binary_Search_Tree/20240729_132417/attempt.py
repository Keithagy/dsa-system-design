# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root:
            return root
        # key property: in a binary search tree, all left chidren are smaller, all right children are larger, always
        if (
            (p.val < root.val and q.val > root.val)
            or (p.val > root.val and q.val < root.val)
            or root.val == p.val
            or root.val == q.val
        ):
            return root

        if not root.left:
            return root.right

        if not root.right:
            return root.left

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

