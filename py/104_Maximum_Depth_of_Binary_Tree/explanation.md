## Explanation: Maximum Depth of Binary Tree

### Analysis of problem & input data

This problem is a classic tree traversal question that tests understanding of recursive tree algorithms and depth-first search (DFS). The key characteristics of this problem are:

1. We're dealing with a binary tree structure, where each node has at most two children.
2. We need to find the longest path from the root to a leaf node.
3. The depth is defined as the number of nodes along this path, not the number of edges.

The key principle that makes this question simple is that the depth of a tree can be recursively defined as:
1 + max(depth of left subtree, depth of right subtree)

This problem is an excellent example of how recursive thinking can lead to elegant solutions for tree-based problems. It's also a good introduction to the concept of post-order traversal, where we process a node after processing its children.

### Test cases

When dealing with tree problems, it's crucial to consider various tree structures. Here are some important test cases:

1. Empty tree (root = None)
2. Tree with only one node
3. Balanced tree (Example 1 in the problem statement)
4. Unbalanced tree (Example 2 in the problem statement)
5. Skewed tree (all nodes to the left or all to the right)
6. Tree with negative values (to ensure we're not accidentally using node values in our depth calculation)

Here's the Python code for these test cases:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Test case 1: Empty tree
test1 = None

# Test case 2: Tree with only one node
test2 = TreeNode(1)

# Test case 3: Balanced tree
test3 = TreeNode(3)
test3.left = TreeNode(9)
test3.right = TreeNode(20)
test3.right.left = TreeNode(15)
test3.right.right = TreeNode(7)

# Test case 4: Unbalanced tree
test4 = TreeNode(1)
test4.right = TreeNode(2)

# Test case 5: Skewed tree
test5 = TreeNode(1)
test5.right = TreeNode(2)
test5.right.right = TreeNode(3)
test5.right.right.right = TreeNode(4)

# Test case 6: Tree with negative values
test6 = TreeNode(-10)
test6.left = TreeNode(-20)
test6.right = TreeNode(-30)
test6.left.left = TreeNode(-40)

# Function to test
def maxDepth(root: TreeNode) -> int:
    # Implementation will be provided in the solutions section

# Test all cases
test_cases = [test1, test2, test3, test4, test5, test6]
for i, test in enumerate(test_cases, 1):
    print(f"Test case {i}: {maxDepth(test)}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Recursive DFS (Depth-First Search)
2. Iterative DFS using stack
3. Iterative BFS (Breadth-First Search) using queue

These 3 solutions are all worth learning as they demonstrate different traversal techniques and data structures commonly used in tree problems.

##### Rejected solutions

1. Brute force approach of storing all paths and then finding the longest one
2. Solutions that try to use the node values to calculate depth

#### Worthy Solutions

##### Recursive DFS

```python
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0  # Base case: empty tree has depth 0

    # Recursive case: depth is 1 (current node) plus max depth of subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)
```

Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(h), where h is the height of the tree (due to recursion stack)

- This solution leverages the recursive nature of tree structures
- It uses the principle that the depth of a tree is 1 (for the current node) plus the maximum depth of its subtrees
- The base case (empty tree) returns 0, which propagates up the recursion chain
- This approach performs a post-order traversal, as we process a node after its children

##### Iterative DFS using stack

```python
from typing import Optional

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 1)]  # Each element is (node, depth)
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)  # Update max_depth if necessary

        # Add right child first so left child is processed first (DFS)
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

    return max_depth
```

Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(h), where h is the height of the tree (worst case: O(n) for a skewed tree)

- This solution mimics the recursive approach but uses an explicit stack
- Each stack element contains both the node and its depth
- We update max_depth as we go, eliminating the need for a separate variable to track current depth
- The right child is pushed onto the stack before the left to maintain DFS left-to-right order

##### Iterative BFS using queue

```python
from collections import deque
from typing import Optional

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([(root, 1)])  # Each element is (node, depth)
    max_depth = 0

    while queue:
        node, depth = queue.popleft()
        max_depth = depth  # In BFS, the last processed node will be at max depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return max_depth
```

Time Complexity: O(n), where n is the number of nodes in the tree
Space Complexity: O(w), where w is the maximum width of the tree (worst case: O(n) for a perfect binary tree)

- This solution uses BFS, processing nodes level by level
- We use a queue instead of a stack, appending children to the end
- The max_depth is simply the depth of the last processed node
- This approach is particularly useful if we need level-order information

#### Rejected Approaches

1. Brute force approach of storing all paths:
   This would involve traversing the entire tree, storing each path, and then finding the longest one. While correct, it's inefficient in both time and space complexity.

2. Solutions using node values:
   Any solution that tries to use the node values to calculate depth would be incorrect. The depth is determined by the structure of the tree, not the values in the nodes.

#### Final Recommendations

The recursive DFS solution is the most elegant and intuitive for this problem. It directly translates the problem statement into code and is the solution most interviewers would expect. However, understanding all three approaches (recursive DFS, iterative DFS, and BFS) is valuable for tackling various tree problems.

### Visualization(s)

To visualize the recursive DFS approach, we can use a simple ASCII tree representation:

```
       3
     /   \
    9    20
        /  \
       15   7

maxDepth(3) = 1 + max(maxDepth(9), maxDepth(20))
             = 1 + max(1, 1 + max(maxDepth(15), maxDepth(7)))
             = 1 + max(1, 1 + max(1, 1))
             = 1 + max(1, 3)
             = 1 + 3
             = 4
```

This visualization shows how the recursive calls build up and then resolve, demonstrating the post-order nature of the traversal.

```tsx
import React, { useState } from "react";
import { Card, CardContent, CardHeader } from "@/components/ui/card";

const TreeNode = ({ value, depth, maxDepth }) => {
  const size = 40;
  const gap = 20;
  const levelWidth = (maxDepth - depth + 1) * (size + gap);

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        width: `${levelWidth}px`,
      }}
    >
      <div
        style={{
          width: `${size}px`,
          height: `${size}px`,
          borderRadius: "50%",
          backgroundColor: "#4a90e2",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          color: "white",
          fontWeight: "bold",
          marginBottom: `${gap}px`,
        }}
      >
        {value}
      </div>
      {depth < maxDepth && (
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            width: "100%",
          }}
        >
          <TreeNode value={null} depth={depth + 1} maxDepth={maxDepth} />
          <TreeNode value={null} depth={depth + 1} maxDepth={maxDepth} />
        </div>
      )}
    </div>
  );
};

const BinaryTreeVisualization = () => {
  const [treeData, setTreeData] = useState({
    value: 3,
    left: { value: 9 },
    right: {
      value: 20,
      left: { value: 15 },
      right: { value: 7 },
    },
  });

  const renderTree = (node, depth = 1, maxDepth = 3) => {
    if (!node) return null;
    return (
      <TreeNode value={node.value} depth={depth} maxDepth={maxDepth}>
        {renderTree(node.left, depth + 1, maxDepth)}
        {renderTree(node.right, depth + 1, maxDepth)}
      </TreeNode>
    );
  };

  return (
    <Card>
      <CardHeader>Binary Tree Depth Visualization</CardHeader>
      <CardContent>
        <div
          style={{ display: "flex", justifyContent: "center", padding: "20px" }}
        >
          {renderTree(treeData)}
        </div>
        <p>Maximum Depth: 3</p>
      </CardContent>
    </Card>
  );
};

export default BinaryTreeVisualization;
```

This visualization demonstrates a binary tree with a maximum depth of 3. The tree is constructed based on Example 1 from the problem statement. Each node is represented by a circle containing its value, and the levels of the tree are clearly visible. This visual representation helps in understanding how the depth of the tree is calculated by counting the number of nodes along the longest path from the root to a leaf node.
