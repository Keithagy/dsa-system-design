## Explanation: Path Sum II

### Analysis of problem & input data

This problem is a classic tree traversal problem with a twist of path sum calculation. The key characteristics of this problem are:

1. We're dealing with a binary tree, which implies a recursive structure.
2. We need to find all root-to-leaf paths, indicating a depth-first search (DFS) approach.
3. We need to keep track of the sum along each path.
4. We're only interested in paths that end at a leaf node (a node with no children).
5. The problem asks for the node values in the path, not the node references.

The key principle that makes this question simple is the recursive nature of trees. We can solve this problem by recursively traversing the tree, keeping track of the current path and sum, and only adding the path to our result when we reach a leaf node with the correct sum.

This problem falls into the category of backtracking problems, where we explore all possible paths and backtrack when necessary. It's also a good example of how to use a preorder traversal (root, left, right) to solve tree problems.

### Test cases

Here are some relevant test cases:

1. Normal case: A tree with multiple valid paths (as in Example 1)
2. No valid paths: A tree where no path sums to the target (as in Example 2)
3. Empty tree: An empty tree (root is None)
4. Single node tree: A tree with only one node
5. Negative values: A tree with negative values, where the path can go up and down
6. Large tree: A tree with many nodes to test performance

Here's the Python code for these test cases:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test_path_sum_ii(path_sum_ii_func):
    # Test case 1: Normal case
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.left = TreeNode(5)
    root1.right.right.right = TreeNode(1)
    assert path_sum_ii_func(root1, 22) == [[5,4,11,2], [5,8,4,5]]

    # Test case 2: No valid paths
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    assert path_sum_ii_func(root2, 5) == []

    # Test case 3: Empty tree
    assert path_sum_ii_func(None, 0) == []

    # Test case 4: Single node tree
    root4 = TreeNode(1)
    assert path_sum_ii_func(root4, 1) == [[1]]
    assert path_sum_ii_func(root4, 0) == []

    # Test case 5: Negative values
    root5 = TreeNode(1)
    root5.left = TreeNode(-2)
    root5.right = TreeNode(3)
    assert path_sum_ii_func(root5, -1) == [[1,-2]]

    print("All test cases passed!")

# You would call this function with your implementation:
# test_path_sum_ii(path_sum_ii)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Recursive DFS with backtracking (Neetcode solution)
2. Iterative DFS using a stack
3. Recursive DFS with global result list

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Breadth-First Search (BFS): While BFS can traverse the tree, it's not well-suited for this problem as we need to track complete paths from root to leaf.
2. Dynamic Programming: This problem doesn't have overlapping subproblems that could benefit from DP.

#### Worthy Solutions

##### Recursive DFS with backtracking (Neetcode solution)

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], target: int, path: List[int], result: List[List[int]]) -> None:
            if not node:
                return

            # Add current node to the path
            path.append(node.val)

            # Check if it's a leaf node and the sum matches the target
            if not node.left and not node.right and target == node.val:
                result.append(path[:])  # Make a copy of the current path

            # Recursively check left and right subtrees
            dfs(node.left, target - node.val, path, result)
            dfs(node.right, target - node.val, path, result)

            # Backtrack: remove the current node from path
            path.pop()

        result = []
        dfs(root, targetSum, [], result)
        return result
```

Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
Space Complexity: O(H), where H is the height of the tree. This space is used by the recursion stack. In the worst case of a skewed tree, this could be O(N).

Explanation:

- We use a depth-first search (DFS) approach to traverse the tree.
- At each node, we add its value to the current path and subtract it from the remaining target sum.
- If we reach a leaf node and the remaining target is zero, we've found a valid path.
- We use backtracking by removing the current node from the path after exploring its subtrees.

Key points:

- The use of a mutable list (`path`) for efficiency, with copying only when a solution is found.
- Backtracking to explore all possible paths.
- The recursive nature mirrors the tree structure, making the solution intuitive.

##### Iterative DFS using a stack

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        result = []
        stack = [(root, [root.val], targetSum - root.val)]

        while stack:
            node, path, remaining = stack.pop()

            # Check if it's a leaf node and the sum matches the target
            if not node.left and not node.right and remaining == 0:
                result.append(path)

            # Add right child to stack (it will be processed after left)
            if node.right:
                stack.append((node.right, path + [node.right.val], remaining - node.right.val))

            # Add left child to stack
            if node.left:
                stack.append((node.left, path + [node.left.val], remaining - node.left.val))

        return result
```

Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
Space Complexity: O(H), where H is the height of the tree. In the worst case of a skewed tree, this could be O(N).

