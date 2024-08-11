# Explanation: Clone Graph

## Analysis of problem & input data

This problem involves creating a deep copy of a connected undirected graph. The key aspects to consider are:

1. Graph representation: The graph is represented using an adjacency list, where each node contains a value and a list of its neighbors.
2. Connectivity: The graph is connected, meaning all nodes can be reached from any starting node.
3. Uniqueness: Each node has a unique value between 1 and 100.
4. No self-loops or repeated edges: This simplifies the cloning process.
5. Deep copy requirement: We need to create new nodes and new connections, not just copy references.

The key principle that makes this question manageable is that we can use a mapping (e.g., a hash map) to keep track of which nodes we've already cloned. This allows us to handle cycles in the graph and avoid infinite recursion or duplication.

### Test cases

1. Standard case: A graph with multiple nodes and connections
2. Single node graph: A graph with only one node
3. Empty graph: An empty list representing no nodes
4. Fully connected graph: Every node is connected to every other node
5. Linear graph: Each node is connected only to the next node in sequence

Here's the executable Python code for these test cases:

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def create_graph(adj_list):
    if not adj_list:
        return None
    nodes = {i+1: Node(i+1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i+1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]

def graph_to_adj_list(node):
    if not node:
        return []
    visited = set()
    adj_list = []

    def dfs(node):
        if node.val in visited:
            return
        visited.add(node.val)
        adj_list.append([n.val for n in node.neighbors])
        for neighbor in node.neighbors:
            dfs(neighbor)

    dfs(node)
    return adj_list

# Test cases
test_cases = [
    [[2,4],[1,3],[2,4],[1,3]],  # Standard case
    [[]],  # Single node graph
    [],  # Empty graph
    [[2,3,4],[1,3,4],[1,2,4],[1,2,3]],  # Fully connected graph
    [[2],[3],[4],[]]  # Linear graph
]

for i, case in enumerate(test_cases):
    original = create_graph(case)
    print(f"Test case {i+1}:")
    print("Original:", graph_to_adj_list(original))
    # The cloneGraph function would be called here
    # cloned = cloneGraph(original)
    # print("Cloned:", graph_to_adj_list(cloned))
    print()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Depth-First Search (DFS) with recursion and hash map
2. Breadth-First Search (BFS) with queue and hash map
3. Iterative DFS with stack and hash map

Count: 3 solutions

#### Rejected solutions

1. Simple copying without handling cycles
2. Using deep copy libraries (e.g., copy.deepcopy in Python)
3. Serialization and deserialization of the graph

### Worthy Solutions

#### 1. Depth-First Search (DFS) with recursion and hash map

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Hash map to store the mapping of original nodes to cloned nodes
        cloned = {}

        def dfs(node):
            # If we've already cloned this node, return the cloned version
            if node in cloned:
                return cloned[node]

            # Create a new node with the same value
            copy = Node(node.val)
            # Add it to our hash map
            cloned[node] = copy

            # Recursively clone all neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
```

Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
Space Complexity: O(N) for the hash map and the recursion stack.

Intuitions and invariants:

- The hash map maintains a one-to-one mapping between original and cloned nodes.
- DFS ensures we explore all connected nodes.
- Recursive calls handle the graph's structure, including cycles.
- Each node is processed exactly once due to the hash map check.

#### 2. Breadth-First Search (BFS) with queue and hash map

```python
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Hash map to store the mapping of original nodes to cloned nodes
        cloned = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    # If we haven't seen this neighbor, clone it and add to queue
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add the cloned neighbor to the current cloned node's neighbors
                cloned[current].neighbors.append(cloned[neighbor])

        return cloned[node]
```

Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
Space Complexity: O(N) for the hash map and the queue.

Intuitions and invariants:

- BFS explores the graph level by level.
- The queue ensures we process all nodes in a breadth-first manner.
- The hash map prevents processing the same node multiple times and handles cycles.
- Each node is enqueued and processed exactly once.

#### 3. Iterative DFS with stack and hash map

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Hash map to store the mapping of original nodes to cloned nodes
        cloned = {node: Node(node.val)}
        stack = [node]

        while stack:
            current = stack.pop()

            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    # If we haven't seen this neighbor, clone it and add to stack
                    cloned[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                # Add the cloned neighbor to the current cloned node's neighbors
                cloned[current].neighbors.append(cloned[neighbor])

        return cloned[node]
```

Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
Space Complexity: O(N) for the hash map and the stack.

Intuitions and invariants:

- Iterative DFS explores the graph depth-first without recursion.
- The stack mimics the call stack of the recursive approach.
- The hash map serves the same purpose as in the other approaches.
- Each node is pushed to the stack and processed exactly once.

### Rejected Approaches

1. Simple copying without handling cycles:
   This approach would fail for graphs with cycles, leading to infinite recursion or loop.

2. Using deep copy libraries:
   While this would work, it doesn't demonstrate understanding of graph traversal algorithms and data structures, which is crucial in a coding interview setting.

3. Serialization and deserialization of the graph:
   This approach is unnecessarily complex for this problem and doesn't directly address the graph traversal aspect of the question.

### Final Recommendations

The DFS recursive approach (Solution 1) is recommended as the best solution to learn and present in an interview setting. It's concise, elegant, and clearly demonstrates understanding of graph traversal and the use of a hash map to handle cycles.

The BFS approach (Solution 2) is also worth knowing as it provides a different perspective on graph traversal and can be preferred in certain scenarios (e.g., when level-order processing is beneficial).

The iterative DFS (Solution 3) is less common but demonstrates the ability to convert recursive algorithms to iterative ones, which can be valuable in certain situations (e.g., to avoid stack overflow for very deep graphs).

All three approaches have the same time and space complexity, but the recursive DFS is often the most intuitive and easiest to implement correctly in an interview setting.

## Visualization(s)

Here's a simple visualization of how the DFS approach works on a small graph:

```tsx
import React, { useState } from "react";

const Node = ({ id, x, y, neighbors, isCloned }) => (
  <g>
    <circle
      cx={x}
      cy={y}
      r="20"
      fill={isCloned ? "lightgreen" : "lightblue"}
      stroke="black"
    />
    <text x={x} y={y} textAnchor="middle" dy=".3em">
      {id}
    </text>
    {neighbors.map((neighbor, index) => (
      <line
        key={index}
        x1={x}
        y1={y}
        x2={neighbor.x}
        y2={neighbor.y}
        stroke="black"
      />
    ))}
  </g>
);

const GraphCloneVisualization = () => {
  const [step, setStep] = useState(0);

  const originalGraph = [
    { id: 1, x: 100, y: 100, neighbors: [] },
    { id: 2, x: 200, y: 100, neighbors: [] },
    { id: 3, x: 150, y: 200, neighbors: [] },
  ];

  originalGraph[0].neighbors = [originalGraph[1], originalGraph[2]];
  originalGraph[1].neighbors = [originalGraph[0], originalGraph[2]];
  originalGraph[2].neighbors = [originalGraph[0], originalGraph[1]];

  const clonedGraph = JSON.parse(JSON.stringify(originalGraph));

  const steps = [
    "Initial graph",
    "Clone node 1",
    "Clone node 2",
    "Clone node 3",
    "Connect cloned nodes",
  ];

  return (
    <div>
      <svg width="500" height="300">
        <g transform="translate(0, 0)">
          {originalGraph.map((node, index) => (
            <Node key={index} {...node} isCloned={false} />
          ))}
        </g>
        <g transform="translate(250, 0)">
          {clonedGraph.map((node, index) => (
            <Node key={index} {...node} isCloned={step > index} />
          ))}
        </g>
      </svg>
      <div>
        <button onClick={() => setStep(Math.max(0, step - 1))}>Previous</button>
        <button onClick={() => setStep(Math.min(steps.length - 1, step + 1))}>
          Next
        </button>
      </div>
      <p>{steps[step]}</p>
    </div>
  );
};

export default GraphCloneVisualization;
```

This visualization shows the original graph on the left and the cloned graph on the right. As you step through the visualization, you can see how nodes are cloned one by one, and finally how the connections are established in the cloned graph.
