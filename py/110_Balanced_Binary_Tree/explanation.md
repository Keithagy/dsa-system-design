## Explanation: Balanced Binary Tree

### Analysis of problem & input data

This problem is about determining if a given binary tree is height-balanced. The key characteristics and insights are:

1. Definition of height-balanced: For every node in the tree, the depth of its left and right subtrees should not differ by more than one.
2. This is a recursive property: If a tree is balanced, its subtrees must also be balanced.
3. The problem involves tree traversal and height calculation.
4. The input can be an empty tree, which is considered balanced by definition.
5. The number of nodes can be up to 5000, so the solution needs to be efficient.

The key principle that makes this question simple is the recursive nature of the problem. We can leverage the fact that a tree is balanced if and only if:

1. Its left subtree is balanced
2. Its right subtree is balanced
3. The difference in heights of its left and right subtrees is at most 1

This problem is a classic example of how a seemingly complex property of a tree can be verified using a bottom-up recursive approach, where we combine information from subtrees to make a decision about the whole tree.

### Test cases

1. Balanced tree: `[3,9,20,null,null,15,7]`
2. Unbalanced tree: `[1,2,2,3,3,null,null,4,4]`
3. Empty tree: `[]`
4. Single node tree: `[1]`
5. Left-heavy unbalanced tree: `[1,2,null,3,null,4,null,5]`
6. Right-heavy unbalanced tree: `[1,null,2,null,3,null,4,null,5]`
7. Large balanced tree with 5000 nodes (not shown due to size)

Here's the Python code to set up these test cases:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

# Test cases
test_cases = [
    [3,9,20,None,None,15,7],
    [1,2,2,3,3,None,None,4,4],
    [],
    [1],
    [1,2,None,3,None,4,None,5],
    [1,None,2,None,3,None,4,None,5]
]

trees = [create_tree(case) for case in test_cases]

# Function to be implemented
def is_balanced(root: TreeNode) -> bool:
    pass

# Run tests
for i, tree in enumerate(trees):
    print(f"Test case {i+1}: {is_balanced(tree)}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Bottom-up recursive approach (optimal)
2. Top-down recursive approach
3. Iterative approach using stack

Count: 3 solutions

##### Rejected solutions

1. Brute force approach of calculating depth for each node separately
2. Approaches that modify the tree structure

#### Worthy Solutions

##### Bottom-up recursive approach

```python
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode]) -> Tuple[bool, int]:
        if not node:
            return True, 0  # Base case: empty tree is balanced with height 0

        left_balanced, left_height = dfs(node.left)
        if not left_balanced:
            return False, 0  # Short-circuit if left subtree is unbalanced

        right_balanced, right_height = dfs(node.right)
        if not right_balanced:
            return False, 0  # Short-circuit if right subtree is unbalanced

        # Check if current node is balanced
        is_current_balanced = abs(left_height - right_height) <= 1
        current_height = max(left_height, right_height) + 1

        return is_current_balanced, current_height

    return dfs(root)[0]  # Return only the balance status, not the height
```

Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

- This solution uses a depth-first search (DFS) approach, traversing the tree in a post-order manner.
- The key intuition is to combine the balance check with height calculation in a single pass.
- We use a tuple to return two pieces of information: whether the subtree is balanced and its height.
- The algorithm leverages the fact that we can make a decision about a node's balance using only information from its immediate children.
- Short-circuiting is used to stop unnecessary computations once an unbalanced subtree is found.
- The height difference check `abs(left_height - right_height) <= 1` encapsulates the definition of a balanced tree.

##### Top-down recursive approach

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: Optional[TreeNode]) -> bool:
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def check_balance(node: Optional[TreeNode]) -> bool:
        if not node:
            return True  # An empty tree is balanced

        left_height = height(node.left)
        right_height = height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return check_balance(node.left) and check_balance(node.right)

    return check_balance(root)
