## Explanation: Rotate List

### Analysis of problem & input data

This problem involves rotating a linked list to the right by k places. The key aspects to consider are:

1. The linked list structure: We're dealing with a singly linked list, which means we can only traverse forward.
2. The rotation operation: We need to move the last k nodes to the front of the list.
3. The value of k: It can be larger than the length of the list, which means we need to handle this case efficiently.
4. Edge cases: Empty list, single node list, k = 0, or k equal to a multiple of the list length.

The key principle that makes this question simple is understanding that rotating a list by its length results in the same list. This means we can reduce k to k % length, which simplifies our approach.

Pattern matching: This problem falls into the category of linked list manipulation and circular array concepts. It's similar to problems involving finding cycles in linked lists or rotating arrays.

### Test cases

1. Normal case: head = [1,2,3,4,5], k = 2
   Expected output: [4,5,1,2,3]

2. Rotation equal to list length: head = [1,2,3], k = 3
   Expected output: [1,2,3]

3. Rotation greater than list length: head = [1,2,3], k = 5
   Expected output: [2,3,1]

4. Empty list: head = [], k = 3
   Expected output: []

5. Single node: head = [1], k = 2
   Expected output: [1]

6. No rotation: head = [1,2,3], k = 0
   Expected output: [1,2,3]

Here's the Python code for these test cases:

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

def test_rotate_list(rotate_right):
    test_cases = [
        ([1,2,3,4,5], 2, [4,5,1,2,3]),
        ([1,2,3], 3, [1,2,3]),
        ([1,2,3], 5, [2,3,1]),
        ([], 3, []),
        ([1], 2, [1]),
        ([1,2,3], 0, [1,2,3])
    ]

    for i, (values, k, expected) in enumerate(test_cases):
        head = create_linked_list(values)
        result = rotate_right(head, k)
        result_list = linked_list_to_list(result)
        assert result_list == expected, f"Test case {i+1} failed: expected {expected}, got {result_list}"
    print("All test cases passed!")

# Usage:
# test_rotate_list(your_rotate_right_function)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Two-pointer approach (Neetcode solution)
2. Connect tail to head and break the cycle
3. Recursive solution
4. Stack-based approach

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Creating a new list: This would use O(n) extra space, which is not optimal.
2. Rotating one by one: This would be inefficient for large k values.

#### Worthy Solutions

##### Two-pointer approach (Neetcode solution)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: empty list or single node
        if not head or not head.next:
            return head

        # Find the length of the list and the last node
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        # Adjust k if it's larger than the list length
        k = k % length
        if k == 0:
            return head

        # Find the new tail (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Adjust pointers to rotate the list
        new_head = new_tail.next
        new_tail.next = None
        last.next = head

        return new_head
```

Time Complexity: O(n), where n is the number of nodes in the list. We traverse the list twice in the worst case: once to find the length and last node, and once to find the new tail.

Space Complexity: O(1), as we only use a constant amount of extra space regardless of the input size.

Intuitions and invariants:

- The effective rotation is always k % length, as rotating by the list length gives the same list.
- The new head will be the (length - k)th node from the end.
- We can find this node by moving (length - k - 1) steps from the head.
- Connecting the original last node to the original head creates the rotation effect.

##### Connect tail to head and break the cycle

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Connect the tail to the head, creating a ring
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        old_tail.next = head

        # Find the new tail: (length - k % length - 1)th node
        # and the new head: (length - k % length)th node
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Break the ring

        return new_head
```

Time Complexity: O(n), where n is the number of nodes in the list. We traverse the list once to find its length and connect the tail to the head, and then at most once more to find the new tail.

Space Complexity: O(1), as we only use a constant amount of extra space.

Intuitions and invariants:

- By connecting the tail to the head, we create a circular linked list.
- The new head will be the (length - k % length)th node in this circular list.
- Breaking the circular list at the correct point completes the rotation.

##### Recursive solution

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rotate_and_get_length(node, k):
            if not node:
                return None, 0
            if not node.next:
                return node, 1

            new_head, length = rotate_and_get_length(node.next, k)
            if k % length == 0:
                return head, length

            if length == k % length:
                return node, length

            node.next = None
            return new_head, length

        new_head, _ = rotate_and_get_length(head, k)
        return new_head
```

Time Complexity: O(n), where n is the number of nodes in the list. We traverse the list once recursively.

Space Complexity: O(n) in the worst case due to the recursive call stack.

Intuitions and invariants:

- The recursion naturally reaches the end of the list, allowing us to count the length.
- As we unwind the recursion, we can determine the new head and tail based on the length and k.
- The base case of the recursion handles the rotation when we reach the end of the list.

##### Stack-based approach

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Push all nodes onto a stack
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next

        length = len(stack)
        k = k % length
        if k == 0:
            return head

        # Reconnect the nodes
        new_head = stack[-k]
        new_tail = stack[-k-1]
        stack[-1].next = head
        new_tail.next = None

        return new_head
```

Time Complexity: O(n), where n is the number of nodes in the list. We traverse the list once to build the stack.

Space Complexity: O(n), as we store all nodes in the stack.

Intuitions and invariants:

- The stack allows easy access to the last k elements, which will become the first elements after rotation.
- By storing all nodes, we can easily reconnect them in the rotated order.
- This approach trades space complexity for simplicity in node manipulation.

#### Rejected Approaches

1. Creating a new list: While this approach would work, it uses O(n) extra space, which is not optimal for this problem. The goal is to modify the existing list in-place.

2. Rotating one by one: This approach would involve moving the last node to the front k times. For large values of k, this would be very inefficient, potentially leading to a time complexity of O(n\*k).

3. Using a circular buffer or queue: While these data structures can handle rotations efficiently, they would require converting the linked list to a different data structure and back, which adds unnecessary complexity and potential space overhead.

#### Final Recommendations

The two-pointer approach (Neetcode solution) is the best to learn for several reasons:

1. Efficiency: It achieves O(n) time complexity with O(1) space complexity, which is optimal for this problem.
2. Intuitive: The solution directly addresses the problem by finding the new head and tail positions.
3. In-place: It modifies the existing list without requiring additional data structures.
4. Handles all cases: It efficiently deals with k values larger than the list length and other edge cases.
5. Widely applicable: The two-pointer technique is useful in many linked list problems, making this solution a good learning opportunity.

While the other approaches have their merits, the two-pointer solution provides the best balance of efficiency, simplicity, and educational value for interview preparation.

### Visualization(s)

To visualize the rotation process, let's consider a simple example with the two-pointer approach:

```
Initial list: 1 -> 2 -> 3 -> 4 -> 5, k = 2

Step 1: Find the length and last node
1 -> 2 -> 3 -> 4 -> 5
^                   ^
head                last
length = 5

Step 2: Adjust k and find new tail
k = 2 % 5 = 2
Move 5 - 2 - 1 = 2 steps from head
1 -> 2 -> 3 -> 4 -> 5
     ^         ^    ^
     new_tail  new_head

Step 3: Adjust pointers
4 -> 5 -> 1 -> 2 -> 3 -> null
^              ^
new_head       new_tail.next = null

Result: 4 -> 5 -> 1 -> 2 -> 3
```

This visualization shows how the two-pointer approach efficiently identifies the new head and tail positions, then reconnects the nodes to achieve the rotation.
