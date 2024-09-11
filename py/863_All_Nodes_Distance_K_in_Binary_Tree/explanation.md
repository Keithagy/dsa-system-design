## Explanation: All Nodes Distance K in Binary Tree

### Analysis of problem & input data

This problem is a classic example of tree traversal with a twist. The key aspects to consider are:

1. **Binary Tree Structure**: We're dealing with a binary tree, which means each node has at most two children.

2. **Bidirectional Traversal**: Unlike typical tree problems where we only need to traverse downwards, this problem requires us to move both up and down the tree. This is because nodes at distance K can be:
   a) Below the target node
   b) Above the target node
   c) In a different subtree altogether

3. **Distance Calculation**: We need to keep track of the distance from the target node as we traverse.

4. **Target Node**: The target node is given by value, not by reference. This means we first need to locate the target node in the tree.

5. **Result Collection**: We need to collect all nodes exactly K distance away from the target, not those closer or further.

The key principle that makes this question manageable is treating the tree as an undirected graph. By doing so, we can use graph traversal techniques (like BFS or DFS) to find all nodes at a specific distance, regardless of their position relative to the target node in the original tree structure.

### Test cases

1. **Standard Case**: As given in Example 1

   - Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
   - Output: [7,4,1]

2. **Single Node Tree**: As given in Example 2

   - Input: root = [1], target = 1, k = 3
   - Output: []

3. **Target is Root**:

   - Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 3, k = 3
   - Output: [6,7,0,8]

4. **K is 0**:

   - Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 0
   - Output: [5]

5. **K is Larger than Tree Height**:
   - Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 3, k = 5
   - Output: []

Here's the Python code for these test cases:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

def test_distance_k(solution_func):
    # Test case 1
    root1 = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    assert sorted(solution_func(root1, 5, 2)) == [1,4,7], "Test case 1 failed"

    # Test case 2
    root2 = build_tree([1])
    assert solution_func(root2, 1, 3) == [], "Test case 2 failed"

    # Test case 3
    root3 = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    assert sorted(solution_func(root3, 3, 3)) == [0,6,7,8], "Test case 3 failed"

    # Test case 4
    root4 = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    assert solution_func(root4, 5, 0) == [5], "Test case 4 failed"

    # Test case 5
    root5 = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    assert solution_func(root5, 3, 5) == [], "Test case 5 failed"

    print("All test cases passed!")

# Usage:
# test_distance_k(your_solution_function)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. DFS with Parent Pointers (Neetcode solution)
2. BFS with Parent Pointers
3. Two-way BFS
4. Graph Conversion and BFS

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Naive DFS/BFS: Traverse the entire tree for each level of K, which is inefficient.
2. Pure Recursive Approach: While possible, it's more complex and less intuitive than the iterative solutions.

#### Worthy Solutions

##### DFS with Parent Pointers (Neetcode solution)

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return

            # Store the parent for each node
            node.parent = parent

            # Recursively process left and right children
            dfs(node.left, node)
            dfs(node.right, node)

        # Step 1: Add parent pointers to each node
        dfs(root, None)

        # Step 2: BFS from target node
        queue = [(target, 0)]
        visited = set([target])
        result = []

        while queue:
            node, distance = queue.pop(0)

            # If we've reached distance k, add node value to result
            if distance == k:
                result.append(node.val)

            # Explore neighbors (left, right, and parent) if distance < k
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor and neighbor not in visited and distance < k:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return result
```

Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N) in the worst case, for both the parent pointers and the queue/visited set in BFS.

Explanation:

- We perform two passes over the tree:
  1. DFS to add parent pointers: This takes O(N) time and O(N) space for the additional parent pointers.
  2. BFS from the target node: This also takes O(N) time in the worst case, and O(N) space for the queue and visited set.
- Each node is visited at most once in each pass, hence the linear time complexity.
- The space complexity is dominated by the parent pointers and BFS data structures, both of which can be up to O(N) in size.

Intuitions and invariants:

- Adding parent pointers transforms the tree into an undirected graph, allowing bidirectional traversal.
- BFS ensures we visit nodes in order of increasing distance from the target.
- The visited set prevents revisiting nodes, avoiding infinite loops in the now-cyclic structure.
- By stopping the BFS when we reach distance k, we ensure we only collect nodes exactly k distance away.

##### BFS with Parent Pointers

```python
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(node, parent):
            if not node:
                return
            node.parent = parent
            add_parent(node.left, node)
            add_parent(node.right, node)

        # Step 1: Add parent pointers
        add_parent(root, None)

        # Step 2: Find the target node
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == target.val:
                target_node = node
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Step 3: BFS from target node
        queue = deque([(target_node, 0)])
        visited = set([target_node])
        result = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor and neighbor not in visited and dist < k:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return result
