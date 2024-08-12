# Explanation: Validate Binary Search Tree

## Analysis of problem & input data

This problem is about validating whether a given binary tree is a valid Binary Search Tree (BST). The key characteristics and insights of this problem are:

1. BST Property: In a BST, for any given node, all nodes in its left subtree must have values less than the node's value, and all nodes in its right subtree must have values greater than the node's value.

2. Recursive Structure: The BST property must hold for every node in the tree, not just the root. This suggests a recursive approach might be suitable.

3. Range Checking: As we traverse down the tree, we can keep track of the valid range of values for each node. This range gets updated as we move left (upper bound decreases) or right (lower bound increases).

4. Inorder Traversal Property: A key insight is that an inorder traversal of a valid BST will yield a sorted list of values. This can be leveraged for an elegant solution.

5. Integer Overflow: The problem constraints mention that node values can be as large as 2^31 - 1 or as small as -2^31. This means we need to be careful about integer overflow when setting initial bounds.

The key principle that makes this question conceptually simple is the recursive nature of the BST property. If we can ensure that this property holds for each node with respect to its immediate children, and we apply this check recursively, we can validate the entire tree.

### Test cases

Here are some test cases to consider:

1. Basic valid BST:

   ```
   [2,1,3]
   ```

2. Invalid BST with right child smaller than root:

   ```
   [5,1,4,null,null,3,6]
   ```

3. Single node tree:

   ```
   [1]
   ```

4. Tree with duplicate values (invalid BST):

   ```
   [1,1]
   ```

5. Tree with negative values:

   ```
   [-2147483648]
   ```

6. Tree with maximum allowed value:

   ```
   [2147483647]
   ```

7. Valid BST with multiple levels:

   ```
   [4,2,6,1,3,5,7]
   ```

8. Invalid BST where property is violated deep in the tree:

   ```
   [5,4,7,null,null,6,8,null,null,3,9]
   ```

Here's the Python code to define these test cases:

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
    create_tree([2,1,3]),
    create_tree([5,1,4,None,None,3,6]),
    create_tree([1]),
    create_tree([1,1]),
    create_tree([-2147483648]),
    create_tree([2147483647]),
    create_tree([4,2,6,1,3,5,7]),
    create_tree([5,4,7,None,None,6,8,None,None,3,9])
]

# Function to run tests (to be implemented with the solution)
def run_tests(is_valid_bst_func):
    for i, case in enumerate(test_cases):
        result = is_valid_bst_func(case)
        print(f"Test case {i+1}: {'Valid' if result else 'Invalid'} BST")

```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Recursive approach with range checking
2. Iterative approach with stack (simulating recursion)
3. Inorder traversal approach

Count: 3 solutions

#### Rejected solutions

1. Checking only immediate children
2. Using a global variable to track the previous node's value

### Worthy Solutions

#### 1. Recursive approach with range checking

This approach involves recursively checking each node while maintaining a valid range for its value.

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            # An empty tree is valid
            if not node:
                return True

            # Check if the current node's value is within the valid range
            if node.val <= low or node.val >= high:
                return False

            # Recursively check left and right subtrees
            # For left subtree, update the high bound to the current node's value
            # For right subtree, update the low bound to the current node's value
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root)

# Test the solution
solution = Solution()
# Assuming test_cases is defined as in the previous code
for i, case in enumerate(test_cases):
    result = solution.isValidBST(case)
    print(f"Test case {i+1}: {'Valid' if result else 'Invalid'} BST")

```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (skewed tree), this could be O(n).

Key intuitions and invariants:

- We maintain a valid range for each node as we traverse the tree.
- The range gets narrower as we go deeper into the tree.
- We use float('-inf') and float('inf') as initial bounds to handle the full range of integer values.
- The BST property must hold for every node, not just in relation to its immediate children.

#### 2. Iterative approach with stack

This approach simulates the recursion using a stack, which can be beneficial for very deep trees to avoid stack overflow.

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, low, high = stack.pop()

            if node.val <= low or node.val >= high:
                return False

            if node.right:
                stack.append((node.right, node.val, high))
            if node.left:
                stack.append((node.left, low, node.val))

        return True

# Test the solution
solution = Solution()
# Assuming test_cases is defined as in the previous code
for i, case in enumerate(test_cases):
    result = solution.isValidBST(case)
    print(f"Test case {i+1}: {'Valid' if result else 'Invalid'} BST")

