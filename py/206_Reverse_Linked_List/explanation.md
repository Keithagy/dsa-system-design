## Explanation: Reverse Linked List

### Analysis of problem & input data

This problem is a classic example of linked list manipulation. The key characteristics to note are:

1. We're dealing with a singly linked list, meaning each node only has a reference to the next node, not the previous one.
2. We need to reverse the entire list, changing the direction of all pointers.
3. The problem asks for both iterative and recursive solutions, which is common for linked list problems.

The key principle that makes this question simple is the idea of pointer manipulation. By carefully managing three pointers (previous, current, and next), we can reverse the links one by one.

Pattern-matching wise, this problem falls into the category of "in-place reversal of a linked list". Recognizing this pattern is crucial for solving similar problems like reversing a linked list in groups, or reversing only a part of a linked list.

### Test cases

1. Normal case: A list with multiple elements (e.g., [1,2,3,4,5])
2. Edge case: Empty list ([])
3. Edge case: List with only one element ([1])
4. Edge case: List with two elements ([1,2])

Here's the executable Python code for these test cases:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Test cases
test_cases = [
    [1,2,3,4,5],  # Normal case
    [],           # Empty list
    [1],          # Single element
    [1,2]         # Two elements
]

for case in test_cases:
    head = create_linked_list(case)
    print(f"Input: {case}")
    # The actual reverse_list function will be implemented in the solutions
    # reversed_head = reverse_list(head)
    # print(f"Output: {linked_list_to_list(reversed_head)}")
    print()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Iterative approach with three pointers
2. Recursive approach
3. Stack-based approach

Count: 3 solutions

##### Rejected solutions

1. Creating a new linked list (not in-place)
2. Using additional data structures like arrays or queues (inefficient space complexity)

#### Worthy Solutions

##### Iterative approach with three pointers

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while current:
        # Store the next node before we change current.next
        next_node = current.next

        # Reverse the link
        current.next = prev

        # Move prev and current one step forward
        prev = current
        current = next_node

    # prev is now the new head of the reversed list
    return prev
```

Runtime complexity: O(n), where n is the number of nodes in the list
Space complexity: O(1), as we only use a constant amount of extra space

Intuitions and invariants:

- We maintain three pointers: prev, current, and next_node
- At each step, we reverse the link between prev and current
- The loop invariant is that at the start of each iteration, we have reversed the portion of the list before 'current'
- When the loop ends, 'prev' becomes the new head of the reversed list

##### Recursive approach

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # Base case: empty list or list with only one node
    if not head or not head.next:
        return head

    # Recursive case
    # Reverse the rest of the list
    new_head = reverse_list(head.next)

    # Reverse the link between current node and next node
    head.next.next = head
    head.next = None

    return new_head
```

Runtime complexity: O(n), where n is the number of nodes in the list
Space complexity: O(n) due to the recursion stack

Intuitions and invariants:

- The recursion reaches the last node, which becomes the new head
- As the recursion unwinds, each node reverses its link to the previous node
- The invariant is that at each recursive call, we've reversed the sublist starting from the next node
- The base case handles empty lists and lists with a single node

##### Stack-based approach

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    stack = []
    current = head

    # Push all nodes onto the stack
    while current:
        stack.append(current)
        current = current.next

    # Pop nodes from stack to reverse the list
    new_head = stack.pop()
    current = new_head

    while stack:
        current.next = stack.pop()
        current = current.next

    # Set the last node's next to None
    current.next = None

    return new_head
```

Runtime complexity: O(n), where n is the number of nodes in the list
Space complexity: O(n) due to the stack

Intuitions and invariants:

- We use a stack to reverse the order of nodes
- The invariant is that the stack always contains the remaining nodes to be reversed
- After popping all nodes, the list is naturally in reverse order

#### Rejected Approaches

1. Creating a new linked list:
   This approach involves creating a new list by traversing the original list and inserting each node at the beginning of the new list. While correct, it's not in-place and uses O(n) extra space, which is less efficient than the in-place reversal.

2. Using arrays or queues:
   Converting the linked list to an array, reversing the array, and then creating a new linked list would work but is inefficient in both time and space (O(n) extra space).

#### Final Recommendations

The iterative approach with three pointers is the best solution to learn and use in an interview setting. It's in-place, has O(1) space complexity, and is generally easier to explain and implement without errors compared to the recursive approach. The recursive approach, while elegant, has the drawback of O(n) space complexity due to the call stack, which could be problematic for very long lists. The stack-based approach, while intuitive, is less efficient in terms of space complexity and is not as commonly expected in interviews.

### Visualization(s)

To visualize the iterative three-pointer approach, we can use a simple ASCII representation:

```
Initial state:
NULL <- 1 -> 2 -> 3 -> 4 -> 5 -> NULL
 ^     ^    ^
prev  curr next

Step 1:
NULL <- 1 <- 2    3 -> 4 -> 5 -> NULL
       ^    ^     ^
      prev curr  next

Step 2:
NULL <- 1 <- 2 <- 3    4 -> 5 -> NULL
            ^    ^     ^
           prev curr  next

...

Final state:
NULL <- 1 <- 2 <- 3 <- 4 <- 5    NULL
                           ^     ^
                          prev  curr
```

This visualization shows how the pointers move and how the links are reversed at each step of the algorithm.

```tsx
import React, { useState } from "react";
import { ChevronRight, ChevronLeft } from "lucide-react";

const Node = ({ value, reversed }) => (
  <div className="flex items-center">
    <div className="w-10 h-10 rounded-full bg-blue-500 flex items-center justify-center text-white font-bold">
      {value}
    </div>
    {reversed ? (
      <ChevronLeft className="text-red-500" />
    ) : (
      <ChevronRight className="text-green-500" />
    )}
  </div>
);

const ReverseLinkedListVisualization = () => {
  const [step, setStep] = useState(0);
  const totalSteps = 5;

  const getReversedCount = (currentStep) => {
    return Math.min(currentStep, 5);
  };

  return (
    <div className="p-4 bg-gray-100 rounded-lg">
      <div className="flex justify-center mb-4">
        {[1, 2, 3, 4, 5].map((value, index) => (
          <Node
            key={value}
            value={value}
            reversed={index < getReversedCount(step)}
          />
        ))}
      </div>
      <div className="flex justify-between mt-4">
        <button
          className="px-4 py-2 bg-blue-500 text-white rounded disabled:opacity-50"
          onClick={() => setStep(Math.max(0, step - 1))}
          disabled={step === 0}
        >
          Previous
        </button>
        <span>
          Step {step} of {totalSteps}
        </span>
        <button
          className="px-4 py-2 bg-blue-500 text-white rounded disabled:opacity-50"
          onClick={() => setStep(Math.min(totalSteps, step + 1))}
          disabled={step === totalSteps}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default ReverseLinkedListVisualization;
```

This React component provides an interactive visualization of the reverse linked list process. Users can step through the reversal process, seeing how the direction of the arrows changes as the list is reversed.
