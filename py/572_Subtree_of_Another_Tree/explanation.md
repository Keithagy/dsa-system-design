# Explanation: Subtree of Another Tree

## Analysis of problem & input data

This problem involves comparing two binary trees to determine if one is a subtree of the other. Key aspects to consider:

1. Tree structure: We're dealing with binary trees, which have a hierarchical structure.
2. Node values: Each node has an integer value within the range [-10^4, 10^4].
3. Size constraints: The root tree can have 1 to 2000 nodes, while the subRoot tree can have 1 to 1000 nodes.
4. Subtree definition: A subtree includes a node and all its descendants.
5. Equality condition: For subRoot to be a subtree of root, it must have the same structure and node values.

The key principle that makes this question approachable is that tree equality can be checked recursively. If we can determine whether two trees are identical, we can apply this check at each node of the larger tree to find a potential subtree match.

Pattern matching:

- This problem falls into the category of tree traversal and comparison.
- It combines aspects of "same tree" and "tree search" problems.
- The solution will likely involve a depth-first search (DFS) approach, either through recursion or using a stack.

## Solutions

### Solution 1: Recursive DFS with Helper Function

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: if root is None, subRoot can't be a subtree
        if not root:
            return False

        # Check if the current root matches the subRoot
        if self.is_same_tree(root, subRoot):
            return True

        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are the same
        if not p and not q:
            return True
        # If one node is None and the other isn't, trees are different
        if not p or not q:
            return False
        # Check if current nodes have same value and recursively check subtrees
        return (p.val == q.val and
                self.is_same_tree(p.left, q.left) and
                self.is_same_tree(p.right, q.right))
```

Time Complexity: O(m \* n), where m is the number of nodes in root and n is the number of nodes in subRoot.
Space Complexity: O(h), where h is the height of the root tree (due to recursion stack).

Intuition and invariants:

- We traverse every node in the root tree, treating each as a potential match for subRoot.
- The is_same_tree helper function checks if two trees are identical in structure and values.
- We leverage the recursive nature of trees: if two nodes are the same and their left and right subtrees are the same, then the entire trees are the same.

### Solution 2: Serialization and KMP Algorithm

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "null"
            return f"#{node.val}{serialize(node.left)}{serialize(node.right)}"

        def kmp(text, pattern):
            def build_lps(pattern):
                lps = [0] * len(pattern)
                length = 0
                i = 1
                while i < len(pattern):
                    if pattern[i] == pattern[length]:
                        length += 1
                        lps[i] = length
                        i += 1
                    else:
                        if length != 0:
                            length = lps[length - 1]
                        else:
                            lps[i] = 0
                            i += 1
                return lps

            lps = build_lps(pattern)
            i = j = 0
            while i < len(text):
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                    if j == len(pattern):
                        return True
                elif i < len(text) and text[i] != pattern[j]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return False

        # Serialize both trees
        root_str = serialize(root)
        subRoot_str = serialize(subRoot)

        # Use KMP to check if subRoot_str is a substring of root_str
        return kmp(root_str, subRoot_str)
```

Time Complexity: O(m + n), where m is the number of nodes in root and n is the number of nodes in subRoot.
Space Complexity: O(m + n) for the serialized strings.

Intuition and invariants:

- We convert the tree structure into a string representation (serialization).
- The KMP algorithm efficiently searches for the subRoot string within the root string.
- This approach leverages string matching algorithms to solve a tree problem.

## Recommendation

I recommend learning and implementing Solution 1 (Recursive DFS with Helper Function) for several reasons:

1. It's more intuitive and directly relates to the tree structure of the problem.
2. It's easier to understand and explain in an interview setting.
3. It doesn't require knowledge of advanced string matching algorithms like KMP.
4. It's a common pattern in tree-related problems, making it more broadly applicable.

While Solution 2 (Serialization and KMP) is more efficient in terms of time complexity, it's more complex and less intuitive. It's a clever approach that's worth knowing about, but it's less likely to be expected in an interview for this particular problem.

## Test cases

