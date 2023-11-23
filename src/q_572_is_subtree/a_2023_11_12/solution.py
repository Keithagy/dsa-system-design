# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, candidate: TreeNode, target: TreeNode) -> bool:
        check_seq = [(candidate, target)]
        while check_seq:
            (cur_candidate, cur_target) = check_seq.pop()
            if cur_candidate.val != cur_target.val:
                return False
            if not (
                (cur_candidate.left and cur_target.left)
                or (not cur_candidate.left and not cur_target.left)
            ):
                return False

            if cur_candidate.left and cur_target.left:
                check_seq.append((cur_candidate.left, cur_target.left))
            if not (
                (cur_candidate.right and cur_target.right)
                or (not cur_candidate.right and not cur_target.right)
            ):
                return False
            if cur_candidate.right and cur_get.right:
                check_seq.append((cur_candidate.right, cur_target.right))
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val:
                if self.check(cur, subRoot):
                    return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