```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
Space Complexity: O(h), where h is the height of the tree. In the worst case (skewed tree), this could be O(n).

Key intuitions and invariants:

- We use a stack to keep track of nodes to visit, along with their valid ranges.
- The stack simulates the recursion stack, allowing us to traverse the tree depth-first.
- We process the right child before the left child to maintain the correct order of visitation.
- The valid range for each node is updated as we traverse down the tree.

#### 3. Inorder traversal approach

This approach leverages the property that an inorder traversal of a BST should yield a sorted list.

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            nonlocal prev
            if not node:
                return True

            if not inorder(node.left):
                return False

            if node.val <= prev:
                return False
            prev = node.val

            return inorder(node.right)

        prev = float('-inf')
        return inorder(root)

# Test the solution
solution = Solution()
# Assuming test_cases is defined as in the previous code
for i, case in enumerate(test_cases):
    result = solution.isValidBST(case)
    print(f"Test case {i+1}: {'Valid' if result else 'Invalid'} BST")

```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
Space Complexity: O(h), where h is the height of the tree, due to the recursion stack. In the worst case (skewed tree), this could be O(n).

Key intuitions and invariants:

- An inorder traversal of a valid BST should yield values in ascending order.
- We keep track of the previously visited node's value and ensure that the current node's value is always greater.
- We use float('-inf') as the initial previous value to handle the first node correctly.
- This approach elegantly combines the BST property check with the traversal itself.

### Rejected Approaches

1. Checking only immediate children: This approach would only verify that each node's value is greater than its left child and less than its right child. However, it fails to catch cases where the BST property is violated by nodes further down the tree. For example, it would incorrectly validate the tree [5,1,4,null,null,3,6].

2. Using a global variable to track the previous node's value: While this can work, it's generally considered bad practice in interview settings as it relies on side effects and can make the code harder to understand and maintain. The inorder traversal approach we discussed achieves the same result more cleanly.

3. Storing all values in an array and then checking if the array is sorted: While this would work, it unnecessarily uses O(n) extra space, when we can achieve the same result with O(1) extra space (excluding the recursion stack) using the inorder traversal approach.

### Final Recommendations

The recursive approach with range checking (Solution 1) is recommended as the best solution to learn and present in an interview setting. Here's why:

1. It directly implements the BST property in a way that's easy to understand and explain.
2. It's efficient in both time and space complexity.
3. It handles all edge cases, including potential integer overflow issues.
4. It demonstrates a good understanding of tree traversal and recursive problem-solving.

The inorder traversal approach (Solution 3) is also excellent and worth knowing, as it leverages a fundamental property of BSTs. It's slightly more elegant but might be less intuitive to come up with in an interview setting.

The iterative approach (Solution 2) is good to know as an alternative, especially if you're asked about handling very deep trees where stack overflow might be a concern with recursion.

When discussing this problem, it's worth mentioning that while checking only immediate children might seem correct at first glance, it fails to catch violations deeper in the tree. This demonstrates an understanding of the importance of considering edge cases and thinking through the problem thoroughly.

## Visualization(s)

To visualize the recursive range-checking approach, we can use a simple tree diagram with annotations:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300">
  <!-- Tree structure -->
  <line x1="250" y1="50" x2="150" y2="100" stroke="black" />
  <line x1="250" y1="50" x2="350" y2="100" stroke="black" />
  <line x1="150" y1="100" x2="100" y2="150" stroke="black" />
  <line x1="150" y1="100" x2="200" y2="150" stroke="black" />
  <line x1="350" y1="100" x2="300" y2="150" stroke="black" />
  <line x1="350" y1="100" x2="400" y2="150" stroke="black" />

  <!-- Nodes -->
  <circle cx="250" cy="50" r="20" fill="white" stroke="black" />
  <circle cx="150" cy="100" r="20" fill="white" stroke="black" />
  <circle cx="350" cy="100" r="20" fill="white" stroke="black" />
  <circle cx="100" cy="150" r="20" fill="white" stroke="black" />
  <circle cx="200" cy="150" r="20" fill="white" stroke="black" />
  <circle cx="300" cy="150" r="20" fill="white" stroke="black" />
  <circle cx="400" cy="150" r="20" fill="white" stroke="black" />

  <!-- Node values -->
  <text x="250" y="55" text-anchor="middle" font-size="14">8</text>
  <text x="150" y="105" text-anchor="middle" font-size="14">3</text>
  <text x="350" y="105" text-anchor="middle" font-size="14">10</text>
  <text x="100" y="155" text-anchor="middle" font-size="14">1</text>
  <text x="200" y="155" text-anchor="middle" font-size="14">6</text>
  <text x="300" y="155" text-anchor="middle" font-size="14">9</text>
  <text x="400" y="155" text-anchor="middle" font-size="14">14</text>

  <!-- Range annotations -->
```