```

Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N) for the parent pointers, queue, and visited set.

Explanation:

- We perform three passes over the tree:
  1. BFS to add parent pointers: O(N) time and O(N) space for the additional parent pointers.
  2. BFS to find the target node: O(N) time in the worst case, O(W) space where W is the maximum width of the tree.
  3. BFS from the target node: O(N) time and O(N) space for the queue and visited set.
- Each node is visited at most once in each pass, maintaining the linear time complexity.
- The space complexity is dominated by the parent pointers and BFS data structures, both O(N) in the worst case.

Intuitions and invariants:

- Adding parent pointers allows us to treat the tree as an undirected graph.
- The first BFS ensures we find the target node efficiently.
- The second BFS from the target node guarantees we find all nodes at exactly distance k.
- The visited set prevents cycles and ensures each node is processed only once.

##### Two-way BFS

```python
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def find_path(node, target, path):
            if not node:
                return None
            if node.val == target.val:
                return path + [node]
            left_path = find_path(node.left, target, path + [node])
            if left_path:
                return left_path
            right_path = find_path(node.right, target, path + [node])
            if right_path:
                return right_path
            return None

        def bfs(node, blocked, distance):
            queue = deque([(node, 0)])
            result = []
            while queue:
                curr, dist = queue.popleft()
                if dist == distance:
                    result.append(curr.val)
                if dist > distance:
                    break
                if curr.left and curr.left != blocked:
                    queue.append((curr.left, dist + 1))
                if curr.right and curr.right != blocked:
                    queue.append((curr.right, dist + 1))
            return result

        # Find path from root to target
        path = find_path(root, target, [])

        result = []
        for i, node in enumerate(path):
            remaining_distance = k - (len(path) - 1 - i)
            if remaining_distance == 0:
                result.append(node.val)
            elif remaining_distance > 0:
                blocked = path[i+1] if i+1 < len(path) else None
                result.extend(bfs(node, blocked, remaining_distance))

        return result
```

Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(H + K), where H is the height of the tree and K is the given distance.

Explanation:

- We perform two main operations:
  1. Finding the path from root to target: O(N) time in the worst case, O(H) space for the recursion stack.
  2. BFS from each node in the path: O(N) time total (as each node is visited at most once), O(K) space for the queue.
- The find_path function may visit each node once in the worst case, giving O(N) time.
- The BFS from each node in the path collectively visits each node at most once, maintaining O(N) time overall.
- The space complexity is dominated by the recursion stack in find_path (O(H)) and the BFS queue (O(K)).

Intuitions and invariants:

- By finding the path from root to target, we can calculate the distance of each node in this path to the target.
- For each node in the path, we perform a BFS to find nodes at the remaining distance.
- The 'blocked' parameter in BFS prevents us from going back up the tree, avoiding duplicate results.
- This approach efficiently handles both upward and downward traversals without need for parent pointers.

##### Graph Conversion and BFS

```python
from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Convert tree to graph
        graph = defaultdict(list)

        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # BFS from target
        queue = deque([(target.val, 0)])
        visited = set([target.val])
        result = []

        while queue:
            node_val, distance = queue.popleft()

            if distance == k:
                result.append(node_val)

            for neighbor in graph[node_val]:
                if neighbor not in visited and distance < k:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return result