```python
def test_isSubtree():
    # Helper function to create trees from lists
    def create_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            node = queue.pop(0)
            if i < len(nodes) and nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root

    solution = Solution()

    # Test case 1: Example 1 from the problem statement
    root1 = create_tree([3,4,5,1,2])
    subRoot1 = create_tree([4,1,2])
    assert solution.isSubtree(root1, subRoot1) == True

    # Test case 2: Example 2 from the problem statement
    root2 = create_tree([3,4,5,1,2,None,None,None,None,0])
    subRoot2 = create_tree([4,1,2])
    assert solution.isSubtree(root2, subRoot2) == False

    # Test case 3: Empty subRoot
    root3 = create_tree([1,2,3])
    subRoot3 = None
    assert solution.isSubtree(root3, subRoot3) == True

    # Test case 4: Empty root
    root4 = None
    subRoot4 = create_tree([1,2,3])
    assert solution.isSubtree(root4, subRoot4) == False

    # Test case 5: Identical trees
    root5 = create_tree([1,2,3,4,5])
    subRoot5 = create_tree([1,2,3,4,5])
    assert solution.isSubtree(root5, subRoot5) == True

    # Test case 6: Subtree in left branch
    root6 = create_tree([1,2,3,4,5,6,7])
    subRoot6 = create_tree([2,4,5])
    assert solution.isSubtree(root6, subRoot6) == True

    # Test case 7: Subtree in right branch
    root7 = create_tree([1,2,3,4,5,6,7])
    subRoot7 = create_tree([3,6,7])
    assert solution.isSubtree(root7, subRoot7) == True

    print("All test cases passed!")

test_isSubtree()
```

## Overview of rejected approaches

1. Brute Force Comparison:

   - Approach: Compare every node in the root tree with the subRoot tree.
   - Why rejected: This would be extremely inefficient, with a time complexity of O(m^2 \* n), where m is the number of nodes in root and n is the number of nodes in subRoot.

2. Level Order Traversal:

   - Approach: Perform a level order traversal on both trees and compare the resulting arrays.
   - Why rejected: While this might work for some cases, it doesn't account for the structure of the tree. Two trees with the same level order traversal might have different structures.

3. Hash-based Approach:

   - Approach: Create a hash of the subRoot tree and compare it with hashes of subtrees in the root tree.
   - Why rejected: While this could be fast, it's complex to implement correctly and might have issues with hash collisions. It's also not as intuitive or commonly expected in interviews.

4. Iterative DFS with Stack:
   - Approach: Implement the same logic as the recursive solution but using an explicit stack.
   - Why not recommended: While this approach is correct and eliminates the risk of stack overflow for very deep trees, it's more complex to implement and understand compared to the recursive solution. For most practical cases, the recursive solution is sufficient and more elegant.

## Visualization(s)

To visualize the recursive DFS approach, we can use a simple diagram to show how the algorithm traverses the tree:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
  <g fill="none" stroke="black" stroke-width="2">
    <circle cx="200" cy="50" r="20"/>
    <circle cx="100" cy="100" r="20"/>
    <circle cx="300" cy="100" r="20"/>
    <circle cx="50" cy="150" r="20"/>
    <circle cx="150" cy="150" r="20"/>
    <circle cx="250" cy="150" r="20"/>
    <circle cx="350" cy="150" r="20"/>

    <line x1="200" y1="70" x2="100" y2="80"/>
    <line x1="200" y1="70" x2="300" y2="80"/>
    <line x1="100" y1="120" x2="50" y2="130"/>
    <line x1="100" y1="120" x2="150" y2="130"/>
    <line x1="300" y1="120" x2="250" y2="130"/>
    <line x1="300" y1="120" x2="350" y2="130"/>
  </g>

  <g font-family="Arial" font-size="16" text-anchor="middle">
    <text x="200" y="55" fill="black">1</text>
    <text x="100" y="105" fill="black">2</text>
    <text x="300" y="105" fill="black">3</text>
    <text x="50" y="155" fill="black">4</text>
    <text x="150" y="155" fill="black">5</text>
    <text x="250" y="155" fill="black">6</text>
    <text x="350" y="155" fill="black">7</text>
  </g>

  <g font-family="Arial" font-size="12" fill="red">
    <text x="220" y="40">Start here</text>
    <text x="120" y="90">Check subtree</text>
    <text x="320" y="90">If no match, check here</text>
    <text x="70" y="140">Continue checking</text>
    <text x="170" y="140">until all nodes</text>
    <text x="270" y="140">are explored or</text>
    <text x="370" y="140">a match is found</text>
  </g>
</svg>

```

This diagram illustrates how the recursive DFS approach starts at the root and systematically checks each node and its subtrees for a match with the subRoot tree. The red text indicates the order and logic of the traversal.
