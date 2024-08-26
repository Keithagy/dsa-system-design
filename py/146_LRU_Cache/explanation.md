## Explanation: LRU Cache

### Analysis of problem & input data

The Least Recently Used (LRU) Cache is a classic data structures problem that combines aspects of a hash map for fast lookups and a doubly linked list for efficient ordering and updates. The key characteristics of this problem are:

1. Fixed capacity: The cache has a maximum number of key-value pairs it can store.
2. Get operation: Retrieve a value by key in O(1) time.
3. Put operation: Insert or update a key-value pair in O(1) time.
4. Eviction policy: When the cache is full, remove the least recently used item.
5. Update access order: Every get or put operation should mark the accessed item as most recently used.

The core principle that makes this question simple is the combination of a hash map and a doubly linked list. The hash map provides O(1) access to cache items, while the doubly linked list maintains the order of recent use with O(1) updates to move an item to the front or remove it from the end.

This problem is about pattern-matching to the composite data structure design, where multiple data structures are combined to achieve the desired performance characteristics. It's a common pattern in system design questions and practical software engineering scenarios.

### Test cases

Here are some relevant test cases:

1. Basic functionality:

   - Initialize cache with capacity 2
   - Put (1, 1) and (2, 2)
   - Get 1 (should return 1)
   - Put (3, 3) (should evict 2)
   - Get 2 (should return -1)

2. Update existing key:

   - Initialize cache with capacity 2
   - Put (1, 1) and (2, 2)
   - Put (2, 3) (should update value and make 2 most recent)
   - Put (3, 3) (should evict 1)
   - Get 1 (should return -1)
   - Get 2 (should return 3)

3. Capacity 1 edge case:

   - Initialize cache with capacity 1
   - Put (1, 1)
   - Put (2, 2) (should evict 1)
   - Get 1 (should return -1)
   - Get 2 (should return 2)

4. Large capacity and frequent updates:
   - Initialize cache with capacity 3000
   - Put 3000 items
   - Update all items in reverse order
   - Verify order of items

Here's the executable Python code for these test cases:

```python
def test_lru_cache():
    # Test case 1: Basic functionality
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1

    # Test case 2: Update existing key
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(2, 3)
    cache.put(3, 3)
    assert cache.get(1) == -1
    assert cache.get(2) == 3

    # Test case 3: Capacity 1 edge case
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    # Test case 4: Large capacity and frequent updates
    cache = LRUCache(3000)
    for i in range(3000):
        cache.put(i, i)
    for i in range(2999, -1, -1):
        cache.put(i, i)
    for i in range(3000):
        assert cache.get(i) == i

    print("All test cases passed!")

# Run the tests
test_lru_cache()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Hash Map + Doubly Linked List: The optimal solution using a combination of a hash map and a doubly linked list.
2. OrderedDict: A Python-specific solution using the OrderedDict class from the collections module.

Count: 2 solutions

##### Rejected solutions

1. Simple dictionary with timestamp: Using a regular dictionary and storing timestamps for each access, sorting on eviction.
2. Array-based solution: Using an array to store key-value pairs and shifting elements on each access.

#### Worthy Solutions

##### Hash Map + Doubly Linked List

```python
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map for O(1) access
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node: Node) -> None:
        # Remove node from the doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: Node) -> None:
        # Add node to the end of the doubly linked list (most recently used)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
```

Time Complexity: O(1) for both get and put operations.

- get: O(1) for hash map lookup and O(1) for updating the doubly linked list.
- put: O(1) for hash map insertion/update and O(1) for updating the doubly linked list.

Space Complexity: O(capacity), where capacity is the maximum number of key-value pairs the cache can hold.

- The hash map and doubly linked list both store at most 'capacity' number of elements.

Explanation of time and space complexity:

- The hash map provides O(1) access to cache items.
- The doubly linked list allows for O(1) updates to the order of elements (removal and addition to the end).
- We maintain pointers to both ends of the list, allowing O(1) access to the least recently used item.
- The space used is directly proportional to the capacity of the cache.

Intuitions and invariants:

- The hash map always contains exactly the same keys as the doubly linked list.
- The order of nodes in the doubly linked list represents the order of recent use, with the tail being the most recent.
- The head.next is always the least recently used item, making eviction O(1).
- Dummy head and tail nodes simplify edge cases in list operations.

##### OrderedDict Solution

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed item to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key exists, move it to the end
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # If at capacity, remove the first item (least recently used)
            self.cache.popitem(last=False)
        self.cache[key] = value
```