```

Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N) for the graph representation and BFS queue/visited set.

Explanation:

- We perform two main operations:
  1. Converting the tree to a graph: O(N) time to visit each node once, O(N) space for the graph representation.
  2. BFS from the target node: O(N) time to visit each node once, O(N) space for the queue and visited set.
- The build_graph function visits each node once, creating bidirectional edges, taking O(N) time.
- The BFS visits each node at most once, maintaining O(N) time complexity.
- The space complexity is dominated by the graph representation, which stores all edges (O(N) in a tree).

Intuitions and invariants:

- Converting the tree to a graph allows us to treat it as an undirected graph, simplifying the traversal.
- The graph representation naturally handles both upward and downward movements without need for parent pointers.
- BFS ensures we visit nodes in order of increasing distance from the target.
- The visited set prevents revisiting nodes, crucial in the now-cyclic graph structure.

#### Rejected Approaches

1. **Naive DFS/BFS**: A straightforward approach might be to perform a DFS or BFS for each level of K, starting from the target node. This would work, but it's highly inefficient with a time complexity of O(N \* K), where N is the number of nodes. It's rejected because it unnecessarily revisits nodes multiple times. For large values of K, this approach could become prohibitively slow.

2. **Pure Recursive Approach**: While it's possible to solve this problem using a purely recursive approach without any additional data structures, it tends to be more complex and less intuitive. Here's why it's rejected:

   - It requires maintaining state across multiple recursive calls, making the code harder to understand and maintain.
   - It often leads to redundant computations, as the same paths might be explored multiple times.
   - The time complexity can be worse than the iterative approaches, potentially O(N^2) in the worst case.
   - It's more prone to stack overflow errors for very deep trees, especially when K is large.

3. **Dijkstra's Algorithm**: While Dijkstra's algorithm can find the shortest path in a graph, it's overkill for this problem. The binary tree structure guarantees that there's only one path between any two nodes, making Dijkstra's unnecessary complexity. It's rejected because:

   - It has a higher time complexity (O(N log N) with a priority queue) than necessary for this problem.
   - It requires converting the tree to a graph first, adding unnecessary steps.
   - The additional complexity doesn't provide any benefits for this specific problem.

4. **Floyd-Warshall Algorithm**: This algorithm finds the shortest paths between all pairs of nodes in a graph. It's massively overkill for this problem and is rejected because:
   - It has a time complexity of O(N^3), which is far worse than the O(N) solutions we have.
   - It solves a much more general problem than what we need, wasting computational resources.
   - It requires converting the tree to a graph and then to an adjacency matrix, adding unnecessary steps and memory usage.

#### Final Recommendations

After analyzing all the approaches, I recommend learning and using the **DFS with Parent Pointers** solution (the Neetcode solution) for the following reasons:

1. **Efficiency**: It solves the problem in O(N) time and space, which is optimal for this problem.
2. **Intuitive**: The two-step process (adding parent pointers, then BFS) is easy to understand and explain.
3. **Versatility**: The technique of adding parent pointers to a tree is useful in many tree-related problems, making this solution a good learning opportunity.
4. **Implementation**: It's relatively straightforward to implement and doesn't require complex data structures.
5. **Interview Performance**: In an interview setting, this solution demonstrates a good understanding of tree structures and graph traversal algorithms.

For those looking to expand their knowledge, the **Two-way BFS** approach is also worth studying. While slightly more complex, it showcases a clever way to handle the problem without modifying the tree structure, which could be beneficial in certain scenarios where modifying the input is not allowed.

### Visualization(s)

To help visualize the DFS with Parent Pointers approach, let's create a simple diagram using ASCII art:

```
Step 1: Add Parent Pointers

       3
     /   \
    5     1
   / \   / \
  6   2 0   8
     / \
    7   4

Becomes:

       3 (parent: None)
     /   \
    5     1 (parent: 3)
   / \   / \
  6   2 0   8 (parent: 1)
     / \
    7   4 (parent: 2)

Step 2: BFS from target (5)

Level 0:   [5]
Level 1:   [6, 2, 3]
Level 2:   [7, 4, 1]

Result for k=2: [7, 4, 1]
```

For a more interactive visualization, we can use a simple React component to demonstrate the BFS process:

```tsx
import React, { useState, useEffect } from "react";

const TreeNode = ({ value, x, y, visited }) => (
  <g transform={`translate(${x},${y})`}>
    <circle r="20" fill={visited ? "lightgreen" : "white"} stroke="black" />
    <text textAnchor="middle" dy=".3em">
      {value}
    </text>
  </g>
);

const BFSVisualization = () => {
  const [step, setStep] = useState(0);
  const [visited, setVisited] = useState(new Set());

  const treeData = [
    { id: 3, x: 200, y: 50 },
    { id: 5, x: 100, y: 100 },
    { id: 1, x: 300, y: 100 },
    { id: 6, x: 50, y: 150 },
    { id: 2, x: 150, y: 150 },
    { id: 0, x: 250, y: 150 },
    { id: 8, x: 350, y: 150 },
    { id: 7, x: 125, y: 200 },
    { id: 4, x: 175, y: 200 },
  ];

  const bfsOrder = [[5], [6, 2, 3], [7, 4, 1], [0, 8]];

  useEffect(() => {
    if (step < bfsOrder.length) {
      setVisited((prev) => new Set([...prev, ...bfsOrder[step]]));
    }
  }, [step]);

  return (
    <div>
      <svg width="400" height="250">
        {treeData.map((node) => (
          <TreeNode
            key={node.id}
            value={node.id}
            x={node.x}
            y={node.y}
            visited={visited.has(node.id)}
          />
        ))}
      </svg>
      <div>
        <button onClick={() => setStep((prev) => Math.max(0, prev - 1))}>
          Previous
        </button>
        <button
          onClick={() => setStep((prev) => Math.min(bfsOrder.length, prev + 1))}
        >
          Next
        </button>
        <p>Step: {step}</p>
        <p>
          Nodes at distance {step}: {bfsOrder[step]?.join(", ") || "None"}
        </p>
      </div>
    </div>
  );
};

export default BFSVisualization;
```

This visualization allows you to step through the BFS process, showing which nodes are visited at each level of the traversal. The nodes turn green as they are visited, helping to illustrate how the algorithm explores the tree level by level from the target node.
