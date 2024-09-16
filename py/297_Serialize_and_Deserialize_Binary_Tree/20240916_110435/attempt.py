from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def leftIdx(self, parentIdx: int) -> int:
        return parentIdx * 2 + 1

    def rightIdx(self, parentIdx: int) -> int:
        return parentIdx * 2 + 2

    def parentIdx(self, childIdx: int) -> int:
        return (childIdx - 1) // 2

    def isLeftChild(self, parentIdx: int, childIdx: int) -> bool:
        return parentIdx * 2 + 1 == childIdx

    def serialize(self, root):
        if not root:
            return "[]"
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        result = []
        while q:
            nextNode = q.popleft()
            result.append(str(nextNode.val) if nextNode else "None")
            if nextNode:
                q.append(nextNode.left)
                q.append(nextNode.right)
        return "[" + ",".join(result) + "]"

    def deserialize(self, data):
        if data == "[]":
            return None
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = [
            None if item == "None" else TreeNode(int(item))
            for item in data[1:-1].split(",")
        ]
        childs = nodes[::-1]
        root = childs.pop()
        for node in nodes:
            if node is not None:
                if childs:
                    node.left = childs.pop()
                if childs:
                    node.right = childs.pop()
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

