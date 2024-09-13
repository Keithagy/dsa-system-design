## Explanation: Non-overlapping Intervals

### Analysis of problem & input data

This problem falls into the category of interval scheduling and greedy algorithms. The key characteristics of the problem are:

1. We're dealing with intervals, each represented by a start and end time.
2. The goal is to find the minimum number of intervals to remove to make the rest non-overlapping.
3. The intervals are not necessarily sorted in the input.

The key principle that makes this question simple is the greedy choice property. We can make locally optimal choices at each step to arrive at a globally optimal solution. In this case, the optimal strategy is to always keep the interval that ends earliest among overlapping intervals.

This problem is similar to the activity selection problem, where we want to schedule the maximum number of activities. Here, we're approaching it from the opposite direction - finding the minimum number to remove.

The pattern-matching here leads us to consider sorting the intervals based on their end times. This allows us to process intervals in a way that maximizes our chances of fitting in more non-overlapping intervals.

### Test cases

1. Standard case: `[[1,2],[2,3],[3,4],[1,3]]` (Output: 1)
2. All overlapping: `[[1,2],[1,2],[1,2]]` (Output: 2)
3. No overlapping: `[[1,2],[2,3]]` (Output: 0)
4. Single interval: `[[1,2]]` (Output: 0)
5. Completely overlapping intervals: `[[1,4],[2,3],[3,4]]` (Output: 2)
6. Intervals with same end time: `[[1,2],[1,2],[1,3],[3,4]]` (Output: 2)
7. Large range of values: `[[-5*10^4,5*10^4],[-4*10^4,4*10^4],[-3*10^4,3*10^4]]` (Output: 2)

Here's the Python code for these test cases:

```python
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    # Implementation will go here
    pass

# Test cases
test_cases = [
    [[1,2],[2,3],[3,4],[1,3]],
    [[1,2],[1,2],[1,2]],
    [[1,2],[2,3]],
    [[1,2]],
    [[1,4],[2,3],[3,4]],
    [[1,2],[1,2],[1,3],[3,4]],
    [[-50000,50000],[-40000,40000],[-30000,30000]]
]

for i, case in enumerate(test_cases, 1):
    print(f"Test case {i}: Input = {case}")
    print(f"Output: {eraseOverlapIntervals(case)}\n")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Greedy approach with sorting by end time (Neetcode solution)
2. Dynamic Programming approach
3. Greedy approach with sorting by start time

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute force approach (trying all combinations)
2. Graph-based approach (creating a graph of overlapping intervals)

#### Worthy Solutions

##### Greedy approach with sorting by end time

```python
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    # Sort intervals based on end time
    intervals.sort(key=lambda x: x[1])

    non_overlapping = 1  # Count of non-overlapping intervals
    end = intervals[0][1]  # End time of the first interval

    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            # Current interval doesn't overlap with the previous one
            non_overlapping += 1
            end = intervals[i][1]

    return len(intervals) - non_overlapping
```

Time Complexity: O(n log n), where n is the number of intervals. This is due to the sorting step, which dominates the time complexity. The subsequent linear scan through the sorted intervals takes O(n) time.

Space Complexity: O(1) if we're allowed to modify the input array, or O(n) if we need to create a copy for sorting.

Intuition and invariants:

- Sorting by end time ensures we always consider the interval that ends earliest, maximizing the chance of accommodating more intervals.
- The `end` variable maintains the end time of the last non-overlapping interval we've kept.
- The `non_overlapping` count keeps track of how many intervals we're keeping.
- By subtracting `non_overlapping` from the total number of intervals, we get the minimum number of intervals to remove.

This greedy approach works because:

1. It always keeps the interval that ends earliest among overlapping intervals.
2. This maximizes the remaining time for future intervals, leading to an optimal solution.

##### Dynamic Programming approach

```python
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    # Sort intervals based on end time
    intervals.sort(key=lambda x: x[1])

    n = len(intervals)
    dp = [1] * n  # dp[i] represents the maximum number of non-overlapping intervals up to i

    for i in range(1, n):
        for j in range(i):
            if intervals[j][1] <= intervals[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)
