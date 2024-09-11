# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        elements of the result array fall into 3 categories: parent, sibling, children
        You can find the children by counting number of steps down in the traversal
        for parent, i would imagine the recursive function needs to return (propagate to parent) how far away it is from the target
        for sibling, i think you just need to pass in the distance in the recursive call
        """

        # This is probably wrong, because it relies on order of traversal. try converting to graph instead
        # distances = {}
        # distances[target.val] = 0
        #
        # def inner(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
        #     if not node:
        #         return
        #     if parent and parent.val in distances:
        #         distances[node.val] = distances[parent.val] + 1
        #     inner(node.left, node)
        #     if (
        #         (node.left and node.left.val in distances)
        #     ) and node.val not in distances:
        #         distances[node.val] = distances[node.left.val] + 1
        #     inner(node.right, node)
        #     if (
        #         (node.right and node.right.val in distances)
        #     ) and node.val not in distances:
        #         distances[node.val] = distances[node.right.val] + 1
        #
        # inner(root, None)
        # return [val for (val, dist) in distances.items() if dist == k]
        #

        graph = defaultdict(set)

        def convertToGraph(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if node.left:
                graph[node].add(node.left)
                graph[node.left].add(node)
            if node.right:
                graph[node].add(node.right)
                graph[node.right].add(node)
            convertToGraph(node.left)
            convertToGraph(node.right)

        convertToGraph(root)

        q = deque([(target, 0)])
        visited = set()
        result = []
        while q:
            (node, dist) = q.popleft()
            visited.add(node)
            if dist == k:
                result.append(node.val)
                continue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append((neighbor, dist + 1))
        return result

