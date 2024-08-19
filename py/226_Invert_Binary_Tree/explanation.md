# Explanation: Invert Binary Tree

## Analysis of problem & input data

The "Invert Binary Tree" problem is a classic tree manipulation question that tests understanding of tree traversal and recursive problem-solving. Key aspects to consider:

1. Tree structure: The input is the root of a binary tree, where each node has at most two children.
2. Inversion process: Inverting the tree means swapping the left and right children of every node.
3. Recursion potential: The problem naturally lends itself to a recursive solution due to the tree's hierarchical structure.
4. In-place modification: The tree can be inverted in-place without creating a new tree structure.
5. Null handling: The solution must handle null nodes correctly, both as input and during traversal.
6. Return value: The problem asks to return the root of the inverted tree, which will be the same node object as the input root.

The key principle that makes this question simple is that inverting a binary tree is a recursive operation: if you can invert the left and right subtrees, you can invert the whole tree by swapping them.

### Test cases

1. Normal case:
   Input: root = [4,2,7,1,3,6,9]
   Output: [4,7,2,9,6,3,1]

2. Small tree:
   Input: root = [2,1,3]
   Output: [2,3,1]

3. Empty tree:
   Input: root = []
   Output: []

4. Single node tree:
   Input: root = [1]
   Output: [1]

5. Unbalanced tree:
   Input: root = [1,2,null,3]
   Output: [1,null,2,null,3]

6. Full binary tree:
   Input: root = [1,2,3,4,5,6,7]
   Output: [1,3,2,7,6,5,4]

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

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result[-1] is None:
        result.pop()
    return result

# Test cases
test_cases = [
    [4,2,7,1,3,6,9],
    [2,1,3],
    [],
    [1],
    [1,2,None,3],
    [1,2,3,4,5,6,7]
]

for case in test_cases:
    root = create_tree(case)
    # The invert_tree function would be called here
    # inverted_root = invert_tree(root)
    # print(tree_to_list(inverted_root))
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Recursive approach
2. Iterative approach using a stack
3. Iterative approach using a queue (level-order traversal)

3 solutions worth learning.

#### Rejected solutions

1. Creating a new inverted tree: While this would work, it's less efficient in terms of space complexity and not necessary given the problem statement.
2. Modifying the tree structure: Changing the tree to a different data structure (like a graph) and then inverting it would be overly complicated and inefficient.

### Worthy Solutions

#### 1. Recursive approach

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Base case: if the node is None, return None
    if not root:
        return None

    # Recursive case: swap the left and right children
    # The swap operation maintains the invariant that each subtree is inverted
    root.left, root.right = invertTree(root.right), invertTree(root.left)

    # Return the root of the inverted tree
    # This return value is crucial for the recursive calls above
    return root
