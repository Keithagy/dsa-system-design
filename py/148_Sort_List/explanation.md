## Explanation: Sort List

### Analysis of problem & input data

This problem requires sorting a singly linked list in ascending order. The key aspects to consider are:

1. Data structure: We're dealing with a singly linked list, which has O(1) access to the next element but O(n) access to arbitrary elements.
2. Input size: The list can have up to 5 \* 10^4 nodes, so we need an efficient algorithm.
3. Value range: Node values are between -10^5 and 10^5, which allows for potential optimization in some sorting algorithms.
4. Space complexity requirement: The follow-up question asks for O(1) space complexity, which rules out some straightforward solutions.

The principle that makes this question tractable is the realization that efficient sorting algorithms like merge sort can be adapted to work with linked lists. The key insight is that merging sorted linked lists is very efficient, and we can recursively divide the list without additional space overhead.

### Test cases

Here are some relevant test cases:

1. Empty list: `head = None`
2. Single node: `head = ListNode(1)`
3. Already sorted list: `head = ListNode(1) -> ListNode(2) -> ListNode(3)`
4. Reverse sorted list: `head = ListNode(3) -> ListNode(2) -> ListNode(1)`
5. List with duplicate values: `head = ListNode(3) -> ListNode(1) -> ListNode(2) -> ListNode(1)`
6. List with negative values: `head = ListNode(-1) -> ListNode(5) -> ListNode(-3) -> ListNode(4)`

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
    [],
    [1],
    [1, 2, 3],
    [3, 2, 1],
    [3, 1, 2, 1],
    [-1, 5, -3, 4]
]

for case in test_cases:
    head = create_linked_list(case)
    print(f"Input: {case}")
    # Call your sorting function here
    # sorted_head = sort_list(head)
    # print(f"Output: {linked_list_to_list(sorted_head)}")
    print()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Merge Sort (Top-down) - Neetcode solution
2. Merge Sort (Bottom-up)
3. Quick Sort
4. Insertion Sort

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Built-in sorting: Converting the linked list to an array, sorting it, and converting it back would be O(n) in space complexity, violating the follow-up constraint.
2. Bubble Sort: O(n^2) time complexity is too inefficient for large inputs.
3. Selection Sort: Also O(n^2) time complexity, too inefficient.
4. Heap Sort: While it's O(n log n) in time, it typically requires O(n) extra space for the heap when used with linked lists.

#### Worthy Solutions

##### Merge Sort (Top-down)

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Divide
        mid = slow.next
        slow.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next
```

Time Complexity: O(n log n)

- The list is recursively divided into two halves, which takes log n levels.
- At each level, we perform a linear-time merge operation.
- Therefore, the total time complexity is O(n log n).

Space Complexity: O(log n)

- The space complexity is determined by the recursion stack.
- The maximum depth of the recursion is log n (as we're halving the list each time).
- Therefore, the space complexity is O(log n).

Intuition and invariants:

- Divide and Conquer: The algorithm recursively divides the list into smaller sublists until we reach single-element lists (which are inherently sorted).
- Merge: We then merge these sorted sublists back together to form the final sorted list.
- The merge operation maintains the invariant that the output list is always sorted.
- The use of a dummy node in the merge operation simplifies handling the head of the merged list.

##### Merge Sort (Bottom-up)

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Count the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        step = 1

        while step < length:
            curr = dummy.next
            tail = dummy

            while curr:
                left = curr
                right = self.split(left, step)
                curr = self.split(right, step)

                tail = self.merge(left, right, tail)

            step *= 2

        return dummy.next

    def split(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        for _ in range(n - 1):
            if not head.next:
                break
            head = head.next

        second = head.next
        head.next = None
        return second

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode], tail: ListNode) -> ListNode:
        curr = tail

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        while curr.next:
            curr = curr.next

        return curr
```

Time Complexity: O(n log n)

- We perform log n iterations (doubling the step size each time).
- In each iteration, we merge sublists, which takes O(n) time in total.
- Therefore, the overall time complexity is O(n log n).

Space Complexity: O(1)

- We only use a constant amount of extra space for pointers and variables.
- The sorting is done in-place, fulfilling the follow-up requirement.

Intuition and invariants:

- Bottom-up approach: We start by merging 1-element sublists, then 2-element sublists, 4-element sublists, and so on.
- The `step` variable represents the current size of sublists being merged.
- The `split` function divides the list into sublists of size `step`.
- The `merge` function combines two sorted sublists while maintaining the sorted order.
- We use a dummy node to simplify handling the head of the list.

##### Quick Sort