```

Time Complexity: O(n^2), where n is the number of intervals. We have two nested loops iterating through the intervals.

Space Complexity: O(n) for the dp array.

Intuition and invariants:

- `dp[i]` represents the maximum number of non-overlapping intervals we can have ending at or before the i-th interval.
- We build this up by considering all previous intervals that don't overlap with the current one.
- The final answer is the total number of intervals minus the maximum value in dp.

This DP approach works because:

1. It considers all possible combinations of non-overlapping intervals.
2. It builds the solution incrementally, using solutions to smaller subproblems.
3. The sorting step ensures we only need to look at previous intervals for potential non-overlapping candidates.

##### Greedy approach with sorting by start time

```python
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    count = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:
            # No overlap, update prev_end
            prev_end = end
        else:
            # Overlap, increment count and keep the interval that ends earlier
            count += 1
            prev_end = min(prev_end, end)

    return count
```

Time Complexity: O(n log n), where n is the number of intervals. This is due to the sorting step, which dominates the time complexity. The subsequent linear scan through the sorted intervals takes O(n) time.

Space Complexity: O(1) if we're allowed to modify the input array, or O(n) if we need to create a copy for sorting.

Intuition and invariants:

- Sorting by start time allows us to process intervals in chronological order.
- `prev_end` keeps track of the end time of the last interval we've decided to keep.
- When we encounter an overlap, we always choose to keep the interval that ends earlier, as this leaves more room for future intervals.

This approach works because:

1. By processing intervals in order of start time, we ensure we're always making a decision based on the earliest possible conflict.
2. When there's an overlap, keeping the interval with the earlier end time is optimal as it leaves more room for future intervals.

#### Rejected Approaches

1. Brute Force Approach: Trying all possible combinations of intervals to remove. This would have a time complexity of O(2^n), which is impractical for large inputs.

2. Graph-based Approach: Creating a graph where intervals are nodes and edges represent overlaps, then finding the minimum vertex cover. While theoretically correct, this is overly complex for this problem and less efficient than the greedy approach.

3. Sorting by interval length: While this might seem intuitive (remove shorter intervals first), it doesn't guarantee an optimal solution. Consider `[[1,100], [2,3], [3,4]]` - removing [2,3] and [3,4] is optimal, but they're the shortest intervals.

#### Final Recommendations

The greedy approach with sorting by end time (the Neetcode solution) is the best to learn for this problem. It's intuitive, efficient (O(n log n) time complexity), and easy to implement. It also demonstrates a key principle in interval scheduling problems: when faced with overlapping intervals, it's often optimal to keep the one that ends earliest.

The DP approach, while correct, is less efficient (O(n^2)) and more complex to implement. It's worth understanding conceptually, but the greedy approach is superior for interviews.

The greedy approach with sorting by start time is also valid and efficient, but slightly more complex in its logic. It's a good alternative to know, but the end-time sorting approach is generally more intuitive for interval problems.

### Visualization(s)

To visualize this algorithm, we can create a simple React component that shows the intervals on a timeline and demonstrates how the greedy algorithm makes its choices.

```tsx
import React from "react";

const IntervalVisualization = () => {
  const intervals = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
  ];
  const maxEnd = Math.max(...intervals.map((interval) => interval[1]));

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Interval Visualization</h2>
      <div className="relative h-64 border-b border-gray-300">
        {intervals.map((interval, index) => (
          <div
            key={index}
            className="absolute h-8 bg-blue-200 border border-blue-500 rounded"
            style={{
              left: `${(interval[0] / maxEnd) * 100}%`,
              width: `${((interval[1] - interval[0]) / maxEnd) * 100}%`,
              top: `${index * 40}px`,
            }}
          >
            <span className="text-xs">{`[${interval[0]},${interval[1]}]`}</span>
          </div>
        ))}
      </div>
      <div className="mt-4">
        <p>
          The greedy algorithm would remove the interval [1,3] (the bottom one).
        </p>
        <p>This leaves the non-overlapping intervals: [1,2], [2,3], [3,4]</p>
      </div>
    </div>
  );
};

export default IntervalVisualization;
```

This visualization helps to understand how the intervals are laid out and why removing [1,3] is the optimal choice in this case.