Explanation:

- We use an iterative depth-first search approach using a stack.
- Each stack entry contains the current node, the path to that node, and the remaining sum needed.
- We process the left subtree before the right subtree by pushing the right child first.
- When we reach a leaf node with the correct sum, we add the path to our result.

Key points:

- Avoids recursion, which can be beneficial for very deep trees to prevent stack overflow.
- Uses more memory than the recursive approach due to storing complete paths in the stack.
- Easier to understand for those more comfortable with iterative approaches.

##### Recursive DFS with global result list

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], target: int, path: List[int]) -> None:
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and target == node.val:
                self.result.append(path[:])
            else:
                dfs(node.left, target - node.val, path)
                dfs(node.right, target - node.val, path)

            path.pop()

        self.result = []
        dfs(root, targetSum, [])
        return self.result
```

Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node once.
Space Complexity: O(H), where H is the height of the tree. This space is used by the recursion stack. In the worst case of a skewed tree, this could be O(N).

Explanation:

- This solution is similar to the first recursive solution, but uses a class variable `self.result` to store the result.
- We perform a depth-first search, updating the path and remaining target sum as we go.
- When we reach a leaf node with the correct sum, we add a copy of the current path to the result.

Key points:

- Uses a class variable to avoid passing the result list through recursive calls.
- Still employs backtracking by removing the current node from the path after exploring its subtrees.
- Slightly more concise than the first recursive solution, but potentially less clear due to the use of a class variable.

#### Rejected Approaches

1. Breadth-First Search (BFS): While BFS can traverse the tree level by level, it's not well-suited for this problem. BFS would require storing complete paths for each node in the queue, leading to higher space complexity. Moreover, BFS doesn't naturally lend itself to backtracking, which is crucial for this problem.

2. Dynamic Programming: This problem doesn't exhibit overlapping subproblems that could benefit from memoization. Each path from root to leaf is unique, and we need to find all such paths, not just determine if a path exists or find the optimal path.

3. Brute Force (generate all paths): While it would work, generating all possible paths and then filtering for those that sum to the target would be inefficient, especially for large trees. It would have a time complexity of O(2^N) in the worst case for a full binary tree.

#### Final Recommendations

The recursive DFS with backtracking (Neetcode solution) is the recommended approach for several reasons:

1. It's intuitive and closely mirrors the problem structure.
2. It has optimal time and space complexity.
3. It uses backtracking efficiently, exploring all paths without unnecessary memory usage.
4. It's a common pattern in tree problems, making it valuable to master for similar questions.

The iterative solution is a good alternative to know, especially if you're concerned about stack overflow for very deep trees. The recursive solution with a global result list is slightly more concise but potentially less clear due to the use of a class variable.

### Visualization(s)

To visualize the recursive DFS with backtracking, we can use a simple ASCII representation:

```
         5
       /   \
      4     8
     /     / \
    11    13  4
   /  \      / \
  7    2    5   1

Path: [5]
Path: [5, 4]
Path: [5, 4, 11]
Path: [5, 4, 11, 7]  // Backtrack
Path: [5, 4, 11, 2]  // Found! Sum = 22
Path: [5, 4]  // Backtrack
Path: [5]  // Backtrack
Path: [5, 8]
Path: [5, 8, 13]  // Backtrack
Path: [5, 8, 4]
Path: [5, 8, 4, 5]  // Found! Sum = 22
Path: [5, 8, 4, 1]  // Backtrack
```

This visualization shows how the algorithm explores each path, backtracking when necessary, and identifies the two paths that sum to 22.
