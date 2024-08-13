# Explanation: Time-Based Key-Value Store

## Analysis of problem & input data

This problem involves designing a time-based key-value data structure that can handle multiple values for the same key at different timestamps. The key characteristics and constraints of this problem are:

1. We need to implement two main operations: `set` and `get`.
2. The `set` operation stores a key-value pair along with a timestamp.
3. The `get` operation retrieves the value for a key at a given timestamp or the most recent value before that timestamp.
4. Timestamps for `set` operations are strictly increasing.
5. The `get` operation needs to handle cases where the exact timestamp doesn't exist.
6. We need to efficiently handle up to 2 \* 10^5 calls to `set` and `get`.
7. Keys and values are strings of length up to 100 characters.
8. Timestamps are integers between 1 and 10^7.

The key principle that makes this question manageable is that the timestamps for each key are strictly increasing. This allows us to use a binary search approach for efficient retrieval.

### Test cases

Here are some test cases to cover various scenarios:

1. Basic set and get operations
2. Get operation with exact timestamp match
3. Get operation with timestamp between two stored values
4. Get operation with timestamp before any stored value
5. Get operation with timestamp after all stored values
6. Multiple values for the same key
7. Operations on non-existent keys

```python
def test_time_map():
    time_map = TimeMap()

    # Test case 1: Basic set and get
    time_map.set("key1", "value1", 1)
    assert time_map.get("key1", 1) == "value1"

    # Test case 2: Exact timestamp match
    time_map.set("key2", "value2", 2)
    assert time_map.get("key2", 2) == "value2"

    # Test case 3: Timestamp between two stored values
    time_map.set("key3", "value3_1", 1)
    time_map.set("key3", "value3_2", 3)
    assert time_map.get("key3", 2) == "value3_1"

    # Test case 4: Timestamp before any stored value
    assert time_map.get("key3", 0) == ""

    # Test case 5: Timestamp after all stored values
    assert time_map.get("key3", 4) == "value3_2"

    # Test case 6: Multiple values for the same key
    time_map.set("key4", "value4_1", 1)
    time_map.set("key4", "value4_2", 2)
    time_map.set("key4", "value4_3", 3)
    assert time_map.get("key4", 2) == "value4_2"
    assert time_map.get("key4", 3) == "value4_3"

    # Test case 7: Non-existent key
    assert time_map.get("non_existent", 1) == ""

# Run the tests
test_time_map()
print("All tests passed!")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. HashMap with Binary Search (Optimal)
2. HashMap with Sorted List and Binary Search
3. Two HashMaps (Timestamp to Value and Key to Timestamp List)
4. Trie with Timestamp Sorting

Count: 4 solutions

#### Rejected solutions

1. Linear search through all timestamps (inefficient for large datasets)
2. Maintaining a fully sorted list of all entries (inefficient for insertions)
3. Using a balanced binary search tree for each key (overly complex for this problem)

### Worthy Solutions

#### HashMap with Binary Search (Optimal)

```python
from typing import List, Tuple
from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Initialize a defaultdict to store key-value pairs with timestamps
        self.store: defaultdict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the new (timestamp, value) pair to the list for this key
        self.store[key].append((timestamp, value))
        # No need to sort here because timestamps are guaranteed to be in increasing order

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist, return an empty string
        if key not in self.store:
            return ""

        values = self.store[key]

        # Implement binary search
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                # Exact match found
                return values[mid][1]
            elif values[mid][0] < timestamp:
                # Search the right half
                left = mid + 1
            else:
                # Search the left half
                right = mid - 1

        # If we're here, we didn't find an exact match
        # Return the value with the largest timestamp_prev <= timestamp
        return values[right][1] if right >= 0 else ""

# Time Complexity:
# set: O(1)
# get: O(log n), where n is the number of timestamps for a given key

# Space Complexity: O(m), where m is the total number of key-value pairs stored
```

This solution uses a HashMap (implemented as a defaultdict in Python) to store key-value pairs along with their timestamps. The key insight is that we can use binary search for efficient retrieval because the timestamps are guaranteed to be in increasing order.

- **Intuition**: By keeping the timestamps sorted (which happens naturally due to the problem constraint), we can use binary search to efficiently find the correct value for a given timestamp.
- **Invariants**:
  1. Timestamps for each key are always in increasing order.
  2. The binary search always returns the largest timestamp less than or equal to the query timestamp.

#### HashMap with Sorted List and Binary Search

```python
from typing import List, Tuple
from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store: defaultdict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        # No need to sort as timestamps are guaranteed to be in increasing order

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        idx = bisect.bisect(values, (timestamp, chr(127)))
        return values[idx-1][1] if idx > 0 else ""

# Time Complexity:
# set: O(1)
# get: O(log n), where n is the number of timestamps for a given key

