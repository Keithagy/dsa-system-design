# Explanation: Binary Tree Level Order Traversal

## Analysis of problem & input data

This problem involves traversing a binary tree in a specific order: level by level, from left to right. This is known as a level order traversal or breadth-first search (BFS) of a tree. The key characteristics and insights of this problem are:

1. The tree structure: We're dealing with a binary tree, where each node has at most two children.
2. Traversal order: We need to process nodes level by level, from top to bottom, and from left to right within each level.
3. Output format: The result should be a list of lists, where each inner list represents a level of the tree.
4. Null nodes: The tree may contain null nodes, which should be skipped in the output.
5. Empty tree handling: We need to consider the case of an empty tree (root is None).
6. Node values: The node values can range from -1000 to 1000, which fits within the standard integer range in most programming languages.
7. Tree size: The tree can have up to 2000 nodes, so our solution should be efficient enough to handle this scale.

The key principle that makes this question conceptually simple is that a breadth-first search naturally visits nodes level by level. By using a queue data structure, we can easily keep track of nodes at each level and process them in the required order.

### Test cases

Here are some test cases to cover various scenarios:

1. Normal case with multiple levels:
   Input: [3,9,20,null,null,15,7]
   Expected Output: [[3],[9,20],[15,7]]

2. Single node tree:
   Input: [1]
   Expected Output: [[1]]

3. Empty tree:
   Input: []
   Expected Output: []

4. Tree with only left children:
   Input: [1,2,null,3,null,4]
   Expected Output: [[1],[2],[3],[4]]

5. Tree with only right children:
   Input: [1,null,2,null,3,null,4]
   Expected Output: [[1],[2],[3],[4]]

6. Balanced tree with multiple levels:
   Input: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
   Expected Output: [[1],[2,3],[4,5,6,7],[8,9,10,11,12,13,14,15]]

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
    [3,9,20,None,None,15,7],
    [1],
    [],
    [1,2,None,3,None,4],
    [1,None,2,None,3,None,4],
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
]

# Function to run tests (to be implemented)
def level_order_traversal(root):
    pass  # Implementation will be provided in the solutions section

# Run tests
for i, case in enumerate(test_cases):
    root = create_tree(case)
    result = level_order_traversal(root)
    print(f"Test case {i + 1}:")
    print(f"Input: {case}")
    print(f"Output: {result}")
    print()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Iterative BFS using a queue (optimal and most intuitive)
2. Recursive DFS with level tracking
3. Iterative BFS using two queues
4. Iterative BFS using a queue with level size tracking

Count: 4 solutions

#### Rejected solutions

1. Depth-First Search (DFS) without level tracking: This approach would traverse the tree, but it wouldn't naturally group nodes by level.
2. Using a hash map to store levels: While this could work, it's unnecessarily complex for this problem and less efficient than using a queue.
3. Morris Traversal: This is an advanced technique for tree traversal with O(1) space complexity, but it's overly complex for this problem and doesn't naturally give level order.

### Worthy Solutions

#### 1. Iterative BFS using a queue

This is the most intuitive and efficient solution for this problem.

```python
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space Complexity: O(w), where w is the maximum width of the tree. In the worst case (a complete binary tree), this could be up to n/2 for the last level.

Key intuitions and invariants:

- Use a queue to maintain the order of nodes to be processed.
- Process nodes level by level, keeping track of the number of nodes at each level.
- Append children of current level nodes to the queue for processing in the next iteration.
- The queue always contains nodes of the next level to be processed.

#### 2. Recursive DFS with level tracking

While not as intuitive for this problem, a recursive DFS approach can also solve it efficiently.

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    def dfs(node: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
        if not node:
            return

        # If this is the first node at this level, create a new list
        if len(result) == level:
            result.append([])

        # Add the current node's value to the current level's list
        result[level].append(node.val)

        # Recursively process left and right children
        dfs(node.left, level + 1, result)
        dfs(node.right, level + 1, result)

    result = []
    dfs(root, 0, result)
    return result
```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space Complexity: O(h), where h is the height of the tree, due to the recursion stack. In the worst case (a skewed tree), this could be O(n).

Key intuitions and invariants:

