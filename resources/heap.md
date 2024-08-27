Certainly, I can provide you with a Python implementation of an array-backed heap from scratch. Let's create a min-heap (where the smallest element is at the root) using a list as the underlying data structure.

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != i:
            self.swap(i, min_index)
            self._heapify_down(min_index)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def __str__(self):
        return str(self.heap)

# Example usage
heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(5)
heap.insert(4)

print("Heap after insertions:", heap)

print("Extracted min:", heap.extract_min())
print("Heap after extraction:", heap)

# Building a heap from an existing array
arr = [9, 4, 7, 1, 2, 6, 3]
heap.build_heap(arr)
print("Heap built from array:", heap)

```

This implementation provides a `MinHeap` class with the following methods:

1. `insert(key)`: Inserts a new element into the heap.
2. `extract_min()`: Removes and returns the minimum element from the heap.
3. `build_heap(arr)`: Builds a heap from an existing array.

The class also includes helper methods for maintaining the heap property:

- `_heapify_up(i)`: Moves an element up the heap to its correct position.
- `_heapify_down(i)`: Moves an element down the heap to its correct position.

The heap is represented using a Python list, where for any element at index `i`:

- Its parent is at index `(i - 1) // 2`
- Its left child is at index `2 * i + 1`
- Its right child is at index `2 * i + 2`

This implementation ensures that the smallest element is always at the root (index 0) of the heap.

Here's a concise overview of the simple Python syntax for using a heap:

```python
import heapq

# Create an empty heap
heap = []

# Push elements onto the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)

# Pop the smallest element
smallest = heapq.heappop(heap)

# Peek at the smallest element without removing it
smallest = heap[0]

# Convert a list to a heap in-place
my_list = [5, 3, 7, 1, 9]
heapq.heapify(my_list)

# Push an item and pop the smallest in one operation
next_item = heapq.heapreplace(heap, 6)
```

This covers the basic operations for a min-heap. Python's `heapq` module implements a min-heap by default. If you need a max-heap, you can negate the values when pushing and popping.

Would you like me to explain any of these operations in more detail?
Certainly, I'd be happy to remind you of the runtime complexities for heap operations. Here's a breakdown:

1. Creation (heapify):

   - O(n) where n is the number of elements

2. Insertion (heappush):

   - O(log n)

3. Deletion of minimum/maximum element (heappop):

   - O(log n)

4. Peeking at the top element:

   - O(1)

5. Replacing the top element (heapreplace):

   - O(log n)

6. Removing and adding a new element (heappushpop):

   - O(log n)

7. Checking if the heap is empty:

   - O(1)

8. Getting the size of the heap:
   - O(1)

It's worth noting that these complexities assume a binary heap implementation, which is what Python's `heapq` module uses. The O(log n) complexity for insertion and deletion operations comes from the need to maintain the heap property by potentially swapping elements up or down the tree.

The O(n) complexity for heapify is actually better than building a heap by n insertions (which would be O(n log n)). This is because heapify uses a clever bottom-up approach that's more efficient.

Yes, you can specify a key to maintain the heap invariant in Python, although it requires a bit more work than the basic `heapq` operations. Python's `heapq` module doesn't directly support custom comparison keys, but you can achieve this functionality using a wrapper class or tuples. Here are two approaches:

1. Using a wrapper class:

```python
import heapq

class KeyWrapper:
    def __init__(self, item, key_func):
        self.item = item
        self.key = key_func(item)

    def __lt__(self, other):
        return self.key < other.key

class CustomKeyHeap:
    def __init__(self, key_func):
        self.key_func = key_func
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, KeyWrapper(item, self.key_func))

    def pop(self):
        return heapq.heappop(self.heap).item

    def peek(self):
        return self.heap[0].item if self.heap else None

# Example usage:
heap = CustomKeyHeap(key_func=lambda x: x['priority'])
heap.push({'name': 'Task 1', 'priority': 3})
heap.push({'name': 'Task 2', 'priority': 1})
heap.push({'name': 'Task 3', 'priority': 2})

print(heap.pop())  # {'name': 'Task 2', 'priority': 1}
print(heap.pop())  # {'name': 'Task 3', 'priority': 2}
print(heap.pop())  # {'name': 'Task 1', 'priority': 3}

```

2. Using tuples (simpler, but less flexible):

```python
import heapq

# Create a list of tuples (priority, task)
heap = []
heapq.heappush(heap, (3, 'Task 1'))
heapq.heappush(heap, (1, 'Task 2'))
heapq.heappush(heap, (2, 'Task 3'))

# Pop items
print(heapq.heappop(heap)[1])  # 'Task 2'
print(heapq.heappop(heap)[1])  # 'Task 3'
print(heapq.heappop(heap)[1])  # 'Task 1'
```

The wrapper class approach is more flexible as it allows you to use complex objects and specify any comparison key. The tuple approach is simpler but limited to cases where you can easily represent your items as tuples with the key as the first element.

Both methods maintain the same O(log n) time complexity for push and pop operations.

Would you like me to explain either of these approaches in more detail?
