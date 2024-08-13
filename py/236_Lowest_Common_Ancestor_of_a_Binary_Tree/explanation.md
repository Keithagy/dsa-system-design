# Explanation: Lowest Common Ancestor of a Binary Tree

## Analysis of problem & input data

This problem is about finding the Lowest Common Ancestor (LCA) of two nodes in a binary tree. The key characteristics and insights of this problem are:

1. The tree is a binary tree, not necessarily a binary search tree.
2. The LCA is defined as the lowest node that has both given nodes as descendants.
3. A node can be a descendant of itself, which is a crucial point for edge cases.
4. The two nodes (p and q) are guaranteed to exist in the tree.
5. All node values are unique, which simplifies node identification.
6. The tree can be quite large (up to 10^5 nodes), so efficiency is important.

The key principle that makes this question approachable is the recursive nature of tree traversal. We can solve this problem by traversing the tree in a depth-first manner, looking for the two target nodes, and using the information from subtrees to determine the LCA.

### Test cases

Let's consider some important test cases:

1. Basic case: LCA is neither p nor q

   ```python
   #     3
   #    / \
   #   5   1
   #  / \
   # 6   2
   root = TreeNode(3)
   root.left = TreeNode(5)
   root.right = TreeNode(1)
   root.left.left = TreeNode(6)
   root.left.right = TreeNode(2)
   p, q = root.left, root.right  # 5 and 1
   # Expected output: 3
   ```

2. LCA is one of the nodes (p or q is ancestor of the other)

   ```python
   #     3
   #    / \
   #   5   1
   #  / \
   # 6   2
   #    / \
   #   7   4
   root = TreeNode(3)
   root.left = TreeNode(5)
   root.right = TreeNode(1)
   root.left.left = TreeNode(6)
   root.left.right = TreeNode(2)
   root.left.right.left = TreeNode(7)
   root.left.right.right = TreeNode(4)
   p, q = root.left, root.left.right.right  # 5 and 4
   # Expected output: 5
   ```

3. Nodes are in different subtrees

   ```python
   #     1
   #    / \
   #   2   3
   #  / \
   # 4   5
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   root.left.left = TreeNode(4)
   root.left.right = TreeNode(5)
   p, q = root.left.left, root.right  # 4 and 3
   # Expected output: 1
   ```

4. One node is the root

   ```python
   #     1
   #    / \
   #   2   3
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   p, q = root, root.left  # 1 and 2
   # Expected output: 1
   ```

5. Tree with only two nodes

   ```python
   #     1
   #    /
   #   2
   root = TreeNode(1)
   root.left = TreeNode(2)
   p, q = root, root.left  # 1 and 2
   # Expected output: 1
   ```

Here's the executable Python code for these test cases:

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def test_lowest_common_ancestor(lca_func):
    # Test case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    assert lca_func(root1, root1.left, root1.right).val == 3

    # Test case 2
    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(7)
    root2.left.right.right = TreeNode(4)
    assert lca_func(root2, root2.left, root2.left.right.right).val == 5

    # Test case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    assert lca_func(root3, root3.left.left, root3.right).val == 1

    # Test case 4
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    assert lca_func(root4, root4, root4.left).val == 1

    # Test case 5
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    assert lca_func(root5, root5, root5.left).val == 1

    print("All test cases passed!")

# You can run the test cases with your implementation like this:
# test_lowest_common_ancestor(your_lca_function)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Recursive DFS with bottom-up approach
2. Iterative solution with parent pointers
3. Iterative solution with path finding

3 solutions

#### Rejected solutions

1. Brute force approach of finding all paths
2. Using a Binary Search Tree (BST) specific algorithm

### Worthy Solutions

#### 1. Recursive DFS with bottom-up approach

This is the most elegant and efficient solution for this problem.

```python
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional[TreeNode]:
        # Base case: if we've reached None or found one of the nodes, return it
        if root is None or root == p or root == q:
            return root

        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right returned a node, this is the LCA
        if left and right:
            return root

        # If only one side returned a node, propagate it upwards
        return left if left else right
```

Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
Space Complexity: O(H), where H is the height of the tree. This is due to the recursion stack.

