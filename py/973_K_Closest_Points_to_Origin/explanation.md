# Explanation: K Closest Points to Origin

## Analysis of problem & input data

This problem involves finding the K closest points to the origin (0, 0) in a 2D plane. The key aspects to consider are:

1. Euclidean distance calculation: The distance between two points is given by the formula √(x₁ - x₂)² + (y₁ - y₂)². In this case, we're always calculating the distance from (0, 0), so it simplifies to √(x² + y²).

2. Sorting vs. selection: We need to find the K closest points, which doesn't necessarily require sorting all points.

3. Comparison optimization: Since we're only comparing distances and not using the actual distance values, we can compare x² + y² instead of √(x² + y²), avoiding the costly square root operation.

4. Input constraints: The number of points can be up to 10^4, and the coordinate values are between -10^4 and 10^4. This suggests that we should aim for a solution with O(n log n) time complexity or better.

5. Output order: The answer can be returned in any order, which gives us flexibility in our approach.

6. Uniqueness: The answer is guaranteed to be unique except for the order, which means we don't need to handle tie-breaking scenarios.

The key principle that makes this question simple is that we can compare squared distances instead of actual distances, avoiding the need for square root calculations.

Solution approaches include:

1. Sort all points by distance (most elegant, but not most efficient)
2. Max heap (efficient and intuitive)
3. Quick select (most efficient in average case)
4. Partial sort using a min heap (efficient and relatively simple)
5. Bucket sort (efficient for specific input distributions)

(5 approaches in total)

## Solutions

### 1. Sort all points by distance

```python
from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the points based on their squared distance from the origin
        # We use squared distance to avoid costly square root calculations
        return sorted(points, key=lambda point: point[0]**2 + point[1]**2)[:k]

```

Time complexity: O(n log n), where n is the number of points
Space complexity: O(n) for the sorting algorithm

Intuitions and invariants:

- Sorting all points by their distance from the origin ensures that the first K points are the closest.
- Using squared distance instead of actual distance preserves the order and avoids square root calculations.
- This approach is simple and works well for small datasets or when you need all points sorted by distance.

### 2. Max heap

```python
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max heap to keep track of the K closest points
        heap = []

        for x, y in points:
            # Calculate the negative squared distance
            # We use negative because heapq implements a min heap
            dist = -(x*x + y*y)

            if len(heap) < k:
                # If we haven't found K points yet, add the current point
                heapq.heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:
                # If we have K points and the current point is closer than the farthest point in the heap,
                # remove the farthest point and add the current point
                heapq.heapreplace(heap, (dist, x, y))

        # Return the K points in the heap
        return [[x, y] for (dist, x, y) in heap]

```

Time complexity: O(n log k), where n is the number of points
Space complexity: O(k) for the heap

Intuitions and invariants:

- We maintain a max heap of size K, which always contains the K closest points seen so far.
- By using a max heap, we can quickly (in O(log k) time) determine if a new point is closer than the farthest point in our current set.
- This approach is efficient when K is significantly smaller than the total number of points.

### 3. Quick select

```python
from typing import List
import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0]**2 + point[1]**2

        def partition(left, right, pivot_idx):
            pivot = distance(points[pivot_idx])
            # Move pivot to end
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if distance(points[i]) < pivot:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1
            # Move pivot to its final place
            points[right], points[store_idx] = points[store_idx], points[right]
            return store_idx

        def select(left, right):
            if left == right:
                return

            # Choose a random pivot
            pivot_idx = random.randint(left, right)

            # Partition the array
            pivot_idx = partition(left, right, pivot_idx)

            if k == pivot_idx:
                # We've found the kth smallest element
                return
            elif k < pivot_idx:
                # The kth smallest is in the left part
                select(left, pivot_idx - 1)
            else:
                # The kth smallest is in the right part
                select(pivot_idx + 1, right)

        select(0, len(points) - 1)
        return points[:k]

```

Time complexity: O(n) average case, O(n^2) worst case
Space complexity: O(1) (in-place partitioning)

Intuitions and invariants:

- Quick select is based on the partitioning step of quicksort.
- We repeatedly partition the array and narrow down the section where the Kth element must be.
- By choosing pivots randomly, we achieve O(n) average time complexity.
- This approach is the most efficient for large datasets when we only need the K closest points and don't need them sorted.

### 4. Partial sort using a min heap

```python
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Convert points to a list of tuples (distance, x, y)
        heap = [(x*x + y*y, x, y) for x, y in points]

        # Transform the list into a heap in-place
        heapq.heapify(heap)

        # Pop the K smallest elements from the heap
        return [[x, y] for (_, x, y) in heapq.nsmallest(k, heap)]

```

Time complexity: O(n + k log n), where n is the number of points
Space complexity: O(n) for the heap

Intuitions and invariants:

- We create a min heap of all points based on their squared distances.
- Heapify operation takes O(n) time.
- Extracting the K smallest elements takes O(k log n) time.
- This approach is efficient when K is relatively small compared to n and we don't need to sort all points.

