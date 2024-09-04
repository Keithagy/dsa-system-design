## Explanation: Inorder Successor in BST

### Analysis of problem & input data

This problem involves finding the in-order successor of a given node in a Binary Search Tree (BST). The key principle that makes this question simpler is understanding the properties of a BST and how in-order traversal works in a BST.

1. BST Property: For any node, all nodes in its left subtree have smaller values, and all nodes in its right subtree have larger values.
2. In-order Traversal: In a BST, in-order traversal visits nodes in ascending order of their values.
3. Successor Definition: The in-order successor is the node with the smallest value greater than the given node's value.

Given these properties, we can deduce that:

- If the node has a right subtree, the successor is the leftmost node in that right subtree.
- If the node doesn't have a right subtree, the successor is the nearest ancestor for which the given node would be in its left subtree.

This problem is about pattern-matching to BST traversal strategies and leveraging BST properties to find the successor efficiently.

### Test cases

1. Normal case: BST with multiple nodes, successor exists
2. Root node: Find successor of the root
3. Leftmost node: Find successor of the smallest value
4. Rightmost node: Find successor of the largest value (should return null)
5. Node with right child: Successor should be leftmost in right subtree
6. Node without right child: Successor should be an ancestor
7. Single node tree: Should return null for any input

Here's the Python code for these test cases:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderSuccessor(root: TreeNode, p: TreeNode) -> TreeNode:
    # Implementation goes here
    pass

# Test case 1: Normal case
root1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
p1 = root1.left.right  # Node with value 4
assert inorderSuccessor(root1, p1).val == 5

# Test case 2: Root node
p2 = root1  # Node with value 5
assert inorderSuccessor(root1, p2).val == 6

# Test case 3: Leftmost node
p3 = root1.left.left  # Node with value 2
assert inorderSuccessor(root1, p3).val == 3

# Test case 4: Rightmost node
p4 = root1.right.right  # Node with value 8
assert inorderSuccessor(root1, p4) is None

# Test case 5: Node with right child
p5 = root1.left  # Node with value 3
assert inorderSuccessor(root1, p5).val == 4

# Test case 6: Node without right child
root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), None), TreeNode(6))
p6 = root2.left.left.left  # Node with value 1
assert inorderSuccessor(root2, p6).val == 2

# Test case 7: Single node tree
root3 = TreeNode(1)
p7 = root3
assert inorderSuccessor(root3, p7) is None

print("All test cases passed!")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Recursive BST traversal (Neetcode solution)
2. Iterative BST traversal
3. Parent pointer approach (if parent pointers are available)

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Full in-order traversal and array storage: This approach would work but is not optimal in terms of time and space complexity.
2. Morris traversal: While this provides O(1) space complexity, it modifies the tree structure temporarily, which might not be allowed in an interview setting.

#### Worthy Solutions

##### Recursive BST traversal (Neetcode solution)

```python
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None

        while root:
            if p.val >= root.val:
                # If p's value is greater than or equal to the current node,
                # the successor must be in the right subtree
                root = root.right
            else:
                # If p's value is less than the current node,
                # this node is a potential successor
                successor = root
                root = root.left

        return successor
```

Time Complexity: O(H), where H is the height of the tree. In the worst case (skewed tree), this could be O(N), where N is the number of nodes. In a balanced BST, it would be O(log N).
Space Complexity: O(1), as we're using constant extra space.

Explanation:

- This solution leverages the BST property to efficiently find the successor.
- We traverse the tree from root to leaf, making decisions at each step:
  - If p's value is greater than or equal to the current node, we know the successor must be in the right subtree (if it exists).
  - If p's value is less than the current node, this node could be a potential successor, so we update our successor candidate and continue searching in the left subtree.
- The algorithm maintains the invariant that `successor` always holds the smallest value greater than p.val that we've seen so far.
- When we reach a null node, we've found the successor (or confirmed there isn't one if `successor` is still null).

##### Iterative BST traversal

