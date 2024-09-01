## Explanation: Swap Nodes in Pairs

### Analysis of problem & input data

This problem involves manipulating a linked list by swapping adjacent pairs of nodes. The key characteristics and constraints of the problem are:

1. We're working with a singly linked list.
2. We need to swap every two adjacent nodes.
3. We can't modify the values in the nodes; we must change the links between nodes.
4. The list length can be 0 to 100 nodes.
5. Node values are between 0 and 100, but this is irrelevant for the swapping operation.

The core principle that makes this question manageable is understanding how to rearrange pointers in a linked list. The challenge lies in keeping track of the correct nodes and updating their next pointers in the right order.

This problem falls into the category of linked list manipulation, which often involves careful pointer management and sometimes requires the use of dummy nodes or multiple pointers to keep track of different parts of the list.

### Test cases

Here are some relevant test cases to consider:

1. Empty list: `[]` → `[]`
2. Single node: `[1]` → `[1]`
3. Even number of nodes: `[1,2,3,4]` → `[2,1,4,3]`
4. Odd number of nodes: `[1,2,3,4,5]` → `[2,1,4,3,5]`
5. Large list (e.g., 100 nodes)

Here's the Python code to set up these test cases:

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
    while head:
        values.append(head.val)
        head = head.next
    return values

# Test cases
test_cases = [
    [],
    [1],
    [1,2,3,4],
    [1,2,3,4,5],
    list(range(1, 101))  # Large list with 100 nodes
]

for case in test_cases:
    head = create_linked_list(case)
    print(f"Input: {case}")
    # The actual swapping function would be called here
    # swapped_head = swapPairs(head)
    # print(f"Output: {linked_list_to_list(swapped_head)}")
    print()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Iterative approach with three pointers (Neetcode solution)
2. Recursive approach
3. Dummy node approach

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Swapping values instead of nodes (violates problem constraints)
2. Creating a new list (inefficient in terms of space complexity)

#### Worthy Solutions

##### Iterative approach with three pointers

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Edge case: if the list is empty or has only one node, no swapping needed
        if not head or not head.next:
            return head

        # Initialize dummy node to handle the case where the head changes
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # Nodes to be swapped
            first = head
            second = head.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

        return dummy.next
```

Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation of time and space complexity:

- We iterate through the list once, performing constant-time operations for each pair of nodes. This results in a linear time complexity of O(n).
- We use only a fixed number of pointers (dummy, prev, first, second) regardless of the input size, leading to constant space complexity O(1).

Intuitions and invariants:

- Using a dummy node simplifies handling the case where the head of the list changes.
- Three pointers (prev, first, second) are sufficient to perform the swap operation.
- The algorithm maintains the invariant that after each iteration, all pairs of nodes before the current position have been swapped.

##### Recursive approach

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one node, no swapping needed
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first = head
        second = head.next

        # Swapping
        first.next = self.swapPairs(second.next)  # Recursive call
        second.next = first

        # Return new head of the pair
        return second
```

Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(n/2) ≈ O(n) due to the recursion stack.

Explanation of time and space complexity:

- We make a recursive call for every pair of nodes, resulting in n/2 recursive calls. Each call performs constant-time operations, leading to O(n) time complexity.
- The recursion stack can go up to n/2 levels deep (one level for each pair of nodes), resulting in O(n) space complexity.

Intuitions and invariants:

- The recursive approach treats the problem as swapping the current pair and then recursively swapping the rest of the list.
- The base case handles lists with 0 or 1 nodes, which don't need swapping.
- Each recursive call returns the new head of its sublist, which becomes the next node for the previous pair.

##### Dummy node approach

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next

            # Swapping
            current.next = second
            first.next = second.next
            second.next = first

            # Move to the next pair
            current = first

        return dummy.next
```

Time Complexity: O(n), where n is the number of nodes in the linked list.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation of time and space complexity:

- We iterate through the list once, performing constant-time operations for each pair of nodes. This results in a linear time complexity of O(n).
- We use only a fixed number of pointers (dummy, current, first, second) regardless of the input size, leading to constant space complexity O(1).

Intuitions and invariants:

- The dummy node simplifies the swapping process by providing a consistent starting point.
- The algorithm maintains the invariant that 'current' always points to the node before the pair to be swapped.
- This approach avoids the need for special handling of the head node.

#### Rejected Approaches

1. Swapping values instead of nodes:
   This approach might seem simpler at first, but it violates the problem constraint that we must not modify the values in the list's nodes. It's important to pay attention to all constraints in the problem statement.

2. Creating a new list:
   While this could work, it would be inefficient in terms of space complexity (O(n) instead of O(1)). In linked list problems, we usually aim to manipulate the existing structure rather than create a new one, unless specifically required.

#### Final Recommendations

The iterative approach with three pointers (Neetcode solution) is recommended as the best solution to learn. Here's why:

1. It has optimal time complexity (O(n)) and space complexity (O(1)).
2. It's iterative, which is generally easier to understand and implement than recursive solutions.
3. It doesn't require creating new nodes, making it memory-efficient.
4. The use of a dummy node elegantly handles the case where the head of the list changes.

The recursive approach is also worth understanding as it demonstrates a different way of thinking about the problem. However, it's less optimal in terms of space complexity due to the recursion stack.

The dummy node approach is very similar to the three-pointer approach and is also a good solution. The main difference is in how it iterates through the list.

### Visualization(s)

To visualize the swapping process, let's consider a simple linked list with four nodes: [1, 2, 3, 4]

Initial state:

```
dummy -> 1 -> 2 -> 3 -> 4 -> None
 prev   head
```

After first swap:

```
dummy -> 2 -> 1 -> 3 -> 4 -> None
         |    |
         |    head
        prev
```

After second swap:

```
dummy -> 2 -> 1 -> 4 -> 3 -> None
              |    |    |
              |    |   head
             prev
```

Final state:

```
dummy -> 2 -> 1 -> 4 -> 3 -> None
```

This visualization helps to understand how the pointers move and how the list is restructured during the swapping process.
