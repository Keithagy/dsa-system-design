## Explanation: Remove Nth Node From End of List

### Analysis of problem & input data

This problem involves manipulating a singly linked list, which is a fundamental data structure in computer science. The key aspects of this problem are:

1. We need to remove a node from the list based on its position from the end, not the beginning.
2. We're given the head of the list and don't know its length upfront.
3. The problem asks if we can do this in one pass, which is a hint towards an optimal solution.

The main challenge here is that in a singly linked list, we can only traverse forward. However, we need to find a node based on its position from the end. This creates a disconnect between the information we have (forward traversal) and the information we need (backward position).

The key principle that makes this question simple is the "two-pointer" technique. By maintaining two pointers with a specific gap between them, we can simulate the process of knowing the nth node from the end without actually traversing the list twice.

### Test cases

1. Normal case: `head = [1,2,3,4,5], n = 2` -> `[1,2,3,5]`
2. Remove head: `head = [1,2,3,4,5], n = 5` -> `[2,3,4,5]`
3. Remove tail: `head = [1,2,3,4,5], n = 1` -> `[1,2,3,4]`
4. Single node: `head = [1], n = 1` -> `[]`
5. Two nodes, remove head: `head = [1,2], n = 2` -> `[2]`
6. Two nodes, remove tail: `head = [1,2], n = 1` -> `[1]`

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
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
test_cases = [
    (create_linked_list([1,2,3,4,5]), 2),
    (create_linked_list([1,2,3,4,5]), 5),
    (create_linked_list([1,2,3,4,5]), 1),
    (create_linked_list([1]), 1),
    (create_linked_list([1,2]), 2),
    (create_linked_list([1,2]), 1)
]

def test_remove_nth_from_end(func):
    for i, (head, n) in enumerate(test_cases):
        result = func(head, n)
        print(f"Test case {i+1}: {linked_list_to_list(result)}")

# Usage: test_remove_nth_from_end(your_function_here)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Two-pointer technique (one-pass solution) [Neetcode solution]
2. Two-pass solution with length calculation
3. Recursive solution

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute force approach with multiple passes
2. Converting to array, modifying, and converting back to linked list

#### Worthy Solutions

##### Two-pointer technique (one-pass solution)

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node to handle edge cases (e.g., removing the head)
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers
        first = dummy
        second = dummy

        # Advance first pointer by n+1 steps
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next
```

Time Complexity: O(L), where L is the length of the linked list

- We traverse the list once with the first pointer (n+1 steps)
- Then we move both pointers until we reach the end (L-n steps)
- Total steps: (n+1) + (L-n) = L+1, which is O(L)

Space Complexity: O(1)

- We only use a constant amount of extra space (two pointers)

Intuition and invariants:

- The key idea is to maintain a gap of n nodes between two pointers
- When the first pointer reaches the end, the second pointer will be at the (n+1)th node from the end
- This allows us to easily remove the nth node by modifying the next pointer of the (n+1)th node
- The dummy node simplifies edge cases, especially when removing the head of the list

##### Two-pass solution with length calculation

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # First pass: Calculate the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Edge case: If n == length, we're removing the head
        if n == length:
            return head.next

        # Second pass: Remove the (length - n)th node
        current = head
        for _ in range(length - n - 1):  # Stop at the node before the one to be removed
            current = current.next

        # Remove the nth node from the end
        current.next = current.next.next

        return head
```

Time Complexity: O(L), where L is the length of the linked list

- We traverse the list twice:
  1. Once to calculate the length (L steps)
  2. Once to reach the node before the one to be removed (at most L-1 steps)
- Total steps: L + (L-1) = 2L-1, which is O(L)

Space Complexity: O(1)

- We only use a constant amount of extra space (length variable and current pointer)

Intuition and invariants:

- By calculating the length first, we can convert the "nth from the end" problem into a "kth from the beginning" problem
- The node to be removed is at position (length - n + 1) from the start
- We stop one node before this to be able to modify the next pointer
- This approach is more straightforward but requires two passes through the list

##### Recursive solution

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def remove_nth(node: ListNode, n: int) -> tuple[ListNode, int]:
            # Base case: end of the list
            if not node:
                return None, 0

            # Recursive call
            next_node, position = remove_nth(node.next, n)

            # Update position (counting from the end)
            position += 1

            if position == n:
                # This is the node to be removed
                return next_node, position
            else:
                # Update the next pointer and return
                node.next = next_node
                return node, position

        # Handle edge case: removing the head
        dummy = ListNode(0)
        dummy.next = head
        dummy.next, _ = remove_nth(dummy.next, n)
        return dummy.next
```

Time Complexity: O(L), where L is the length of the linked list

- We traverse the list once recursively, visiting each node exactly once

Space Complexity: O(L)

- The recursion stack will have L frames in the worst case (when removing the last node)

Intuition and invariants:

- We use recursion to implicitly traverse the list backwards
- As we unwind the recursion, we count the position from the end
- When we reach the nth position, we "remove" the node by returning its next node
- The dummy node helps handle the edge case of removing the head

#### Rejected Approaches

1. Brute force approach with multiple passes:

   - Traverse the list to find its length
   - Traverse again to the (length - n)th node
   - Remove the next node
     This approach is correct but inefficient, requiring multiple passes through the list.

2. Converting to array, modifying, and converting back to linked list:
   - Convert the linked list to an array
   - Remove the nth element from the end
   - Convert the array back to a linked list
     This approach works but defeats the purpose of using a linked list and uses O(L) extra space.

#### Final Recommendations

The two-pointer technique (one-pass solution) is the best to learn for this problem. It's efficient (O(L) time, O(1) space) and demonstrates a clever use of pointers to solve the problem in a single pass. This technique is also applicable to many other linked list problems, making it a valuable addition to your problem-solving toolkit.

The two-pass solution is a good fallback if you can't recall or implement the two-pointer technique under pressure. It's straightforward and still efficient in terms of time complexity.

The recursive solution, while interesting, is generally not recommended for interviews due to its space complexity and potential for stack overflow with very long lists. However, understanding it can deepen your grasp of recursion and linked list operations.

### Visualization(s)

For the two-pointer technique, we can visualize it as follows:

```
Initial state:
dummy -> 1 -> 2 -> 3 -> 4 -> 5
first
second

After advancing first by n+1 steps (n=2):
dummy -> 1 -> 2 -> 3 -> 4 -> 5
               first
second

Final state before removal:
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
                              first
          second

After removal:
dummy -> 1 -> 2 -> 3 -> 5
               ↑_______|
```

This visualization helps to understand how the two pointers move and how their final positions allow us to remove the correct node.
