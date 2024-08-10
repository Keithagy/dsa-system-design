# Explanation: Insert Interval

## Analysis of problem & input data

This problem involves merging and inserting intervals, which is a common pattern in interval-based problems. The key characteristics and constraints of this problem are:

1. The input `intervals` is already sorted in ascending order by start time.
2. The intervals in the input are non-overlapping.
3. We need to insert a new interval `newInterval` and merge if necessary.
4. The output should maintain the sorted and non-overlapping properties.
5. We don't need to modify the input in-place; we can return a new array.

The key principle that makes this question manageable is the fact that the input intervals are already sorted. This allows us to process the intervals in order, making decisions about merging or inserting based on the relationship between the current interval and the new interval.

The problem can be broken down into three main parts:

1. Intervals that come before the new interval (no overlap)
2. Intervals that overlap with the new interval (need to be merged)
3. Intervals that come after the new interval (no overlap)

## Solutions

Solution approaches include:

1. Linear scan and merge (most optimal and worth learning)
2. Binary search and merge (less optimal due to additional merging step)
3. Brute force insertion and sort (least optimal and not worth implementing)

### Linear Scan and Merge

This approach involves a single pass through the intervals, merging the new interval where necessary.

```python
from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the merged interval
    result.append(newInterval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

Time Complexity: O(n), where n is the number of intervals
Space Complexity: O(n) for the result array

Intuition and invariants:

- We process intervals in order, leveraging the sorted nature of the input.
- We maintain the invariant that all intervals processed so far are non-overlapping and in the correct order.
- The merging step ensures that overlapping intervals are combined correctly.

### Binary Search and Merge

This approach uses binary search to find the insertion point, then merges overlapping intervals.

```python
from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    def binary_search(intervals, target):
        left, right = 0, len(intervals)
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid
        return left

    # Find insertion point
    index = binary_search(intervals, newInterval[0])

    # Insert the new interval
    intervals.insert(index, newInterval)

    # Merge overlapping intervals
    result = []
    for interval in intervals:
        if not result or interval[0] > result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result
```

Time Complexity: O(n), despite using binary search, we still need to potentially shift all elements
Space Complexity: O(n) for the result array

Intuition and invariants:

- Binary search efficiently finds the insertion point.
- The merging step is similar to the linear scan approach, ensuring non-overlapping intervals.

## Recommendation

The linear scan and merge approach is recommended for learning and implementation. It's more intuitive, has the same time complexity as the binary search approach, and doesn't require the additional merging step. It also more directly leverages the sorted nature of the input, making it a cleaner and more elegant solution.

## Test cases

```python
def test_insert():
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([], [5,7]) == [[5,7]]
    assert insert([[1,5]], [2,3]) == [[1,5]]
    assert insert([[1,5]], [6,8]) == [[1,5],[6,8]]
    print("All test cases passed!")

test_insert()
```

## Overview of rejected approaches

1. Brute force insertion and sort: This approach would insert the new interval into the list and then sort the entire list. While correct, it's not optimal as it doesn't leverage the already sorted nature of the input. Time complexity would be O(n log n) due to sorting.

2. Two-pointer approach: While two pointers are often useful for interval problems, in this case, a single pointer (as used in the linear scan) is sufficient and more straightforward.

3. Heap-based approach: Using a heap might seem tempting for interval problems, but it's unnecessary here given the sorted input and would add unnecessary complexity.

4. Segment Tree or Interval Tree: These data structures are powerful for range queries and updates but are overkill for this problem. They would introduce unnecessary complexity and overhead.

## Visualization(s)

To visualize the linear scan and merge approach, we can use a simple diagram:

```svg
<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
  <style>
    text { font-family: Arial, sans-serif; font-size: 12px; }
    .small { font-size: 10px; }
  </style>

  <!-- Timeline -->
  <line x1="50" y1="100" x2="450" y2="100" stroke="black" />
  <text x="20" y="105" text-anchor="end">Time</text>

  <!-- Existing intervals -->
  <rect x="100" y="80" width="50" height="20" fill="lightblue" stroke="blue" />
  <text x="125" y="75" text-anchor="middle">[1,3]</text>

  <rect x="300" y="80" width="75" height="20" fill="lightblue" stroke="blue" />
  <text x="337.5" y="75" text-anchor="middle">[6,9]</text>

  <!-- New interval -->
  <rect x="150" y="120" width="100" height="20" fill="lightgreen" stroke="green" />
  <text x="200" y="155" text-anchor="middle">[2,5] (New)</text>

  <!-- Merged result -->
  <rect x="100" y="30" width="150" height="20" fill="lightyellow" stroke="orange" />
  <text x="175" y="25" text-anchor="middle">[1,5] (Merged)</text>

  <rect x="300" y="30" width="75" height="20" fill="lightyellow" stroke="orange" />
  <text x="337.5" y="25" text-anchor="middle">[6,9]</text>

  <!-- Labels -->
  <text x="250" y="190" text-anchor="middle" class="small">The new interval [2,5] overlaps with [1,3], resulting in a merged interval [1,5]</text>
</svg>

```

This visualization shows how the new interval [2,5] is merged with the existing interval [1,3] to form [1,5], while [6,9] remains unchanged. The timeline helps to illustrate the interval positions and overlaps.
