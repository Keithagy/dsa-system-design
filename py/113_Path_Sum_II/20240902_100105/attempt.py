from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # probably a backtracking problem
    # DFS >> O(n) time, O(h) space for tracking path
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        cur_sum = root.val  # 5
        path = [root.val]  # [5]
        result = []

        def dfs(node: TreeNode) -> None:
            nonlocal cur_sum

            if not node.left and not node.right:
                if cur_sum == targetSum:
                    result.append(path[:])
                return

            if node.left:
                cur_sum += node.left.val
                path.append(node.left.val)
                dfs(node.left)
                cur_sum -= path.pop()  # backtrack left

            if node.right:
                cur_sum += node.right.val
                path.append(node.right.val)
                dfs(node.right)
                cur_sum -= path.pop()  # backtrack right

        dfs(root)
        cur_sum -= path.pop()  # backtrack root
        return result