Time Complexity: O(1) for both get and put operations.

- get: O(1) for OrderedDict lookup and O(1) for moving the item to the end.
- put: O(1) for OrderedDict insertion/update and O(1) for potential removal of the least recently used item.

Space Complexity: O(capacity), where capacity is the maximum number of key-value pairs the cache can hold.

- The OrderedDict stores at most 'capacity' number of elements.

Explanation of time and space complexity:

- OrderedDict in Python is implemented as a combination of a hash table and a doubly linked list, providing O(1) average case complexity for all operations.
- move_to_end() is an O(1) operation as it only involves updating pointers in the underlying doubly linked list.
- popitem(last=False) removes the first inserted item in O(1) time.

Intuitions and invariants:

- The order of items in the OrderedDict represents the order of recent use.
- New or accessed items are always moved to the end of the OrderedDict.
- The first item in the OrderedDict is always the least recently used.

#### Rejected Approaches

1. Simple dictionary with timestamp:

   - Approach: Use a regular dictionary to store key-value pairs along with a timestamp for each access. On eviction, sort the dictionary by timestamp.
   - Why rejected: Sorting on each eviction would result in O(n log n) time complexity, violating the O(1) requirement for put operations.

2. Array-based solution:
   - Approach: Use an array to store key-value pairs and shift elements on each access to maintain the order of recent use.
   - Why rejected: Shifting elements in an array is an O(n) operation, violating the O(1) requirement for both get and put operations.

#### Final Recommendations

The Hash Map + Doubly Linked List solution is the best to learn for several reasons:

1. It demonstrates a fundamental technique of combining data structures to achieve desired performance characteristics.
2. It provides insight into the internal workings of more abstract data structures like OrderedDict.
3. It's a common pattern in system design and can be adapted to various caching scenarios.
4. Implementing it from scratch showcases a deep understanding of data structures, which is valuable in coding interviews.

While the OrderedDict solution is concise and effective, it relies on a built-in Python data structure that may not be available in all languages or interview settings. Understanding the underlying implementation (Hash Map + Doubly Linked List) is more valuable for demonstrating algorithmic thinking and data structure knowledge.

### Visualization(s)

To visualize the LRU Cache operations, we can use a simple React component that demonstrates the state of the cache after each operation. Here's a basic implementation:

```tsx
import React, { useState } from "react";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

const LRUCacheVisualization = () => {
  const [cache, setCache] = useState(new Map());
  const [capacity, setCapacity] = useState(3);
  const [key, setKey] = useState("");
  const [value, setValue] = useState("");
  const [operations, setOperations] = useState([]);

  const handlePut = () => {
    if (key && value) {
      if (cache.size >= capacity && !cache.has(key)) {
        const lruKey = cache.keys().next().value;
        cache.delete(lruKey);
      }
      cache.delete(key);
      cache.set(key, value);
      setCache(new Map(cache));
      setOperations([...operations, `Put: (${key}, ${value})`]);
      setKey("");
      setValue("");
    }
  };

  const handleGet = () => {
    if (key) {
      const value = cache.get(key) || "Not found";
      if (cache.has(key)) {
        cache.delete(key);
        cache.set(key, value);
      }
      setCache(new Map(cache));
      setOperations([...operations, `Get: ${key} -> ${value}`]);
      setKey("");
    }
  };

  return (
    <div className="space-y-4">
      <Card>
        <CardHeader>LRU Cache (Capacity: {capacity})</CardHeader>
        <CardContent>
          {Array.from(cache).map(([k, v], index) => (
            <div key={index} className="mb-2">
              {k}: {v}
            </div>
          ))}
        </CardContent>
      </Card>
      <div className="flex space-x-2">
        <Input
          placeholder="Key"
          value={key}
          onChange={(e) => setKey(e.target.value)}
        />
        <Input
          placeholder="Value"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
        <Button onClick={handlePut}>Put</Button>
        <Button onClick={handleGet}>Get</Button>
      </div>
      <Card>
        <CardHeader>Operations</CardHeader>
        <CardContent>
          {operations.map((op, index) => (
            <div key={index}>{op}</div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
};

export default LRUCacheVisualization;
```

This visualization allows users to interactively see how the LRU Cache behaves with put and get operations, helping to reinforce understanding of the data structure's behavior.