```

Time complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (skewed tree), this could be O(n).

Intuitions and invariants:

- The base case (empty tree) is correctly handled, maintaining the invariant that an empty tree inverted is still an empty tree.
- The recursive calls ensure that all subtrees are inverted before the current node's children are swapped.
- The swapping operation at each node maintains the invariant that the subtree rooted at that node is correctly inverted.
- The return value of each recursive call is used to construct the inverted tree from bottom to top.

#### 2. Iterative approach using a stack

```python
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    # Use a stack to simulate the recursion
    stack = deque([root])

    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # Swap the left and right children
        # This maintains the invariant that each processed node is inverted
        node.left, node.right = node.right, node.left

        # Push the children onto the stack if they exist
        # This ensures we process all nodes in the tree
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return root
```

Time complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space complexity: O(w), where w is the maximum width of the tree. In the worst case (perfect binary tree), this could be O(n/2) ≈ O(n).

Intuitions and invariants:

- The stack mimics the recursion stack, allowing us to process nodes in a depth-first manner.
- Each node is processed (its children swapped) before its children are added to the stack, ensuring that the inversion happens from top to bottom.
- The order of pushing children onto the stack (right before left) doesn't affect the correctness but can affect the traversal order.
- The invariant that each processed node has its immediate children swapped is maintained throughout the algorithm.

#### 3. Iterative approach using a queue (level-order traversal)

```python
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    # Use a queue for level-order traversal
    queue = deque([root])

    while queue:
        # Dequeue the front node
        node = queue.popleft()

        # Swap the left and right children
        # This maintains the invariant that each level is inverted as we process it
        node.left, node.right = node.right, node.left

        # Enqueue the children if they exist
        # This ensures we process all nodes in the tree level by level
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root
```

Time complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
Space complexity: O(w), where w is the maximum width of the tree. In the worst case (perfect binary tree), this could be O(n/2) ≈ O(n).

Intuitions and invariants:

- The queue allows us to process nodes in a breadth-first (level-order) manner.
- Each level of the tree is fully processed before moving to the next level, ensuring that the inversion happens level by level.
- The invariant that each processed node has its immediate children swapped is maintained throughout the algorithm.
- This approach provides a different perspective on the tree inversion process, showing that it can be done in any traversal order.

### Rejected Approaches

1. Creating a new inverted tree: While this approach would work, it's less efficient in terms of space complexity (O(n) additional space) and not necessary given the problem statement. The question asks to invert the tree and return its root, implying an in-place modification.

2. Modifying the tree structure: Changing the binary tree to a different data structure (like a graph) and then inverting it would be overly complicated and inefficient. It would require additional time and space to convert the structure and then convert it back, without providing any benefits over the direct inversion approaches.

3. Using a hash map or other auxiliary data structures: The problem doesn't require keeping track of node values or positions separately, so using additional data structures would unnecessarily increase space complexity without improving the time complexity or simplifying the solution.

### Final Recommendations

The recursive approach (Solution 1) is the best one to learn and present in an interview setting for several reasons:

1. Simplicity: It's the most concise and easy-to-understand solution, clearly expressing the recursive nature of the problem.
2. Elegance: It directly maps to the problem statement and the structure of the tree.
3. Space efficiency: While it uses O(h) space on the call stack, this is often better than the O(w) space used by iterative approaches, especially for balanced trees.
4. Interview performance: It demonstrates understanding of recursion and tree structures, which are fundamental concepts in computer science.

The iterative approaches (Solutions 2 and 3) are also worth knowing:

- They demonstrate an understanding of how to convert recursive algorithms to iterative ones.
- They can be more efficient in languages that don't optimize tail recursion.
- They show familiarity with different tree traversal techniques (DFS and BFS).

Approaches that seem correct but aren't:

1. Only swapping the root's children: This would invert only the top level of the tree, not the entire structure.
2. Traversing the tree without swapping: Simply visiting all nodes without performing the swap operation wouldn't invert the tree.

Correct but not worth learning:

1. Morris traversal: While it achieves O(1) space complexity, it's overly complex for this problem and modifies the tree structure temporarily.
2. Threaded binary tree approach: This would require changing the tree structure and is unnecessarily complex for the given problem.

In conclusion, mastering the recursive approach and understanding the iterative alternatives provides a comprehensive grasp of the "Invert Binary Tree" problem, showcasing both depth of knowledge and problem-solving versatility in an interview setting.

## Visualization(s)

To visualize the inversion process, we can use a simple ASCII representation of a binary tree before and after inversion:

```
Original Tree:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Inverted Tree:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

This visualization helps to understand that:

1. The root node (4) stays in place.
2. The left and right subtrees are swapped.
3. This swapping process is applied recursively to all subtrees.

For a step-by-step visualization of the recursive process:

```
Step 1: Start with root
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Step 2: Invert left subtree
     4
   /   \
  2     7
 / \   / \
3   1 6   9

Step 3: Invert right subtree
     4
   /   \
  2     7
 / \   / \
3   1 9   6

Step 4: Swap left and right subtrees
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

This step-by-step process illustrates how the recursive approach builds the inverted tree from the bottom up, maintaining the invariant that each subtree is fully inverted before it's swapped at its parent node.