# Space Complexity: O(m), where m is the total number of key-value pairs stored
```

This solution is similar to the previous one but uses Python's `bisect` module for binary search. The `bisect` function finds the insertion point for a given element in a sorted list.

- **Intuition**: The `bisect` function can be used to find the rightmost position where we could insert the given timestamp while maintaining sorted order.
- **Invariants**:
  1. Timestamps for each key are always in increasing order.
  2. The `bisect` function always returns the index of the first element greater than the given timestamp.

#### Two HashMaps (Timestamp to Value and Key to Timestamp List)

```python
from typing import List
from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.key_time: defaultdict[str, List[int]] = defaultdict(list)
        self.time_value: dict[tuple[str, int], str] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time[key].append(timestamp)
        self.time_value[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_time:
            return ""

        times = self.key_time[key]
        idx = bisect.bisect(times, timestamp)
        if idx == 0:
            return ""
        return self.time_value[(key, times[idx-1])]

# Time Complexity:
# set: O(1)
# get: O(log n), where n is the number of timestamps for a given key

# Space Complexity: O(m), where m is the total number of key-value pairs stored
```

This solution uses two separate data structures: one to store the timestamps for each key, and another to store the actual values.

- **Intuition**: By separating the timestamps and values, we can perform binary search on just the timestamps, which can be more efficient for certain access patterns.
- **Invariants**:
  1. The `key_time` list for each key is always sorted.
  2. Every (key, timestamp) pair in `time_value` has a corresponding timestamp in `key_time[key]`.

#### Trie with Timestamp Sorting

```python
from typing import Optional

class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.timestamps: list[int] = []
        self.values: list[str] = []

class TimeMap:
    def __init__(self):
        self.root = TrieNode()

    def set(self, key: str, value: str, timestamp: int) -> None:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.timestamps.append(timestamp)
        node.values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        node = self._find_node(key)
        if not node:
            return ""
        return self._binary_search(node, timestamp)

    def _find_node(self, key: str) -> Optional[TrieNode]:
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _binary_search(self, node: TrieNode, timestamp: int) -> str:
        left, right = 0, len(node.timestamps) - 1
        while left <= right:
            mid = (left + right) // 2
            if node.timestamps[mid] == timestamp:
                return node.values[mid]
            elif node.timestamps[mid] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return node.values[right] if right >= 0 else ""

# Time Complexity:
# set: O(k), where k is the length of the key
# get: O(k + log n), where k is the length of the key and n is the number of timestamps for the key

# Space Complexity: O(m * k), where m is the total number of key-value pairs stored and k is the average key length
```

This solution uses a Trie data structure to store the keys, with each node containing a sorted list of timestamps and corresponding values.

- **Intuition**: A Trie can be more efficient for string keys, especially when there are many keys with common prefixes.
- **Invariants**:
  1. Each node's timestamps list is always sorted.
  2. The timestamps and values lists in each node are always of the same length and correspond to each other.

### Rejected Approaches

1. **Linear search through all timestamps**: This approach would involve storing all (key, value, timestamp) tuples in a list and searching through it linearly for each `get` operation. While simple to implement, it would be highly inefficient for large datasets, with a time complexity of O(n) for each `get` operation.

2. **Maintaining a fully sorted list of all entries**: This approach would keep a single list of all entries sorted by timestamp. While it would allow for efficient binary search during `get` operations, it would make `set` operations very slow (O(n) time complexity) due to the need to maintain the sorted order.

3. **Using a balanced binary search tree for each key**: While this would provide efficient operations (O(log n) for both `set` and `get`), it's overly complex for this problem. The strictly increasing timestamp constraint allows for simpler and equally efficient solutions.

### Final Recommendations

The HashMap with Binary Search (Optimal) solution is the best one to learn and implement for this problem. Here's why:

1. It's efficient: O(1) for `set` operations and O(log n) for `get` operations.
2. It's relatively simple to implement and understand.
3. It directly leverages the problem constraint of strictly increasing timestamps.
4. It uses common data structures (HashMap and list) that are available in most programming languages.

The HashMap with Sorted List and Binary Search is a close second and is worth understanding as well, especially if you're using a language with built-in binary search functions like Python's `bisect`.

The Two HashMaps and Trie solutions, while correct, add unnecessary complexity for this specific problem. They might be more suitable for variations of this problem (e.g., if keys had common prefixes or if we needed to perform range queries on timestamps).

Approaches like linear search or maintaining a fully sorted list of all entries should be avoided as they don't scale well with large datasets. Always consider the constraints and characteristics of the input data when designing your solution.

## Visualization(s)

To visualize the binary search process in the optimal solution, we can use a simple ASCII art representation:

```
Key: "foo"
Timestamps:  1    4    7    10   13
Values:     bar  baz  qux  quux corge

Get("foo", 8):

Step 1:     1    4    7    10   13
            ^         ^          ^
           left      mid       right

Step 2:     1    4    7    10   13
                      ^    ^    ^
                     left mid right

Step 3:     1    4    7    10   13
                      ^    ^
                     right left

Final result: "qux" (timestamp 7)
```

This visualization shows how the binary search narrows down the range of possible values until it finds the largest timestamp less than or equal to the query timestamp.
