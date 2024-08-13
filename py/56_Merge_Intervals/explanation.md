# Explanation: Merge Intervals

## Analysis of problem & input data

This problem deals with merging overlapping intervals, which is a common task in various applications such as scheduling, time series analysis, and data processing. The key characteristics of this problem are:

1. Input is a list of intervals, where each interval is represented by a start and end point.
2. Intervals may overlap partially or completely.
3. The goal is to merge overlapping intervals and return a list of non-overlapping intervals.

The key principle that makes this question simple is the realization that if we sort the intervals by their start times, we can merge them in a single pass through the sorted list. This is because after sorting, any overlapping intervals will be adjacent to each other.

Important observations:

- The intervals are not necessarily given in any particular order.
- The start and end times are inclusive (e.g., [1,3] and [3,4] are considered overlapping).
- The problem doesn't specify how to handle empty intervals (like [2,2]), but we'll assume they're valid.

### Test cases

Here are some test cases to consider:

1. Basic case with overlapping intervals:
   Input: [[1,3],[2,6],[8,10],[15,18]]
   Expected Output: [[1,6],[8,10],[15,18]]

2. Case with complete overlap:
   Input: [[1,4],[2,3]]
   Expected Output: [[1,4]]

3. Case with no overlaps:
   Input: [[1,2],[3,4],[5,6]]
   Expected Output: [[1,2],[3,4],[5,6]]

4. Case with all intervals overlapping:
   Input: [[1,5],[2,6],[3,7],[4,8]]
   Expected Output: [[1,8]]

5. Case with adjacent intervals:
   Input: [[1,2],[2,3],[3,4],[4,5]]
   Expected Output: [[1,5]]

6. Case with a single interval:
   Input: [[1,2]]
   Expected Output: [[1,2]]

7. Case with negative numbers:
   Input: [[-2,3],[-1,2],[1,4]]
   Expected Output: [[-2,4]]

8. Edge case with maximum values:
   Input: [[0,10000],[5000,10000]]
   Expected Output: [[0,10000]]

Here's the Python code to run these test cases:

```python
def merge(intervals):
    # Implementation goes here
    pass

# Test cases
test_cases = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[2,3]], [[1,4]]),
    ([[1,2],[3,4],[5,6]], [[1,2],[3,4],[5,6]]),
    ([[1,5],[2,6],[3,7],[4,8]], [[1,8]]),
    ([[1,2],[2,3],[3,4],[4,5]], [[1,5]]),
    ([[1,2]], [[1,2]]),
    ([[-2,3],[-1,2],[1,4]], [[-2,4]]),
    ([[0,10000],[5000,10000]], [[0,10000]])
]

for i, (intervals, expected) in enumerate(test_cases, 1):
    result = merge(intervals)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Sort and Merge (Optimal)
2. Line Sweep Algorithm

Count: 2 solutions

#### Rejected solutions

1. Brute Force Comparison
2. Interval Tree
3. Segment Tree

### Worthy Solutions

#### 1. Sort and Merge (Optimal)

```python
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged is empty or current interval doesn't overlap with previous
        # append it directly
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Otherwise, there is overlap, so we merge the current and previous
            # intervals by updating the end time of the previous interval
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
```

Time Complexity: O(n log n), where n is the number of intervals. This is due to the sorting step.
Space Complexity: O(n) to store the sorted and merged intervals.

Intuition and invariants:

- Sorting the intervals by start time ensures that overlapping intervals are adjacent.
- The merged list always contains non-overlapping intervals.
- We only need to compare the current interval with the last interval in the merged list.
- The end time of an interval in the merged list is always the maximum end time of all merged intervals.

#### 2. Line Sweep Algorithm

```python
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    events = []
    for start, end in intervals:
        events.append((start, 1))  # 1 represents start of an interval
        events.append((end, -1))   # -1 represents end of an interval

    events.sort(key=lambda x: (x[0], -x[1]))  # Sort by time, prioritize starts over ends

    merged = []
    open_count = 0
    start = 0

    for time, event_type in events:
        if open_count == 0 and event_type == 1:
            start = time

        open_count += event_type

        if open_count == 0:
            merged.append([start, time])

    return merged
```

Time Complexity: O(n log n), where n is the number of intervals. This is due to the sorting step.
Space Complexity: O(n) to store the events and merged intervals.

Intuition and invariants:

- We treat each interval as two events: start and end.
- Sorting events allows us to process them in chronological order.
- We keep track of how many intervals are "open" at any given time.
- When open_count goes from 0 to 1, we start a new merged interval.
- When open_count goes back to 0, we close the current merged interval.

### Rejected Approaches

1. Brute Force Comparison:

   - Comparing each interval with every other interval.
   - Time complexity: O(n^2)
   - Reason for rejection: Inefficient for large inputs, doesn't leverage the inherent structure of the problem.

2. Interval Tree:

   - Building an interval tree and querying for overlaps.
   - Time complexity: O(n log n) for construction, O(log n + k) for each query where k is the number of overlapping intervals.
   - Reason for rejection: While efficient for querying overlaps, it's overkill for this problem and doesn't directly solve the merging aspect.

3. Segment Tree:
   - Building a segment tree to track overlapping intervals.
   - Time complexity: O(n log m) where m is the range of interval values.
   - Reason for rejection: Complex to implement, and the range of values can be large (up to 10^4), making it less efficient than simpler solutions.

### Final Recommendations

The Sort and Merge approach is the recommended solution for this problem. It's intuitive, efficient, and directly addresses the problem at hand. The Line Sweep algorithm is also worth understanding as it provides a different perspective on interval problems and can be more efficient in certain scenarios (e.g., when dealing with a large number of short intervals).

The Sort and Merge approach is particularly well-suited for coding interviews because:

1. It's straightforward to implement and explain.
2. It demonstrates understanding of sorting and linear traversal algorithms.
3. It has optimal time complexity for this problem.
4. It showcases the ability to think about edge cases and handle them efficiently.

While the Line Sweep algorithm is also efficient, it's slightly more complex to implement and explain in an interview setting. However, it's a valuable technique to know for more advanced interval-related problems.

The rejected approaches, while potentially applicable to related problems, are either too inefficient (Brute Force) or overly complex (Interval Tree, Segment Tree) for this specific problem. In an interview, using these approaches might suggest a lack of problem-solving efficiency or overcomplication of a straightforward task.

## Visualization(s)

To visualize the Sort and Merge approach, we can use a simple ASCII art representation:

```
Input intervals:  [1,3] [2,6] [8,10] [15,18]
                   |--|
                     |-----|
                               |--|
                                        |---|

After sorting:    [1,3] [2,6] [8,10] [15,18]
                   |--|
                     |-----|
                               |--|
                                        |---|

Merging process:
Step 1: [1,3]     |--|
Step 2: [1,6]     |------|  (merged [1,3] and [2,6])
Step 3: [1,6]     |------|
       [8,10]              |--|
Step 4: [1,6]     |------|
       [8,10]              |--|
       [15,18]                    |---|

Final result:     [1,6] [8,10] [15,18]
                   |------|
                           |--|
                                 |---|
```

This visualization helps to understand how the algorithm processes the intervals in order and merges overlapping ones.