```

Time Complexity: O(n^2) in the worst case, where n is the number of nodes
Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

- This approach separates the height calculation and balance checking into two separate recursive functions.
- The `height` function calculates the height of a subtree.
- The `check_balance` function checks if the current node is balanced and recursively checks its children.
- This solution is intuitive and closely follows the problem definition.
- It's less efficient than the bottom-up approach because it may recalculate heights of the same subtrees multiple times.
- The balance condition `abs(left_height - right_height) <= 1` is checked for each node explicitly.

##### Iterative approach using stack

```python
from typing import Optional, Tuple
from collections import namedtuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: Optional[TreeNode]) -> bool:
    NodeInfo = namedtuple('NodeInfo', ['node', 'state', 'height'])
    stack = [NodeInfo(root, 0, 0)]

    while stack:
        info = stack[-1]

        if not info.node:
            stack.pop()
            continue

        if info.state == 0:  # Pre-order: push right child
            stack[-1] = NodeInfo(info.node, 1, info.height)
            stack.append(NodeInfo(info.node.right, 0, 0))
        elif info.state == 1:  # In-order: push left child
            stack[-1] = NodeInfo(info.node, 2, info.height)
            stack.append(NodeInfo(info.node.left, 0, 0))
        else:  # Post-order: process node
            left_height = stack[-2].height if len(stack) > 1 and stack[-2].node == info.node.left else 0
            right_height = stack[-3].height if len(stack) > 2 and stack[-3].node == info.node.right else 0

            if abs(left_height - right_height) > 1:
                return False

            current_height = max(left_height, right_height) + 1
            stack.pop()
            if stack:
                stack[-1] = NodeInfo(stack[-1].node, stack[-1].state, current_height)

    return True
```

Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(h), where h is the height of the tree (due to the stack)

- This solution uses an iterative approach with a stack to simulate the recursive process.
- We use a named tuple `NodeInfo` to keep track of each node's state and height.
- The algorithm performs a post-order traversal, processing each node after its children.
- We use the stack to maintain the state of each node (0 for pre-order, 1 for in-order, 2 for post-order).
- The balance check is performed when a node is in its post-order state.
- This approach avoids the function call overhead of recursion and can be beneficial in languages with limited recursion depth.

#### Rejected Approaches

1. Brute force approach: Calculate the depth for each node separately and then check balance. This would result in O(n^2) time complexity and is inefficient for large trees.

2. Modifying tree structure: Any approach that modifies the original tree structure is not acceptable as it changes the input data.

3. BFS (Breadth-First Search) approach: While BFS can be used to traverse the tree, it doesn't naturally lend itself to efficient height calculation and balance checking for this problem.

#### Final Recommendations

The bottom-up recursive approach is the best solution to learn and use in an interview setting. It offers:

1. Optimal time complexity of O(n)
2. Clear and concise implementation
3. Efficient use of recursion to solve the problem in a single pass
4. Demonstrates understanding of tree structures and post-order traversal

This solution effectively combines height calculation with balance checking, avoiding redundant computations. It's also easier to explain and implement under interview pressure compared to the iterative approach.

### Visualization(s)

To visualize the bottom-up recursive approach, we can use a simple ASCII art representation:

```
       3
      / \
     9  20
       /  \
      15   7

Step 1: Check leaf nodes (9, 15, 7)
   9  -> (True, 1)
   15 -> (True, 1)
   7  -> (True, 1)

Step 2: Check node 20
   20 -> max(1, 1) + 1 = 2, |1-1| <= 1
      -> (True, 2)

Step 3: Check root node 3
   3  -> max(1, 2) + 1 = 3, |1-2| <= 1
      -> (True, 3)

Final result: Tree is balanced
```

This visualization shows how the algorithm works bottom-up, calculating heights and checking balance at each level.

```tsx
import React from "react";

const TreeNode = ({ value, left, right, x, y, level }) => {
  const radius = 20;
  const verticalSpacing = 80;
  const horizontalSpacing = 40 / (level + 1);

  return (
    <g>
      <circle cx={x} cy={y} r={radius} fill="lightblue" stroke="black" />
      <text x={x} y={y} textAnchor="middle" dominantBaseline="central">
        {value}
      </text>
      {left && (
        <>
          <line
            x1={x}
            y1={y + radius}
            x2={x - horizontalSpacing}
            y2={y + verticalSpacing - radius}
            stroke="black"
          />
          <TreeNode
            {...left}
            x={x - horizontalSpacing}
            y={y + verticalSpacing}
            level={level + 1}
          />
        </>
      )}
      {right && (
        <>
          <line
            x1={x}
            y1={y + radius}
            x2={x + horizontalSpacing}
            y2={y + verticalSpacing - radius}
            stroke="black"
          />
          <TreeNode
            {...right}
            x={x + horizontalSpacing}
            y={y + verticalSpacing}
            level={level + 1}
          />
        </>
      )}
    </g>
  );
};

const BalancedTreeVisualization = () => {
  const tree = {
    value: 3,
    left: { value: 9 },
    right: {
      value: 20,
      left: { value: 15 },
      right: { value: 7 },
    },
  };

  return (
    <svg width="300" height="300" viewBox="0 0 300 300">
      <TreeNode {...tree} x={150} y={40} level={0} />
    </svg>
  );
};

export default BalancedTreeVisualization;
```

This React component creates a visual representation of the balanced binary tree from Example 1. The tree is drawn using SVG, with each node represented by a circle containing its value. The layout of the tree is adjusted dynamically based on the depth of each node.
