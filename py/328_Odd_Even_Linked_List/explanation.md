## Explanation: Odd Even Linked List

### Analysis of problem & input data

This problem focuses on reordering a singly linked list based on the indices of its nodes. The key aspects to consider are:

1. The problem asks to group odd-indexed nodes followed by even-indexed nodes.
2. The first node is considered odd, the second even, and so on.
3. The relative order within odd and even groups should be maintained.
4. The solution must use O(1) extra space and O(n) time complexity.

The main principle that makes this question simple is the realization that we can traverse the list once, maintaining two separate lists (odd and even), and then connect them at the end. This approach allows us to reorder the list in-place, satisfying the space complexity requirement.

The problem fits into the category of linked list manipulation, where we need to modify the next pointers of nodes to achieve the desired order. It's similar to other linked list problems that involve rearranging nodes, such as reversing a linked list or partitioning a linked list.

### Test cases

1. Normal case: `[1,2,3,4,5]` → `[1,3,5,2,4]`
2. Even length list: `[1,2,3,4]` → `[1,3,2,4]`
3. Odd length list: `[1,2,3,4,5,6,7]` → `[1,3,5,7,2,4,6]`
4. Two-element list: `[1,2]` → `[1,2]`
5. Single element list: `[1]` → `[1]`
6. Empty list: `[]` → `[]`

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

def test_odd_even_list(odd_even_list_func):
    test_cases = [
        [1,2,3,4,5],
        [1,2,3,4],
        [1,2,3,4,5,6,7],
        [1,2],
        [1],
        []
    ]

    for case in test_cases:
        head = create_linked_list(case)
        result = odd_even_list_func(head)
        print(f"Input: {case}")
        print(f"Output: {linked_list_to_list(result)}\n")

# Usage:
# test_odd_even_list(oddEvenList)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Two-pointer approach (Neetcode solution)
2. Dummy node approach
3. Recursive approach

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Using extra space to store odd and even nodes separately
2. Sorting the linked list based on indices

#### Worthy Solutions

##### Two-pointer approach (Neetcode solution)

```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head  # Pointer for odd-indexed nodes
        even = head.next  # Pointer for even-indexed nodes
        even_head = even  # Save the head of even-indexed nodes

        while even and even.next:
            # Connect odd nodes
            odd.next = even.next
            odd = odd.next

            # Connect even nodes
            even.next = odd.next
            even = even.next

        # Connect the end of odd list to the start of even list
        odd.next = even_head

        return head
```

Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once, visiting each node exactly once.
Space Complexity: O(1), as we only use a constant amount of extra space regardless of the input size.

Explanation of time and space complexity:

- Time: We iterate through the list once, performing constant time operations for each node. The while loop runs approximately n/2 times, but this is still O(n).
- Space: We only use a few additional pointers (odd, even, even_head) regardless of the input size, hence O(1) extra space.

Intuitions and invariants:

- We maintain two separate lists: one for odd-indexed nodes and one for even-indexed nodes.
- The `odd` pointer always points to the last node in the odd list.
- The `even` pointer always points to the last node in the even list.
- After each iteration, `odd.next` is the next odd-indexed node, and `even.next` is the next even-indexed node.
- The original order within odd and even groups is maintained because we're moving through the list sequentially.

##### Dummy node approach

```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_odd = ListNode(0)  # Dummy node for odd-indexed list
        dummy_even = ListNode(0)  # Dummy node for even-indexed list
        odd = dummy_odd
        even = dummy_even
        is_odd = True

        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next

            head = head.next
            is_odd = not is_odd

        # Connect odd list to even list
        odd.next = dummy_even.next
        even.next = None  # Ensure the last node points to None

        return dummy_odd.next
```

Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once, visiting each node exactly once.
Space Complexity: O(1), as we only use a constant amount of extra space regardless of the input size.

Explanation of time and space complexity:

- Time: We iterate through the list once, performing constant time operations for each node. The while loop runs n times, resulting in O(n) time complexity.
- Space: We use a constant number of additional pointers (dummy_odd, dummy_even, odd, even) regardless of the input size, hence O(1) extra space.

Intuitions and invariants:

- Using dummy nodes simplifies edge cases and list manipulation.
- The `is_odd` boolean flag alternates to determine whether the current node should go to the odd or even list.
- The original order within odd and even groups is maintained because we're moving through the list sequentially.
- At the end, we connect the odd list to the even list and ensure the last node points to None.

##### Recursive approach

```python
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reorder(odd, even, is_odd):
            if not even:
                odd.next = even_head
                return odd

            if is_odd:
                odd.next = even.next
                return reorder(odd.next, even, False) if odd.next else odd
            else:
                even.next = odd.next
                return reorder(odd, even.next, True)

        if not head or not head.next:
            return head

        even_head = head.next
        return reorder(head, head.next, False)
```

Time Complexity: O(n), where n is the number of nodes in the linked list. We visit each node once through recursive calls.
Space Complexity: O(n) in the worst case due to the call stack.

Explanation of time and space complexity:

- Time: We make a recursive call for each node in the list, performing constant time operations in each call. This results in O(n) time complexity.
- Space: In the worst case, the recursion depth can reach n/2 for a list with n nodes. This leads to O(n) space complexity due to the call stack.

Intuitions and invariants:

- The recursive approach alternates between processing odd and even nodes.
- The `is_odd` parameter keeps track of whether we're currently processing an odd or even node.
- The base case is when we reach the end of the even list, at which point we connect the odd list to the saved `even_head`.
- Each recursive call advances either the odd or even pointer and switches the `is_odd` flag.

#### Rejected Approaches

1. Using extra space to store odd and even nodes separately:
   This approach involves creating two new lists for odd and even nodes, then merging them. While correct, it uses O(n) extra space, violating the problem's space complexity requirement.

2. Sorting the linked list based on indices:
   This approach would involve assigning index values to each node and then sorting the list based on these indices. It's inefficient (O(n log n) time complexity) and unnecessarily complex for this problem.

#### Final Recommendations

The two-pointer approach (Neetcode solution) is the best to learn for this problem. It's intuitive, efficient, and satisfies both the time and space complexity requirements. It demonstrates a clear understanding of linked list manipulation and is likely to be well-received in an interview setting.

The dummy node approach is also worth understanding as it's a common technique in linked list problems, especially for handling edge cases more elegantly.

The recursive approach, while interesting, is not recommended for interviews due to its space complexity and potential for stack overflow with very large inputs.

### Visualization(s)

For a visual representation of the two-pointer approach, we can use ASCII art to show how the pointers move:

```
Initial state:
1 -> 2 -> 3 -> 4 -> 5 -> NULL
^    ^
odd  even (even_head)

After first iteration:
1 -> 3 -> 4 -> 5 -> NULL
     ^
     odd
2 -> 4 -> 5 -> NULL
     ^
     even

After second iteration:
1 -> 3 -> 5 -> NULL
          ^
          odd
2 -> 4 -> NULL
          ^
          even

Final state:
1 -> 3 -> 5 -> 2 -> 4 -> NULL
```

This visualization helps to understand how the `odd` and `even` pointers move through the list, rearranging the nodes as they go.