### 5. Bucket sort

```python
from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Find the maximum possible distance
        max_dist = 20000  # sqrt(10000^2 + 10000^2)
        buckets = [[] for _ in range(max_dist + 1)]

        for x, y in points:
            # Calculate the distance and use it as the bucket index
            dist = int(math.sqrt(x*x + y*y))
            buckets[dist].append([x, y])

        result = []
        for bucket in buckets:
            result.extend(bucket)
            if len(result) >= k:
                return result[:k]

        return result  # This line should never be reached given the problem constraints

```

Time complexity: O(n) average case, assuming uniformly distributed distances
Space complexity: O(n + m), where m is the range of possible distances

Intuitions and invariants:

- We use the distance as an index to sort points into buckets.
- This approach works well when the points are somewhat uniformly distributed.
- It can be very fast for certain input distributions, but may use a lot of memory for sparse distributions.

## Recommendation

For a technical coding interview setting, I would recommend the Max Heap approach (Solution 2) as the best one to learn and implement. Here's why:

1. It has a good balance of efficiency (O(n log k) time complexity) and simplicity.
2. It demonstrates understanding of heap data structures, which are commonly used in interview problems.
3. It's more efficient than sorting when k is significantly smaller than n.
4. It's easier to explain and implement correctly in an interview setting compared to Quick Select.
5. It uses less memory than the sorting approach.

The Quick Select approach is the most efficient in terms of average-case time complexity, but it's more complex to implement correctly and explain in an interview setting. However, it's definitely worth mentioning as an optimal solution if you have time.

## Test cases

```python
def test_kClosest():
    solution = Solution()

    # Test case 1
    assert solution.kClosest([[1,3],[-2,2]], 1) == [[-2,2]]

    # Test case 2
    result = solution.kClosest([[3,3],[5,-1],[-2,4]], 2)
    assert len(result) == 2
    assert [3,3] in result
    assert [-2,4] in result

    # Test case 3: All points at the same distance
    result = solution.kClosest([[1,1],[-1,1],[1,-1],[-1,-1]], 4)
    assert len(result) == 4

    # Test case 4: Points on the axes
    result = solution.kClosest([[0,1],[1,0],[0,-1],[-1,0]], 2)
    assert len(result) == 2
    for point in result:
        assert abs(point[0]) + abs(point[1]) == 1

    # Test case 5: Large k
    points = [[i, i] for i in range(10000)]
    result = solution.kClosest(points, 9999)
    assert len(result) == 9999
    assert [0,0] in result
    assert [9999,9999] not in result

    print("All test cases passed!")

test_kClosest()
```

## Overview of rejected approaches

1. Brute Force: Calculating the distance for all points and sorting them. This is similar to our sorting approach but less efficient because it doesn't leverage the fact that we can compare squared distances.

2. BFS/DFS on a grid: While these approaches are often used for shortest path problems, they're not suitable here because we're dealing with discrete points rather than a connected grid.

3. Dynamic Programming: This problem doesn't have overlapping subproblems or an optimal substructure, so DP is not applicable.

4. Binary Search on distance: While it might seem tempting to use binary search to find the distance that separates the k closest points, this approach would require multiple passes over the data and would be less efficient than our recommended solutions.

5. Using a balanced BST: While a self-balancing binary search tree could maintain the k closest points, it would be more complex to implement and less efficient than a heap for this specific problem.

## Visualization(s)

Here's a simple visualization of how the max heap approach works:

```tsx
import React, { useState } from "react";

const MaxHeapVisualization = () => {
  const [step, setStep] = useState(0);
  const [heap, setHeap] = useState([]);
  const k = 3;
  const points = [
    [1, 3],
    [-2, 2],
    [2, -1],
    [-1, 4],
    [0, 5],
  ];

  const addPoint = () => {
    if (step < points.length) {
      const [x, y] = points[step];
      const dist = -(x * x + y * y); // Negative for max heap
      const newHeap = [...heap, [dist, x, y]];
      newHeap.sort((a, b) => b[0] - a[0]); // Sort descending
      if (newHeap.length > k) {
        newHeap.pop();
      }
      setHeap(newHeap);
      setStep(step + 1);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Max Heap Visualization (k={k})</h2>
      <div className="mb-4">
        <button
          onClick={addPoint}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          disabled={step >= points.length}
        >
          Add Next Point
        </button>
      </div>
      <div className="mb-4">
        <h3 className="font-bold">Current Heap:</h3>
        <ul>
          {heap.map(([dist, x, y], index) => (
            <li key={index}>
              ({x}, {y}) - Distance: {Math.sqrt(-dist).toFixed(2)}
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h3 className="font-bold">Remaining Points:</h3>
        <ul>
          {points.slice(step).map(([x, y], index) => (
            <li key={index}>
              ({x}, {y})
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default MaxHeapVisualization;
```

This visualization demonstrates how the max heap approach maintains the k closest points as we process each point in the input. You can click the "Add Next Point" button to see how the heap evolves as new points are added.