Key intuitions and invariants:

- The algorithm works bottom-up, which means it first reaches the deepest nodes and then backtracks.
- If a node is None or is one of p or q, we return it. This forms the base case of our recursion.
- For any other node, we recursively search its left and right subtrees.
- If both left and right subtrees return a non-None value, it means we've found our LCA.
- If only one side returns a non-None value, we propagate that value upwards.

#### 2. Iterative solution with parent pointers

This approach involves two passes through the tree.

```python
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional[TreeNode]:
        # Step 1: Create a parent pointer for each node
        stack = [root]
        parent = {root: None}

        # Continue until we've found both p and q
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Step 2: Backtrack from p until we find the LCA
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # Backtrack from q until we find a common ancestor
        while q not in ancestors:
            q = parent[q]

        return q
```

Time Complexity: O(N), where N is the number of nodes in the tree. We potentially visit each node twice.
Space Complexity: O(N) to store the parent pointers.

Key intuitions and invariants:

- We first create parent pointers for each node, allowing us to backtrack from any node to the root.
- We then use these parent pointers to find the first common ancestor when backtracking from both p and q.
- The use of a set to store ancestors allows for O(1) lookup time.

#### 3. Iterative solution with path finding

This approach finds the paths to both nodes and then compares them.

```python
from typing import Optional, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional[TreeNode]:
        def find_path(root: TreeNode, target: TreeNode) -> List[TreeNode]:
            path = []
            stack = [(root, [root])]

            while stack:
                node, current_path = stack.pop()
                if node == target:
                    return current_path

                if node.right:
                    stack.append((node.right, current_path + [node.right]))
                if node.left:
                    stack.append((node.left, current_path + [node.left]))

            return []  # Target not found

        path_p = find_path(root, p)
        path_q = find_path(root, q)

        # Find the last common node in both paths
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1

        return path_p[i-1]
```

Time Complexity: O(N), where N is the number of nodes in the tree. In the worst case, we might need to traverse the entire tree twice.
Space Complexity: O(N) to store the paths.

Key intuitions and invariants:

- We find the path from the root to each of the target nodes.
- The LCA is the last common node in these two paths.
- This approach is more intuitive but less efficient than the recursive solution.

### Rejected Approaches

1. Brute force approach of finding all paths:

   - This would involve finding all paths from the root to every leaf, then searching for paths containing p and q.
   - Rejected because it's highly inefficient, with a time complexity of O(N^2) in the worst case.

2. Using a Binary Search Tree (BST) specific algorithm:
   - While efficient for BSTs, this problem involves a general binary tree.
   - The BST property (left < root < right) doesn't hold here, so BST-specific algorithms won't work.

### Final Recommendations

The recursive DFS with bottom-up approach (Solution 1) is the best one to learn and use in an interview setting. It's concise, elegant, and efficient in both time and space complexity. It demonstrates a deep understanding of tree traversal and recursive problem-solving.

The iterative solutions (2 and 3) are worth understanding as they provide different perspectives on the problem. They might be preferred in scenarios where stack overflow is a concern due to very deep trees.

The brute force approach of finding all paths seems intuitive at first but is inefficient and should be avoided. Similarly, BST-specific algorithms are a trap here and should not be considered for this general binary tree problem.

## Visualization(s)

To visualize the recursive DFS approach, we can use a simple ASCII art representation:

```
       3
     /   \
    5     1
   / \   / \
  6   2 0   8
     / \
    7   4

Let's find LCA of 5 and 1:

1. Start at root (3)
2. Recursive call on left subtree (5)
   - 5 is found, return 5
3. Recursive call on right subtree (1)
   - 1 is found, return 1
4. Both left and right returned non-null, so 3 is the LCA

        3 (LCA)
      /   \
     5     1
   (found) (found)

```

This visualization helps to understand how the algorithm works its way up from the bottom, finding the lowest node where both target nodes are present in different subtrees.
