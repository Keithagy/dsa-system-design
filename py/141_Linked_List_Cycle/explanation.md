## Explanation: Linked List Cycle

### Analysis of problem & input data

This problem is about detecting a cycle in a linked list. The key characteristics of the problem are:

1. We're given the head of a linked list.
2. We need to determine if there's a cycle in the list.
3. A cycle exists if we can reach a node again by following the `next` pointers.
4. The `pos` parameter is not directly given to us; it's used internally to create the cycle.
5. We need to return a boolean value: `True` if there's a cycle, `False` otherwise.

The crucial insight for this problem is that if there's a cycle, we can detect it by using two pointers moving at different speeds. This is known as the "Floyd's Cycle-Finding Algorithm" or the "Tortoise and Hare Algorithm". The key principle that makes this question simple is: in a cyclic list, a fast pointer will eventually catch up to a slow pointer.

This problem falls into the category of "Two Pointer" problems, specifically the "Fast and Slow Pointer" pattern. It's a classic example of how two pointers moving at different speeds can be used to detect a cycle in a linear data structure.

### Test cases

Here are some important test cases to consider:

1. Empty list: `head = None`
2. Single node without cycle: `head = [1]`
3. Two nodes with cycle: `head = [1,2]`, `pos = 0`
4. Multiple nodes with cycle: `head = [3,2,0,-4]`, `pos = 1`
5. Multiple nodes without cycle: `head = [1,2,3,4,5]`
6. Single node with self-cycle: `head = [1]`, `pos = 0`

Here's the Python code to set up these test cases:

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(values, pos):
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]

# Test cases
test_cases = [
    ([], -1),
    ([1], -1),
    ([1,2], 0),
    ([3,2,0,-4], 1),
    ([1,2,3,4,5], -1),
    ([1], 0)
]

test_heads = [create_linked_list(values, pos) for values, pos in test_cases]
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Floyd's Cycle-Finding Algorithm (Two Pointers: Fast and Slow)
2. Hash Set Approach
3. Marking Nodes Approach (modifying the original list)

Count: 3 solutions

##### Rejected solutions

1. Naive approach: Keeping track of all visited nodes in a list
2. Using a counter and arbitrary large number of steps

#### Worthy Solutions

##### Floyd's Cycle-Finding Algorithm (Two Pointers: Fast and Slow)

```python
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        # Initialize two pointers
        slow = head  # moves one step at a time
        fast = head.next  # moves two steps at a time

        # Loop until fast reaches the end or slow meets fast
        while fast and fast.next:
            if slow == fast:
                return True  # Cycle detected
            slow = slow.next  # Move slow one step
            fast = fast.next.next  # Move fast two steps

        return False  # No cycle detected
```

Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as we only use two pointers regardless of the list size.

Key intuitions and invariants:

- If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
- The fast pointer moves twice as fast as the slow pointer.
- If there's no cycle, the fast pointer will reach the end of the list.
- This algorithm works because in a cyclic list, the distance between the two pointers decreases by 1 in each iteration.

##### Hash Set Approach

```python
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()  # Set to store visited nodes

        current = head
        while current:
            if current in seen:
                return True  # Cycle detected
            seen.add(current)  # Mark current node as visited
            current = current.next

        return False  # No cycle detected
```

Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(n), as in the worst case, we might need to store all nodes in the set.

Key intuitions and invariants:

- Each node is unique, even if values are repeated.
- If we encounter a node we've seen before, there must be a cycle.
- The set allows for O(1) lookup time to check if a node has been visited.

##### Marking Nodes Approach

```python
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == float('inf'):
                return True  # Cycle detected
            head.val = float('inf')  # Mark node as visited
            head = head.next
        return False  # No cycle detected
```

Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as we modify the existing nodes without using extra space.

Key intuitions and invariants:

- We use a special value (infinity) to mark visited nodes.
- If we encounter a marked node, there must be a cycle.
- This approach modifies the original list, which might not be allowed in all scenarios.

#### Rejected Approaches

1. Naive approach (keeping track of all visited nodes in a list):

   - This would work but is less efficient in terms of space complexity (O(n)) and time complexity for lookups (O(n) per lookup).

2. Using a counter and arbitrary large number of steps:
   - This approach might fail for very large lists and doesn't guarantee correctness.

#### Final Recommendations

The Floyd's Cycle-Finding Algorithm (Two Pointers: Fast and Slow) is the best solution to learn for this problem. It has optimal space complexity O(1) and time complexity O(n), and it doesn't modify the original list. This algorithm is also widely applicable to other problems involving cycles or finding middle elements in linked lists.

### Visualization(s)

To visualize the Floyd's Cycle-Finding Algorithm, let's create a simple React component that demonstrates how the slow and fast pointers move through a linked list.

```tsx
import React, { useState, useEffect } from "react";

const LinkedListNode = ({ value, isSlow, isFast }) => (
  <div
    className={`inline-flex items-center justify-center w-12 h-12 rounded-full border-2 border-gray-300 ${isSlow ? "bg-blue-200" : ""} ${isFast ? "bg-red-200" : ""} ${isSlow && isFast ? "bg-purple-200" : ""}`}
  >
    {value}
  </div>
);

const Arrow = () => <div className="inline-block mx-2">→</div>;

const FloydCycleFinding = () => {
  const [nodes, setNodes] = useState([3, 2, 0, -4, 2, 0]);
  const [slow, setSlow] = useState(0);
  const [fast, setFast] = useState(0);
  const [cycleDetected, setCycleDetected] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      if (cycleDetected) return;

      setSlow((prev) => (prev + 1) % nodes.length);
      setFast((prev) => (prev + 2) % nodes.length);

      if (slow === fast) {
        setCycleDetected(true);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [slow, fast, nodes.length, cycleDetected]);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">
        Floyd's Cycle-Finding Algorithm Visualization
      </h2>
      <div className="flex flex-wrap items-center mb-4">
        {nodes.map((node, index) => (
          <React.Fragment key={index}>
            <LinkedListNode
              value={node}
              isSlow={index === slow}
              isFast={index === fast}
            />
            {index < nodes.length - 1 && <Arrow />}
          </React.Fragment>
        ))}
      </div>
      <div className="mt-4">
        <p className="text-lg">
          {cycleDetected ? "Cycle detected!" : "Searching for cycle..."}
        </p>
        <p>Slow pointer position: {slow}</p>
        <p>Fast pointer position: {fast}</p>
      </div>
    </div>
  );
};

export default FloydCycleFinding;
```

This visualization demonstrates how the slow and fast pointers move through the linked list. The slow pointer (blue) moves one step at a time, while the fast pointer (red) moves two steps. When they meet (purple), a cycle is detected.

## Implementation Details

The provided implementations follow the guidelines:

- They use Python with type hints.
- Memoization (in the Hash Set approach) uses a direct hash map (set).
- Comments explain the intuition and key characteristics of each algorithm.
- Variable naming is contextually helpful (e.g., `slow`, `fast`, `seen`).
- The solutions demonstrate understanding of data structures and algorithms without relying on excessive built-in functions.

These implementations strike a balance between clarity and efficiency, making them excellent examples for Leetcode interview preparation.
