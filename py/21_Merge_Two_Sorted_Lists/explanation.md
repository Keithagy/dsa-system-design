# Explanation: Merge Two Sorted Lists

## Analysis of problem & input data

This problem is a classic example of merging two sorted sequences, specifically applied to linked lists. The key characteristics and insights are:

1. **Input structure**: Two sorted linked lists, potentially of different lengths.
2. **Sorting order**: Both lists are sorted in non-decreasing order (ascending).
3. **Output requirement**: A single merged list that maintains the sorted order.
4. **In-place merging**: The problem asks to splice the nodes, implying an in-place merge rather than creating a new list.
5. **Node range**: The number of nodes in each list is between 0 and 50, inclusive.
6. **Value range**: Each node's value is between -100 and 100, inclusive.

Key principle that makes this question simple:

- The lists are already sorted, so we can always compare the current nodes of both lists and choose the smaller one to add to our result.
- We can leverage the existing nodes and simply adjust their next pointers, avoiding the need for new node creation.

### Test cases

1. **Both lists non-empty, same length**:

   - Input: list1 = [1,2,4], list2 = [1,3,4]
   - Expected Output: [1,1,2,3,4,4]

2. **Both lists empty**:

   - Input: list1 = [], list2 = []
   - Expected Output: []

3. **One list empty, other non-empty**:

   - Input: list1 = [], list2 = [0]
   - Expected Output: [0]

4. **Lists with different lengths**:

   - Input: list1 = [1,3,5], list2 = [2,4,6,8]
   - Expected Output: [1,2,3,4,5,6,8]

5. **One list is a subset of the other**:

   - Input: list1 = [1,2,3], list2 = [2]
   - Expected Output: [1,2,2,3]

6. **Lists with negative numbers**:
   - Input: list1 = [-2,1,3], list2 = [-1,0,4]
   - Expected Output: [-2,-1,0,1,3,4]

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

def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_merge_lists(merge_function):
    test_cases = [
        ([1,2,4], [1,3,4]),
        ([], []),
        ([], [0]),
        ([1,3,5], [2,4,6,8]),
        ([1,2,3], [2]),
        ([-2,1,3], [-1,0,4])
    ]

    for i, (list1_vals, list2_vals) in enumerate(test_cases, 1):
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        result = merge_function(list1, list2)
        print(f"Test case {i}:")
        print(f"Input: list1 = {list1_vals}, list2 = {list2_vals}")
        print(f"Output: {list_to_array(result)}")
        print()

# Usage:
# test_merge_lists(your_merge_function)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Iterative in-place merge (optimal)
2. Recursive merge
3. Dummy node approach

Count: 3 solutions

#### Rejected solutions

1. Creating a new list and copying nodes
2. Sorting a combined list of all nodes

### Worthy Solutions

#### 1. Iterative in-place merge (optimal)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Edge case: if either list is empty, return the other list
    if not list1:
        return list2
    if not list2:
        return list1

    # Choose the head of the merged list
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    current = head

    # Iterate through both lists, always choosing the smaller node
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach any remaining nodes
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return head
```

Time Complexity: O(n + m), where n and m are the lengths of list1 and list2 respectively.
Space Complexity: O(1), as we only use a constant amount of extra space.

Key intuitions and invariants:

- We maintain a `current` pointer that always points to the last node in our merged list.
- At each step, we choose the smaller of the two current nodes and append it to our result.
- The `while` loop invariant: At the start of each iteration, `current` points to the last node of the merged portion, and `list1` and `list2` point to the first unmerged nodes of their respective lists.
- After the main loop, at most one of the lists will have remaining elements, which we can directly append.

#### 2. Recursive merge

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Base cases: if either list is empty, return the other list
    if not list1:
        return list2
    if not list2:
        return list1

    # Recursive case: choose the smaller node and recurse
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
```

Time Complexity: O(n + m), where n and m are the lengths of list1 and list2 respectively.
Space Complexity: O(n + m) in the worst case due to the recursive call stack.

Key intuitions and invariants:

- The recursive approach leverages the fact that merging two sorted lists is essentially the same problem as merging the rest of the lists after choosing the smaller first element.
- Each recursive call decides on one node of the final merged list.
- The base cases handle the situation when one or both lists are empty.
- The recursive invariant: At each step, we're always working with the current nodes of two sorted lists.

#### 3. Dummy node approach

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to simplify the merging process
    dummy = ListNode(0)
    current = dummy

    # Iterate through both lists, always choosing the smaller node
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach any remaining nodes
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    # Return the merged list, excluding the dummy node
    return dummy.next
```

Time Complexity: O(n + m), where n and m are the lengths of list1 and list2 respectively.
Space Complexity: O(1), as we only use a constant amount of extra space.

Key intuitions and invariants:

- The dummy node simplifies the merging process by eliminating the need for special handling of the head of the merged list.
- The `current` pointer always points to the last node in our merged list, starting from the dummy node.
- The main loop invariant is the same as in the iterative approach.
- After the main loop, we handle any remaining nodes in either list.
- By returning `dummy.next`, we exclude the dummy node from the final result.

### Rejected Approaches

1. **Creating a new list and copying nodes**:

   - While this approach would work, it's not optimal in terms of space complexity.
   - It would require O(n + m) extra space to create new nodes for the merged list.
   - The problem specifically asks to splice together the nodes of the first two lists, implying an in-place merge is preferred.

2. **Sorting a combined list of all nodes**:
   - This approach would involve detaching all nodes from both lists, combining them into a single list or array, and then sorting.
   - Time complexity would be O((n+m) log(n+m)) due to the sorting step, which is less efficient than the linear time solutions.
   - This approach doesn't leverage the fact that the input lists are already sorted, which is a key aspect of the problem.

### Final Recommendations

The iterative in-place merge (Solution 1) is the best approach to learn and use in an interview setting. Here's why:

1. It has optimal time complexity O(n + m) and space complexity O(1).
2. It directly addresses the problem requirement of splicing together the existing nodes.
3. It's intuitive and easy to explain, which is crucial in an interview setting.
4. It doesn't rely on recursion, avoiding potential stack overflow issues with very large lists.

The recursive solution, while elegant, is not as practical due to its space complexity and potential for stack overflow with large inputs. However, it's worth understanding as it demonstrates a different problem-solving approach.

The dummy node approach is also valid and has the same time and space complexity as the optimal solution. It's a good technique to know as it simplifies edge case handling in linked list problems. However, it introduces an extra node that needs to be dealt with at the end, which slightly complicates the code.

Approaches like creating a new list or sorting a combined list should be avoided as they don't leverage the problem's key characteristic (input lists are already sorted) and are less efficient in terms of time or space complexity.

Remember, in an interview, it's important to discuss these trade-offs and demonstrate your understanding of why certain approaches are better than others.

## Visualization(s)

To visualize the merging process, we can use a simple ASCII representation. Let's consider merging two lists: [1,3,5] and [2,4,6].

```
Step 1: Initial state
List1: 1 -> 3 -> 5 -> None
List2: 2 -> 4 -> 6 -> None
Merged: None

Step 2: After first comparison
List1: 3 -> 5 -> None
List2: 2 -> 4 -> 6 -> None
Merged: 1 -> None

Step 3: After second comparison
List1: 3 -> 5 -> None
List2: 4 -> 6 -> None
Merged: 1 -> 2 -> None

Step 4: After third comparison
List1: 5 -> None
List2: 4 -> 6 -> None
Merged: 1 -> 2 -> 3 -> None

Step 5: After fourth comparison
List1: 5 -> None
List2: 6 -> None
Merged: 1 -> 2 -> 3 -> 4 -> None

Step 6: After fifth comparison
List1: None
List2: 6 -> None
Merged: 1 -> 2 -> 3 -> 4 -> 5 -> None

Final Step: Attach remaining nodes
List1: None
List2: None
Merged: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
```

This visualization helps to understand how the algorithm progresses step by step, always choosing the smaller of the two current nodes and appending it to the merged list.