```python
import random

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Choose a random pivot
        pivot = self.get_random_node(head)

        # Partition the list
        dummy_less = ListNode(0)
        dummy_equal = ListNode(0)
        dummy_greater = ListNode(0)
        less, equal, greater = dummy_less, dummy_equal, dummy_greater

        curr = head
        while curr:
            if curr.val < pivot.val:
                less.next = curr
                less = less.next
            elif curr.val > pivot.val:
                greater.next = curr
                greater = greater.next
            else:
                equal.next = curr
                equal = equal.next
            curr = curr.next

        # Terminate the sublists
        less.next = equal.next = greater.next = None

        # Recursively sort the sublists
        sorted_less = self.sortList(dummy_less.next)
        sorted_greater = self.sortList(dummy_greater.next)

        # Connect the sorted sublists
        return self.connect_lists(sorted_less, dummy_equal.next, sorted_greater)

    def get_random_node(self, head: ListNode) -> ListNode:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        return random.choice(nodes)

    def connect_lists(self, less: Optional[ListNode], equal: Optional[ListNode], greater: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        for sublist in (less, equal, greater):
            if sublist:
                curr.next = sublist
                while curr.next:
                    curr = curr.next

        return dummy.next
```

Time Complexity: O(n log n) on average, O(n^2) in the worst case

- The average-case time complexity is O(n log n) when the pivot choices divide the list roughly in half each time.
- In the worst case (always choosing the smallest or largest element as pivot), it degrades to O(n^2).

Space Complexity: O(log n) on average, O(n) in the worst case

- The space complexity is determined by the recursion stack.
- In the average case, the recursion depth is log n.
- In the worst case (unbalanced partitions), it can be O(n).

Intuition and invariants:

- Divide and Conquer: We partition the list around a randomly chosen pivot.
- The partitioning ensures that all elements less than the pivot come before it, and all elements greater come after it.
- Random pivot selection helps to avoid the worst-case scenario of always choosing the smallest or largest element.
- The algorithm maintains the invariant that after each partition, the pivot is in its final sorted position.

##### Insertion Sort

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        last_sorted = head
        curr = head.next

        while curr:
            if last_sorted.val <= curr.val:
                last_sorted = last_sorted.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next

                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr

            curr = last_sorted.next

        return dummy.next
```

Time Complexity: O(n^2)

- In the worst case (reverse sorted input), we need to scan through the entire sorted portion for each element.
- This results in a quadratic time complexity.

Space Complexity: O(1)

- The algorithm sorts the list in-place, using only a constant amount of extra space.

Intuition and invariants:

- We maintain a sorted portion at the beginning of the list and gradually expand it.
- For each new element, we find its correct position in the sorted portion and insert it there.
- The `last_sorted` pointer keeps track of the last node in the sorted portion.
- We use a dummy node to simplify handling the head of the list.

#### Rejected Approaches

1. Built-in sorting: While tempting for its simplicity, converting the linked list to an array, sorting it, and converting it back would require O(n) extra space, violating the follow-up constraint of O(1) space complexity.

2. Bubble Sort: Although it can be implemented with O(1) space complexity, its O(n^2) time complexity makes it too inefficient for large inputs (up to 5 \* 10^4 nodes in this case).

3. Selection Sort: Similar to Bubble Sort, it has O(n^2) time complexity, making it unsuitable for large inputs.

4. Heap Sort: While it achieves O(n log n) time complexity, implementing it efficiently for a linked list typically requires O(n) extra space for the heap structure, violating the space constraint.

#### Final Recommendations

The Merge Sort (Bottom-up) approach is the best solution to learn for this problem. Here's why:

1. Time Complexity: It achieves the optimal O(n log n) time complexity.
2. Space Complexity: It satisfies the follow-up requirement of O(1) space complexity.
3. Stability: It's a stable sorting algorithm, which can be important in some applications.
4. Consistency: Unlike Quick Sort, its performance doesn't degrade in worst-case scenarios.

While the Top-down Merge Sort is slightly easier to understand and implement, it doesn't meet the O(1) space requirement due to its recursive nature. The Bottom-up approach, although a bit more complex, overcomes this limitation.

Quick Sort is a good alternative to know, but its worst-case time and space complexities make it less ideal for this specific problem. Insertion Sort, while simple and in-place, is too slow for large inputs.

### Visualization(s)

For this problem, a visual representation of the Bottom-up Merge Sort process would be helpful. Here's a simple ASCII visualization of how the algorithm works on a small example:

```
Initial list: 4 -> 2 -> 1 -> 3

Step 1 (merging 1-element sublists):
[4] [2] [1] [3]
 ↓    ↓   ↓   ↓
[2,4] [1,3]

Step 2 (merging 2-element sublists):
[2,4] [1,3]
   ↓     ↓
[1,2,3,4]

Final sorted list: 1 -> 2 -> 3 -> 4
```

This visualization shows how the Bottom-up Merge Sort starts by considering each element as a sorted sublist of length 1, then iteratively merges adjacent sublists to form longer sorted sublists until the entire list is sorted.
