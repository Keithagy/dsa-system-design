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

Would you like me to explain any part of this implementation in more detail?
