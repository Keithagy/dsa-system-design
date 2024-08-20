## Explanation: Diameter of Binary Tree

### Analysis of problem & input data

This problem is about finding the longest path between any two nodes in a binary tree. The key insights are:

1. The diameter doesn't necessarily pass through the root.
2. The diameter is the maximum of:
   a) The longest path that passes through the root (left height + right height)
   b) The diameter of the left subtree
   c) The diameter of the right subtree

3. We can solve this problem using a depth-first search (DFS) approach, specifically a post-order traversal.
4. The height of a node is the maximum of the heights of its left and right children, plus one.
5. We can calculate the diameter and height simultaneously in one pass.

The key principle that makes this question simple is that the diameter of a tree can be expressed in terms of the heights of its subtrees. This allows us to use a bottom-up approach, calculating heights and updating the diameter as we go.

### Test cases

1. Empty tree: `root = None`
2. Single node: `root = TreeNode(1)`
3. Balanced tree: `root = [1,2,3,4,5,6,7]`
4. Skewed tree (left): `root = [1,2,None,3,None,4]`
5. Skewed tree (right): `root = [1,None,2,None,3,None,4]`
6. Tree with negative values: `root = [-10,9,20,None,None,15,7]`

Here's the Python code for these test cases:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Test cases
test_cases = [
    None,
    [1],
    [1,2,3,4,5,6,7],
    [1,2,None,3,None,4],
    [1,None,2,None,3,None,4],
    [-10,9,20,None,None,15,7]
]

trees = [create_tree(case) for case in test_cases]

# You can now use these trees to test your diameter function
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Recursive DFS with post-order traversal (optimal)
2. Iterative DFS with stack
3. BFS with queue

Count: 3 solutions

##### Rejected solutions

1. Brute force approach (calculating path length for every pair of nodes)
2. Converting the tree to a graph and using graph algorithms

#### Worthy Solutions

##### Recursive DFS with post-order traversal

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Class variable to store the maximum diameter

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Base case: height of None is 0

            left_height = dfs(node.left)   # Recurse on left subtree
            right_height = dfs(node.right) # Recurse on right subtree

            # Update diameter if path through current node is longer
            self.diameter = max(self.diameter, left_height + right_height)

            # Return height of current node
            return 1 + max(left_height, right_height)

        dfs(root)  # Start DFS from root
        return self.diameter
```

Runtime complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (skewed tree), this could be O(n).

Intuitions and invariants:

- The height of a node is 1 + max(left_height, right_height)
- The diameter through a node is left_height + right_height
- We can calculate both height and diameter in a single pass
- The maximum diameter seen so far is always maintained

##### Iterative DFS with stack

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        heights = {}  # Dictionary to store heights of nodes
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if visited:
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                # Update diameter
                diameter = max(diameter, left_height + right_height)

                # Calculate and store height of current node
                heights[node] = 1 + max(left_height, right_height)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return diameter
```

Runtime complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly twice (once to add to stack, once to process).
Space complexity: O(n) in the worst case, where we need to store heights for all nodes and the stack could contain all nodes for a skewed tree.

Intuitions and invariants:

- We use a stack to simulate the recursion
- Each node is visited twice: once to add its children to the stack, and once to process it
- We use a dictionary to store the heights of processed nodes
- The diameter is updated when processing a node, using its children's heights

##### BFS with queue

```python
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, None)])  # (node, parent) pairs
        children = {}  # Dictionary to store children of each node
        leaves = []

        while queue:
            node, parent = queue.popleft()

            if parent:
                children.setdefault(parent, []).append(node)

            if not node.left and not node.right:
                leaves.append(node)

            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))

        diameter = 0
        for leaf in leaves:
            path = self.longest_path(leaf, children)
            diameter = max(diameter, len(path) - 1)

        return diameter

    def longest_path(self, start: TreeNode, children: dict) -> list:
        queue = deque([(start, [start])])
        longest = []

        while queue:
            node, path = queue.popleft()
            if len(path) > len(longest):
                longest = path

            for child in children.get(node, []):
                queue.append((child, path + [child]))

        return longest
```

Runtime complexity: O(n^2) in the worst case, where n is the number of nodes. The BFS takes O(n), but we might need to find the longest path from each leaf, which could take O(n) for each leaf.
Space complexity: O(n) to store the children dictionary and the queue.

Intuitions and invariants:

- We first perform a BFS to identify all leaves and build a parent-child relationship
- We then find the longest path starting from each leaf
- The diameter is the length of the longest such path
- This approach is less efficient but demonstrates a different perspective on the problem

#### Rejected Approaches

1. Brute force approach: Calculating the path length between every pair of nodes. This would be O(n^2) time complexity and is unnecessary given the more efficient solutions available.

2. Converting to graph: While it's possible to convert the tree to a graph and use graph algorithms like Floyd-Warshall to find the longest path, this is overly complex and inefficient for this problem. It would change the time complexity to O(n^3) and space complexity to O(n^2).

#### Final Recommendations

The recursive DFS approach is the most elegant and efficient solution for this problem. It solves the problem in a single pass through the tree, has O(n) time complexity, and O(h) space complexity (which is often O(log n) for balanced trees). This solution demonstrates a deep understanding of tree structures and recursion, which are crucial for many tree-based problems in coding interviews.

The iterative DFS solution is also worth understanding as it demonstrates how to convert a recursive approach to an iterative one, which can be useful in scenarios where stack space is a concern.

The BFS approach, while less efficient, provides a different perspective on the problem and could be useful for understanding similar problems where level-order traversal is beneficial.

### Visualization(s)

To visualize the recursive DFS approach, we can use a simple ASCII representation of a binary tree and show how the algorithm processes it:

```
       1
      / \
     2   3
    / \
   4   5

Processing order:
4 -> 5 -> 2 -> 3 -> 1

At node 4: height = 1, diameter = 0
At node 5: height = 1, diameter = 0
At node 2: height = 2, diameter = 2 (path: 4 - 2 - 5)
At node 3: height = 1, diameter = 2
At node 1: height = 3, diameter = 3 (path: 4 - 2 - 1 - 3)

Final diameter: 3
```

This visualization shows how the algorithm processes nodes in post-order (left, right, root) and how the diameter is updated at each step.
