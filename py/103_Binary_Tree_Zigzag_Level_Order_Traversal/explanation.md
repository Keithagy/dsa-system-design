## Explanation: Binary Tree Zigzag Level Order Traversal

### Analysis of problem & input data

This problem is a variation of the standard level-order traversal (also known as breadth-first search) of a binary tree. The key difference is the zigzag pattern requirement: we need to alternate the direction of traversal at each level.

Key characteristics of the problem:

1. We're dealing with a binary tree structure.
2. We need to process the tree level by level (breadth-first).
3. The direction of traversal alternates at each level (zigzag pattern).
4. The output should be a list of lists, where each inner list represents a level.

The input data is a binary tree, which could be:

- Empty (null root)
- A single node
- A complete binary tree
- An unbalanced tree (skewed left or right)

The key principle that makes this question conceptually simple is recognizing that it's fundamentally a level-order traversal with an added step of reversing the order of nodes at alternating levels. This insight allows us to leverage our understanding of BFS and queue-based level order traversal, with a minor modification to achieve the zigzag pattern.

### Test cases

1. Empty tree: `root = []`
   Expected output: `[]`

2. Single node tree: `root = [1]`
   Expected output: `[[1]]`

3. Complete binary tree: `root = [3,9,20,null,null,15,7]`
   Expected output: `[[3],[20,9],[15,7]]`

4. Unbalanced tree (left-skewed): `root = [1,2,null,3,null,4,null,5]`
   Expected output: `[[1],[2],[3],[4],[5]]`

5. Unbalanced tree (right-skewed): `root = [1,null,2,null,3,null,4,null,5]`
   Expected output: `[[1],[2],[3],[4],[5]]`

6. Tree with negative values: `root = [-1,2,-3,4,-5]`
   Expected output: `[[-1],[-3,2],[4,-5]]`

Here's the Python code to set up these test cases:

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
    [],
    [1],
    [3,9,20,None,None,15,7],
    [1,2,None,3,None,4,None,5],
    [1,None,2,None,3,None,4,None,5],
    [-1,2,-3,4,-5]
]

# Create tree objects for each test case
trees = [create_tree(case) for case in test_cases]

# Function to test (to be implemented)
def zigzag_level_order(root):
    pass

# Run tests
for i, tree in enumerate(trees):
    result = zigzag_level_order(tree)
    print(f"Test case {i+1}: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. BFS with level tracking and alternating order (Neetcode solution)
2. DFS with level tracking
3. BFS with deque and alternating append direction

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Naive approach: Perform a standard level-order traversal and then reverse alternate levels
2. Creating a full tree representation and then traversing it in zigzag order

#### Worthy Solutions

##### BFS with level tracking and alternating order (Neetcode solution)

```python
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        level = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()

                # Append node value based on level parity
                if level % 2 == 0:
                    current_level.append(node.val)
                else:
                    current_level.insert(0, node.val)

                # Add child nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            level += 1

        return result
```

Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(w), where w is the maximum width of the tree.

Explanation:

- We process each node exactly once, hence the time complexity is O(n).
- The space complexity is determined by the maximum number of nodes at any level (the width of the tree). In the worst case (a complete binary tree), this could be n/2, which is O(n), but it's more precisely described as O(w).

Key intuitions and invariants:

- Use a queue to perform level-order traversal (BFS).
- Keep track of the current level to determine the insertion order.
- Use `deque.popleft()` for efficient O(1) removal from the front of the queue.
- For even levels, append to the end; for odd levels, insert at the beginning.
- The level size is determined at the start of processing each level, ensuring we don't mix nodes from different levels.

##### DFS with level tracking

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], level: int, result: List[List[int]]):
            if not node:
                return

            # Ensure the list for this level exists
            if len(result) <= level:
                result.append([])

            # Add the node's value to the appropriate position based on level
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)

            # Recurse on children
            dfs(node.left, level + 1, result)
            dfs(node.right, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result
```

Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(h), where h is the height of the tree (due to recursion stack).

Explanation:

- We visit each node once, giving us a time complexity of O(n).
- The space complexity is determined by the recursion stack, which in the worst case (a skewed tree) could be O(n), but is generally O(h) for a balanced tree.

Key intuitions and invariants:

- Use DFS to traverse the tree, keeping track of the current level.
- Dynamically expand the result list as we encounter new levels.
- Use the level parity to determine whether to append or prepend to the current level's list.
- The recursion naturally handles the left-to-right ordering within each level.

##### BFS with deque and alternating append direction

```python
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level = deque()

            for _ in range(level_size):
                node = queue.popleft()

                # Add node value to level based on direction
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                # Add child nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result
```

Time Complexity: O(n), where n is the number of nodes in the tree.
Space Complexity: O(w), where w is the maximum width of the tree.

Explanation:

- We process each node once, giving us a time complexity of O(n).
- The space complexity is determined by the maximum number of nodes at any level (width of the tree), which is O(w).

Key intuitions and invariants:

- Use a queue for level-order traversal.
- Use a deque for each level to efficiently append in either direction.
- Alternate the direction of insertion for each level.
- Convert the deque to a list before adding to the result.

#### Rejected Approaches

1. Naive approach: Perform a standard level-order traversal and then reverse alternate levels

   - This approach is correct but inefficient. It requires an additional pass through half of the levels to reverse them, increasing time complexity unnecessarily.

2. Creating a full tree representation and then traversing it in zigzag order
   - This approach would require O(n) extra space to store the full tree representation, which is unnecessary for this problem.

#### Final Recommendations

The BFS with level tracking and alternating order (Neetcode solution) is the recommended approach for several reasons:

1. It's intuitive and directly addresses the zigzag requirement.
2. It has optimal time and space complexity.
3. It doesn't require any post-processing of the results.
4. It's easy to implement and understand, making it suitable for a coding interview setting.

The DFS approach is also worth knowing as it demonstrates a different perspective on the problem and can be useful in scenarios where recursion is preferred or when dealing with very deep trees where the stack space might be a concern.

### Visualization(s)

To visualize the BFS with level tracking approach, we can use a simple ASCII representation:

```
   3            Level 0: [3]
 /   \
9     20        Level 1: [20, 9]
     /  \
    15   7      Level 2: [15, 7]

Queue progression:
[3] → [9, 20] → [20, 15, 7] → [15, 7] → []

Result building:
[] → [[3]] → [[3], [20, 9]] → [[3], [20, 9], [15, 7]]
```

This visualization shows how we process the tree level by level, and how the zigzag pattern is achieved by alternating the order of insertion at each level.
