## Explanation: Path Sum III

### Analysis of problem & input data

This problem is a classic tree traversal problem with a twist. It's about finding paths in a binary tree that sum up to a target value, but with the added complexity that the paths don't need to start at the root or end at a leaf. This characteristic makes it different from typical path sum problems and requires a more nuanced approach.

Key observations:

1. The path must be downwards, meaning we can only move from parent to child nodes.
2. The path can start and end anywhere in the tree, as long as it's continuous and downward.
3. The values in the tree can be positive or negative, and so can the target sum.
4. The tree can have up to 1000 nodes, so an efficient solution is necessary.

The main challenge here is keeping track of all possible paths and their sums efficiently. This problem falls into the category of "cumulative sum" problems, which often benefit from prefix sum techniques.

The key principle that makes this question simple is the use of prefix sums combined with a depth-first search (DFS) traversal. By maintaining a running sum and using a hash map to store prefix sums, we can efficiently count the number of valid paths without explicitly checking every possible path.

### Test cases

1. Basic case: A small tree with a simple path sum

   ```
   Input: root = [10,5,-3,3,2,null,11], targetSum = 8
   Output: 3
   ```

2. Empty tree:

   ```
   Input: root = [], targetSum = 0
   Output: 0
   ```

3. Single node tree, matching target:

   ```
   Input: root = [1], targetSum = 1
   Output: 1
   ```

4. Single node tree, not matching target:

   ```
   Input: root = [1], targetSum = 0
   Output: 0
   ```

5. Tree with negative values:

   ```
   Input: root = [1,-2,3], targetSum = -1
   Output: 1
   ```

6. Large tree with multiple valid paths:

   ```
   Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
   Output: 3
   ```

7. Tree with all zero values:

   ```
   Input: root = [0,0,0], targetSum = 0
   Output: 6
   ```

Here's the executable Python code for these test cases:

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
    ([10,5,-3,3,2,None,11], 8),
    ([], 0),
    ([1], 1),
    ([1], 0),
    ([1,-2,3], -1),
    ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22),
    ([0,0,0], 0)
]

# Function to run test cases (implementation of pathSum to be added later)
def run_tests(pathSum):
    for i, (values, target) in enumerate(test_cases, 1):
        root = create_tree(values)
        result = pathSum(root, target)
        print(f"Test case {i}: Input: root = {values}, targetSum = {target}")
        print(f"Output: {result}\n")

# Run tests
# run_tests(pathSum)  # Uncomment this line after implementing pathSum
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Prefix Sum with Hash Map (Neetcode solution)
2. Recursive DFS with Running Sum
3. Two-pass DFS (Brute Force)

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Dynamic Programming on Trees: While DP can be applied to tree problems, it's not the most efficient for this specific problem due to the arbitrary start and end points of paths.
2. BFS (Breadth-First Search): While BFS can traverse the tree, it's not well-suited for tracking paths from arbitrary start points to arbitrary end points.

#### Worthy Solutions

##### Prefix Sum with Hash Map (Neetcode solution)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> None:
            if not node:
                return

            # Update current sum
            curr_sum += node.val

            # If we've found a path, increment count
            if curr_sum - targetSum in prefix_sums:
                self.count += prefix_sums[curr_sum - targetSum]

            # Update prefix_sums
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            # Recurse on children
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # Backtrack: remove current sum from prefix_sums
            prefix_sums[curr_sum] -= 1

        self.count = 0
        prefix_sums = {0: 1}  # Initialize with 0 to handle paths starting from root
        dfs(root, 0)
        return self.count
```

Time Complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack and the prefix_sums dictionary. In the worst case (skewed tree), h can be n, making it O(n).

Explanation:

- We use a hash map (prefix_sums) to store the cumulative sum frequencies.
- As we traverse the tree, we keep track of the current sum (curr_sum).
- At each node, we check if curr_sum - targetSum exists in our prefix_sums. If it does, we've found path(s) that sum to targetSum.
- We update prefix_sums with the current sum.
- After processing a node and its subtrees, we backtrack by decrementing the count for the current sum in prefix_sums.

Key intuitions:

- The use of prefix sums allows us to efficiently find paths that sum to targetSum without explicitly checking every path.
- By storing cumulative sum frequencies, we can determine how many paths end at the current node with the desired sum.
- Backtracking ensures that we only consider paths in the current subtree.

##### Recursive DFS with Running Sum

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0

            # Count paths ending at this node
            count = 1 if curr_sum + node.val == targetSum else 0

            # Recurse on children, passing the updated sum
            count += dfs(node.left, curr_sum + node.val)
            count += dfs(node.right, curr_sum + node.val)

            return count

        def count_paths(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Count paths starting from this node
            return (
                dfs(node, 0) +
                count_paths(node.left) +
                count_paths(node.right)
            )

        return count_paths(root)
```