```python
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        # Step 1: Find the target node
        current = root
        while current and current.val != p.val:
            if p.val < current.val:
                current = current.left
            else:
                current = current.right

        # Step 2: If right subtree exists, find the minimum in right subtree
        if current and current.right:
            current = current.right
            while current.left:
                current = current.left
            return current

        # Step 3: If no right subtree, find the nearest ancestor for which p would be in left subtree
        ancestor = root
        successor = None
        while ancestor != p:
            if p.val < ancestor.val:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right

        return successor
```

Time Complexity: O(H), where H is the height of the tree. In the worst case (skewed tree), this could be O(N), where N is the number of nodes. In a balanced BST, it would be O(log N).
Space Complexity: O(1), as we're using constant extra space.

Explanation:

- This solution breaks down the problem into three steps:
  1. Find the target node: We traverse the BST to locate the node p.
  2. If the node has a right subtree, the successor is the leftmost node in that subtree.
  3. If the node doesn't have a right subtree, we need to find the nearest ancestor for which p would be in its left subtree.
- The algorithm maintains two invariants:
  1. In step 2, the leftmost node in the right subtree is always the successor.
  2. In step 3, the `successor` variable always holds the most recent ancestor where we went left.
- This approach is more intuitive and closely follows the definition of an in-order successor in a BST.

##### Parent pointer approach

```python
class Solution:
    def inorderSuccessor(self, p: TreeNode) -> Optional[TreeNode]:
        # If right subtree exists, return leftmost node of right subtree
        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr

        # If no right subtree, go up until we're on left instead of right
        curr = p
        parent = p.parent
        while parent and parent.right == curr:
            curr = parent
            parent = parent.parent
        return parent
```

Time Complexity: O(H), where H is the height of the tree. In the worst case (skewed tree), this could be O(N), where N is the number of nodes. In a balanced BST, it would be O(log N).
Space Complexity: O(1), as we're using constant extra space.

Explanation:

- This solution assumes that each node has a parent pointer.
- The algorithm has two main parts:
  1. If the node has a right child, we find the leftmost node in the right subtree.
  2. If the node doesn't have a right child, we go up the parent pointers until we find a parent where we came from its left subtree.
- The algorithm maintains two invariants:
  1. In the first part, the leftmost node in the right subtree is always the successor.
  2. In the second part, we keep moving up until we find the first ancestor where the current node is in its left subtree.
- This approach is very efficient if parent pointers are available, as it doesn't require traversing from the root.

#### Rejected Approaches

1. Full in-order traversal and array storage:

   - This approach involves performing a complete in-order traversal of the BST, storing all nodes in an array, then finding the successor.
   - While correct, it's not optimal as it uses O(N) time and O(N) space, where N is the number of nodes in the tree.
   - It doesn't leverage the BST property efficiently and processes unnecessary nodes.

2. Morris traversal:
   - This approach provides O(1) space complexity by temporarily modifying the tree structure.
   - However, it's generally not recommended in interview settings as it alters the input data structure.
   - It's also more complex to implement and understand compared to the other solutions.

#### Final Recommendations

The recursive BST traversal (Neetcode solution) is the best to learn for this problem. It's concise, efficient, and directly leverages the BST property. It has optimal time complexity O(H) and space complexity O(1). This solution demonstrates a deep understanding of BST properties and is likely to impress in an interview setting.

The iterative BST traversal is also worth learning as it provides a more step-by-step approach that closely follows the definition of an in-order successor. It's slightly more verbose but might be easier to explain in an interview.

The parent pointer approach is good to know conceptually, but it's less commonly applicable as many BST implementations don't include parent pointers.

### Visualization(s)

For this problem, a visual representation of a BST with arrows showing the succession order would be helpful. Here's a simple ASCII representation:

```
        5
      /   \
     3     7
    / \   / \
   2   4 6   8
  /
 1

In-order traversal: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
```

This visualization helps to understand:

1. The in-order traversal of a BST visits nodes in ascending order.
2. For a node with a right subtree (e.g., 5), the successor is the leftmost node in that subtree (6).
3. For a node without a right subtree (e.g., 4), the successor is the first ancestor for which this node is in the left subtree (5).