- Use the recursion stack to implicitly keep track of the nodes to be processed.
- Pass the current level as a parameter in the recursive calls.
- Maintain a list of lists where each inner list corresponds to a level in the tree.
- The level parameter always matches the current depth in the tree.

#### 3. Iterative BFS using two queues

This approach uses two queues to separate the current level from the next level.

```python
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    current_level = deque([root])

    while current_level:
        next_level = deque()
        level_values = []

        while current_level:
            node = current_level.popleft()
            level_values.append(node.val)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(level_values)
        current_level = next_level

    return result
```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space Complexity: O(w), where w is the maximum width of the tree. In the worst case (a complete binary tree), this could be up to n/2 for the last level.

Key intuitions and invariants:

- Use two queues: one for the current level and one for the next level.
- Process all nodes in the current level before moving to the next level.
- The separation of levels is explicit in the data structure used.

#### 4. Iterative BFS using a queue with level size tracking

This approach is similar to the first one but doesn't use the `deque` data structure.

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level_values = []

        for _ in range(level_size):
            node = queue.pop(0)
            level_values.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_values)

    return result
```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space Complexity: O(w), where w is the maximum width of the tree. In the worst case (a complete binary tree), this could be up to n/2 for the last level.

Key intuitions and invariants:

- Use a single list as a queue to maintain the order of nodes to be processed.
- Keep track of the number of nodes at each level explicitly.
- Process nodes level by level, using the level size to determine when to start a new level.

### Rejected Approaches

1. Depth-First Search (DFS) without level tracking:
   While DFS can traverse the entire tree, it doesn't naturally group nodes by level. You would need to add significant complexity to track levels and reorganize the output, making it less efficient and more error-prone than BFS for this specific problem.

2. Using a hash map to store levels:
   This approach involves using a dictionary to store nodes at each level during traversal. While it works, it's unnecessarily complex and less efficient in both time and space compared to using a queue. It also requires an additional step to convert the dictionary to the required list of lists format.

3. Morris Traversal:
   This is an advanced technique that allows for tree traversal with O(1) extra space. However, it's overly complex for this problem and doesn't naturally produce a level order traversal. It would require significant modifications to work for this problem, making it impractical and hard to understand.

### Final Recommendations

The best solution to learn and implement for this problem is the Iterative BFS using a queue (Solution 1). This approach is:

1. Intuitive: It directly models the level-by-level traversal requirement.
2. Efficient: It has optimal time complexity O(n) and space complexity O(w).
3. Easy to implement and understand: The code is straightforward and mirrors the problem description.
4. Versatile: This approach can be easily modified for related problems (e.g., zigzag level order traversal).

The recursive DFS approach (Solution 2) is also worth understanding as it demonstrates how a depth-first approach can be adapted to solve a breadth-first problem. It's a good exercise in thinking about tree traversals more flexibly.

Solutions 3 and 4 are variations on the BFS theme and are less commonly used, but understanding them can deepen your grasp of BFS implementations.

Avoid using DFS without level tracking or hash map-based solutions, as they overcomplicate the problem. The Morris Traversal, while an interesting technique for other tree problems, is overkill for this particular task and doesn't align well with the level order requirement.

Remember, in an interview setting, clearly communicating your thought process and the trade-offs between different approaches is often as important as the implementation itself. Start with the simplest, most intuitive solution (iterative BFS), and then discuss possible optimizations or alternative approaches if time permits.

## Visualization(s)

To help visualize the BFS traversal process, here's a simple ASCII representation of how the queue evolves during the traversal of the tree from Example 1:

```
Tree:
     3
   /   \
  9    20
      /  \
     15   7

Step 0: Queue = [3]
        Output = []

Step 1: Process 3
        Queue = [9, 20]
        Output = [[3]]

Step 2: Process 9, 20
        Queue = [15, 7]
        Output = [[3], [9, 20]]

Step 3: Process 15, 7
        Queue = []
        Output = [[3], [9, 20], [15, 7]]

Final Output: [[3], [9, 20], [15, 7]]
```

This visualization shows how nodes are added to and removed from the queue, and how the output is built level by level. Each step represents the processing of one level of the tree.