Time Complexity: O(n^2) in the worst case, where n is the number of nodes. For each node, we potentially traverse all its descendants.
Space Complexity: O(h), where h is the height of the tree, due to the recursion stack. In the worst case (skewed tree), this becomes O(n).

Explanation:

- We use two recursive functions: dfs and count_paths.
- dfs counts the number of paths that sum to targetSum and end at the current node.
- count_paths initiates a dfs call for each node in the tree, effectively considering all possible starting points.
- At each node, we check if the current path sums to targetSum and recurse on its children.

Key intuitions:

- By starting a new path at each node (via count_paths), we ensure we consider all possible starting points.
- The running sum allows us to efficiently check if we've found a valid path at each node.
- This approach is more intuitive but less efficient than the prefix sum method.

##### Two-pass DFS (Brute Force)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0

            # Count paths starting from this node
            return (
                (1 if node.val == target else 0) +
                dfs(node.left, target - node.val) +
                dfs(node.right, target - node.val)
            )

        if not root:
            return 0

        # Count paths starting from the root
        return (
            dfs(root, targetSum) +
            self.pathSum(root.left, targetSum) +
            self.pathSum(root.right, targetSum)
        )
```

Time Complexity: O(n^2) in the worst case, where n is the number of nodes. For each node, we potentially traverse all its descendants.
Space Complexity: O(h), where h is the height of the tree, due to the recursion stack. In the worst case (skewed tree), this becomes O(n).

Explanation:

- This solution uses a straightforward, brute-force approach.
- For each node, we start a DFS to find all paths summing to targetSum that start from that node.
- We then recursively apply this process to the left and right children.

Key intuitions:

- By starting a new search at each node, we ensure we consider all possible starting points.
- The recursive calls with target - node.val allow us to keep track of the remaining sum we need to find.
- This approach is intuitive but less efficient than the prefix sum method.

#### Rejected Approaches

1. Dynamic Programming on Trees:
   While DP can be powerful for tree problems, it's not ideal here because:

   - Paths can start and end at any node, making it difficult to define a clear subproblem structure.
   - The arbitrary nature of path start and end points doesn't align well with typical DP state definitions.

2. BFS (Breadth-First Search):
   BFS is not well-suited for this problem because:

   - It doesn't naturally maintain path information as it traverses level by level.
   - Keeping track of all possible paths from arbitrary start points would require significant additional complexity and memory usage.

3. Iterative DFS with Stack:
   While this approach could work, it's generally more complex to implement for this specific problem compared to the recursive solutions. The need to maintain path information explicitly on the stack makes it less intuitive and more error-prone.

#### Final Recommendations

The Prefix Sum with Hash Map solution (Neetcode solution) is the best to learn for several reasons:

1. It has the best time complexity (O(n)) among all solutions.
2. It demonstrates an advanced technique (prefix sums) that's applicable to many other problems.
3. It's space-efficient, using O(h) space where h is the height of the tree.
4. It solves the problem in a single pass through the tree.

While the other solutions are more intuitive, the prefix sum approach showcases a more sophisticated problem-solving technique that's valuable in coding interviews and real-world scenarios. Understanding this solution will enhance your problem-solving skills for a wide range of tree and cumulative sum problems.

### Visualization(s)

To visualize the Prefix Sum with Hash Map approach, we can use a simple tree diagram with annotations. Here's a textual representation:

```
       10 [PS: 10, C: 0]
      /  \
     /    \
    5      -3 [PS: 7, C: 1]
   / \      \
  3   2      11 [PS: 18, C: 1]
 / \   \
3  -2   1
[PS: 16, C: 1]

PS: Prefix Sum, C: Count of paths ending here

Hash Map:
{0: 1, 10: 1, 15: 1, 18: 1, 17: 1, 7: 1, 16: 1}
```

This visualization shows:

1. The tree structure with node values.
2. Annotations for each node showing the prefix sum (PS) at that point and the count of paths (C) ending at that node that sum to the target (assuming targetSum = 8).
3. The state of the hash map after traversing the tree.

This visual aids in understanding how the prefix sum is calculated and how the hash map is used to count valid paths efficiently.
