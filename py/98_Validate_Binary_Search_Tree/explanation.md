# Explanation: Validate Binary Search Tree

## Analysis of problem & input data

This problem requires us to validate whether a given binary tree is a valid Binary Search Tree (BST). The key aspects to consider are:

1. BST Property: For each node, all nodes in its left subtree must have values less than the node's value, and all nodes in its right subtree must have values greater than the node's value.

2. Recursive Nature: The BST property must hold for every node in the tree, not just the root.

3. Range Constraints: Each node's value must fall within a valid range, which changes as we traverse down the tree.

4. Input Constraints: The tree can have up to 10^4 nodes, and node values are 32-bit integers.

5. Edge Cases: We need to handle empty trees, single-node trees, and trees with duplicate values (which are not allowed in a BST).

The key principle that makes this question solvable is that a valid BST's in-order traversal yields a sorted list. However, directly using this property can be inefficient for large trees. Instead, we can leverage the BST property to define valid ranges for each node as we traverse the tree.

## Solutions

### Solution 1: Recursive Range Checking

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: Optional[int] = None, high: Optional[int] = None) -> bool:
            # An empty tree is considered valid
            if not node:
                return True

            # Check if the current node's value is within the valid range
            if (low is not None and node.val <= low) or (high is not None and node.val >= high):
                return False

            # Recursively validate left and right subtrees
            # For left subtree, update high bound to current node's value
            # For right subtree, update low bound to current node's value
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Start the validation from the root with no initial bounds
        return validate(root)
```

This solution uses a recursive approach with the following characteristics:

- Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
- Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (skewed tree), it can be O(n).

Key intuitions and invariants:

- We maintain a valid range for each node as we traverse down the tree.
- The range starts unbounded (-inf, +inf) at the root and narrows down for each child.
- For a left child, we update the upper bound to be the parent's value.
- For a right child, we update the lower bound to be the parent's value.
- If at any point a node's value falls outside its valid range, the tree is not a valid BST.

### Solution 2: Iterative Inorder Traversal

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float('-inf')

        # Perform an iterative inorder traversal
        while stack or root:
            # Traverse to the leftmost node
            while root:
                stack.append(root)
                root = root.left

            # Process the current node
            root = stack.pop()

            # Check if the current value is greater than the previous value
            if root.val <= prev:
                return False

            # Update the previous value and move to the right subtree
            prev = root.val
            root = root.right

        return True
```

This solution uses an iterative inorder traversal approach:

- Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
- Space Complexity: O(h), where h is the height of the tree. This is due to the stack used for iterative traversal. In the worst case (skewed tree), it can be O(n).

Key intuitions and invariants:

- An inorder traversal of a valid BST produces values in ascending order.
- We keep track of the previously visited node's value.
- If at any point the current node's value is not greater than the previous value, the tree is not a valid BST.

## Recommendation

I recommend learning and mastering the Recursive Range Checking solution (Solution 1) for the following reasons:

1. It's more intuitive and directly applies the BST property.
2. It's easier to explain in an interview setting.
3. It can be easily extended to handle additional constraints or variations of the problem.
4. It demonstrates a good understanding of recursion and tree traversal.

While the Iterative Inorder Traversal solution is also valid and efficient, it relies on the property that an inorder traversal of a BST produces a sorted list, which might not be immediately obvious to all interviewers.

## Test cases

```python
def test_isValidBST():
    solution = Solution()

    # Test case 1: Valid BST
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    assert solution.isValidBST(root1) == True

    # Test case 2: Invalid BST
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    assert solution.isValidBST(root2) == False

    # Test case 3: Single node tree
    root3 = TreeNode(1)
    assert solution.isValidBST(root3) == True

    # Test case 4: Empty tree
    assert solution.isValidBST(None) == True

    # Test case 5: BST with duplicate values
    root5 = TreeNode(2)
    root5.left = TreeNode(2)
    root5.right = TreeNode(2)
    assert solution.isValidBST(root5) == False

    # Test case 6: Large valid BST
    root6 = TreeNode(5)
    root6.left = TreeNode(3)
    root6.right = TreeNode(7)
    root6.left.left = TreeNode(1)
    root6.left.right = TreeNode(4)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(8)
    assert solution.isValidBST(root6) == True

    print("All test cases passed!")

test_isValidBST()
```

## Overview of rejected approaches

1. Checking only immediate children:

   - Approach: Verify that for each node, its left child is smaller and its right child is larger.
   - Why it fails: This doesn't account for the entire subtree. A node might satisfy this condition for its immediate children, but violate the BST property further down the tree.

2. Using global variables for prev_value:

   - Approach: Use a global variable to keep track of the previously visited node in an inorder traversal.
   - Why it's not recommended: While this can work, it's generally discouraged in interviews as it makes the code less clear and can lead to issues with concurrent executions or multiple test cases.

3. Collecting all values and then checking if sorted:

   - Approach: Perform an inorder traversal to collect all values, then check if the resulting list is sorted.
   - Why it's not optimal: While correct, this requires O(n) extra space to store all values, which is unnecessary. It also doesn't leverage the BST property as efficiently as other methods.

4. Using the min and max values of subtrees:
   - Approach: For each node, calculate the max value in its left subtree and the min value in its right subtree.
   - Why it's not efficient: This requires multiple passes through the tree, resulting in a time complexity of O(n^2) in the worst case.

## Visualization(s)

To visualize the recursive range checking algorithm, we can use a simple React component to show how the valid range narrows down as we traverse the tree. Here's a basic implementation:

```tsx
import React, { useState } from "react";

const TreeNode = ({ value, low, high, left, right }) => (
  <div className="flex flex-col items-center">
    <div
      className={`w-12 h-12 rounded-full border-2 flex items-center justify-center ${(low === null || value > low) && (high === null || value < high) ? "border-green-500" : "border-red-500"}`}
    >
      {value}
    </div>
    <div className="text-xs mt-1">
      Range: [{low === null ? "-∞" : low}, {high === null ? "∞" : high}]
    </div>
    {(left || right) && (
      <div className="flex mt-4">
        {left && <TreeNode {...left} low={low} high={value} />}
        {right && <TreeNode {...right} low={value} high={high} />}
      </div>
    )}
  </div>
);

const BSTValidator = () => {
  const [root] = useState({
    value: 5,
    left: {
      value: 3,
      left: { value: 1 },
      right: { value: 4 },
    },
    right: {
      value: 7,
      left: { value: 6 },
      right: { value: 8 },
    },
  });

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">BST Validation Visualizer</h2>
      <TreeNode {...root} low={null} high={null} />
    </div>
  );
};

export default BSTValidator;
```

This visualization shows a binary search tree with nodes colored green if they're within the valid range for their position, and red if they're outside the valid range. The valid range for each node is displayed below it, showing how the range narrows as we move down the tree.

To use this visualization, you would render the `BSTValidator` component in your React application. You can modify the initial state in the `useState` hook to visualize different tree structures or invalid BSTs.
