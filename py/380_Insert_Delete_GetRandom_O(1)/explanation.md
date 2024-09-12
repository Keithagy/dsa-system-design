## Explanation: Insert Delete GetRandom O(1)

### Analysis of problem & input data

This problem is a classic example of data structure design, where we need to implement a set with specific operations that must be performed in average O(1) time complexity. The key aspects of the problem are:

1. We need to support three operations: insert, remove, and getRandom.
2. All operations must be performed in average O(1) time.
3. The getRandom operation must return a random element with equal probability for all elements.

The main challenge here is to achieve O(1) time complexity for all operations, especially the getRandom operation. This requires a clever combination of data structures to achieve the desired performance.

The key principle that makes this question simple is the realization that we can use an array for O(1) random access and a hash map for O(1) insertion and deletion. By combining these two data structures, we can achieve the required time complexity for all operations.

### Test cases

Here are some relevant test cases:

1. Basic operations:

   - Insert a new element
   - Insert an existing element
   - Remove an existing element
   - Remove a non-existing element
   - Get random element

2. Edge cases:

   - Insert and remove when the set is empty
   - Get random when there's only one element
   - Insert and remove the same element multiple times

3. Large scale test:
   - Insert a large number of elements
   - Remove a large number of elements
   - Perform getRandom multiple times to check for uniformity

Here's the Python code for these test cases:

```python
def test_randomized_set():
    rs = RandomizedSet()

    # Basic operations
    assert rs.insert(1) == True
    assert rs.insert(2) == True
    assert rs.insert(1) == False
    assert rs.remove(1) == True
    assert rs.remove(3) == False

    # Edge cases
    assert rs.remove(2) == True
    assert rs.insert(3) == True
    random_val = rs.getRandom()
    assert random_val == 3

    # Large scale test
    for i in range(1000):
        rs.insert(i)

    for i in range(0, 1000, 2):
        rs.remove(i)

    random_counts = {}
    for _ in range(10000):
        val = rs.getRandom()
        random_counts[val] = random_counts.get(val, 0) + 1

    # Check if the distribution is roughly uniform
    expected_count = 10000 // 500
    for count in random_counts.values():
        assert 0.8 * expected_count <= count <= 1.2 * expected_count

test_randomized_set()
print("All tests passed!")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Array + Hash Map (Neetcode solution)
2. Linked List + Hash Map

Count: 2 solutions (1 Neetcode solution)

##### Rejected solutions

1. Using only a Hash Set: This would work for insert and remove in O(1), but getRandom would be O(n).
2. Using only an Array: This would work for getRandom in O(1), but remove would be O(n).
3. Using a Binary Search Tree: This would give O(log n) complexity for all operations, which is not optimal.

#### Worthy Solutions

##### Array + Hash Map (Neetcode solution)

```python
import random

class RandomizedSet:
    def __init__(self):
        self.num_map = {}  # val -> index in num_list
        self.num_list = []  # list of values

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        self.num_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
        # Move the last element to the place idx of the element to delete
        last_element, idx = self.num_list[-1], self.num_map[val]
        self.num_list[idx], self.num_map[last_element] = last_element, idx
        # Delete the last element
        self.num_list.pop()
        del self.num_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)
```

Time Complexity:

- insert(): O(1) average case. The hash map insertion and list append are both O(1) operations.
- remove(): O(1) average case. The hash map lookup, deletion, and list pop are all O(1) operations. The trick of swapping with the last element ensures we don't need to shift elements in the list.
- getRandom(): O(1). random.choice() on a list is an O(1) operation.

Space Complexity: O(n), where n is the number of elements in the set. We store each element in both a list and a hash map.

Intuitions and invariants:

- The list (num_list) allows for O(1) random access, which is crucial for the getRandom() operation.
- The hash map (num_map) allows for O(1) lookup of the index of an element in the list, which is crucial for O(1) removal.
- By always swapping the element to be removed with the last element in the list, we ensure that removal can be done in O(1) time without leaving gaps in the list.
- The invariant maintained is that for every element val in the set, num_map[val] is always equal to the index of val in num_list.

##### Linked List + Hash Map

```python
import random

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class RandomizedSet:
    def __init__(self):
        self.num_map = {}  # val -> ListNode
        self.head = ListNode(0)  # Dummy head
        self.tail = ListNode(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        new_node = ListNode(val)
        # Insert at the end of the list (before tail)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.num_map[val] = new_node
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_map:
            return False
        node = self.num_map[val]
        # Remove node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.num_map[val]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        if self.size == 0:
            return None
        index = random.randint(0, self.size - 1)
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val
```

Time Complexity:

- insert(): O(1) average case. The hash map insertion and linked list insertion are both O(1) operations.
- remove(): O(1) average case. The hash map lookup and linked list removal are both O(1) operations.
- getRandom(): O(n) worst case, where n is the number of elements. We need to traverse the linked list to reach the randomly chosen index.

Space Complexity: O(n), where n is the number of elements in the set. We store each element in both a linked list node and a hash map.

Intuitions and invariants:

- The linked list allows for O(1) insertion and deletion at any position, which is crucial for the insert() and remove() operations.
- The hash map allows for O(1) lookup of the node containing a specific value, which is crucial for O(1) removal.
- The dummy head and tail nodes simplify edge cases in insertion and deletion.
- The size variable allows us to generate a random index in the correct range for getRandom().
- The invariant maintained is that for every element val in the set, num_map[val] always points to the ListNode containing val in the linked list.

#### Rejected Approaches

1. Using only a Hash Set:

   - While this would allow O(1) insert and remove operations, getRandom would be O(n) because we'd need to convert the set to a list to select a random element.
   - This approach is rejected because it doesn't meet the O(1) time complexity requirement for all operations.

2. Using only an Array:

   - This would allow O(1) insert (at the end) and getRandom operations, but remove would be O(n) because we'd need to shift elements to fill the gap left by the removed element.
   - This approach is rejected because it doesn't meet the O(1) time complexity requirement for all operations.

3. Using a Binary Search Tree:
   - This would give O(log n) complexity for all operations, which is not optimal for this problem.
   - While it's better than O(n), it still doesn't meet the O(1) requirement.

#### Final Recommendations

The Array + Hash Map solution (Neetcode solution) is the best to learn for this problem. Here's why:

1. It achieves O(1) average time complexity for all operations, meeting the problem requirements perfectly.
2. It's space-efficient, using only an array and a hash map.
3. The implementation is relatively simple and easy to understand.
4. It demonstrates a clever technique of swapping with the last element for efficient removal, which is a useful pattern to know for other problems.

The Linked List + Hash Map solution, while interesting, is less optimal because getRandom becomes O(n) in the worst case. However, it's still worth understanding as it demonstrates how different data structures can be combined to solve problems, and it could be useful in variations of this problem where order matters.

### Visualization(s)

For the Array + Hash Map solution, here's a simple visualization of how the data structures change with operations:

```mermaid
graph TD
    subgraph "num_list"
    A[1] --> B[2] --> C[3]
    end
    subgraph "num_map"
    D[1 -> 0] --> E[2 -> 1] --> F[3 -> 2]
    end
    G[Initial State]

    subgraph "num_list"
    H[1] --> I[3] --> J[2]
    end
    subgraph "num_map"
    K[1 -> 0] --> L[3 -> 1] --> M[2 -> 2]
    end
    N[After remove(2)]

    G --> N
```

This visualization shows how the data structures look initially and after removing the element 2. Notice how 2 is replaced by the last element (3) in the list, and the hash map is updated accordingly. This is the key to achieving O(1) removal time.
