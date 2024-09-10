## Explanation: Meeting Rooms II

### Analysis of problem & input data

This problem is fundamentally about tracking overlapping intervals and determining the maximum number of simultaneous overlaps. The key characteristics of the input data that guide our solution strategy are:

1. The intervals represent meeting times with start and end points.
2. We need to find the maximum number of meetings happening at any given time.
3. The order of the intervals in the input is not guaranteed to be sorted.

The core principle that makes this question approachable is realizing that we only need to keep track of the count of active meetings at each critical point (start or end of a meeting). The maximum count at any point will give us the minimum number of conference rooms required.

This problem falls into the category of interval problems and can be solved efficiently using a line sweep algorithm or a priority queue approach. Both methods leverage the fact that we can separate the start and end times and process them in order.

### Test cases

Here are some relevant test cases to consider:

1. Basic case with overlapping meetings:

   ```python
   intervals = [[0,30],[5,10],[15,20]]
   # Expected output: 2
   ```

2. Non-overlapping meetings:

   ```python
   intervals = [[7,10],[2,4]]
   # Expected output: 1
   ```

3. Multiple overlapping meetings:

   ```python
   intervals = [[1,4],[2,5],[3,6],[4,7]]
   # Expected output: 4
   ```

4. Meetings with same start time:

   ```python
   intervals = [[0,5],[0,10],[0,15]]
   # Expected output: 3
   ```

5. Meetings with same end time:

   ```python
   intervals = [[1,10],[2,10],[3,10],[4,10]]
   # Expected output: 4
   ```

6. Single meeting:

   ```python
   intervals = [[1,2]]
   # Expected output: 1
   ```

7. Edge case with maximum constraints:

   ```python
   intervals = [[i, i+1] for i in range(10000)]
   # Expected output: 1
   ```

Here's the executable Python code for these test cases:

```python
def min_meeting_rooms(intervals):
    # Implementation will go here
    pass

test_cases = [
    ([[0,30],[5,10],[15,20]], 2),
    ([[7,10],[2,4]], 1),
    ([[1,4],[2,5],[3,6],[4,7]], 4),
    ([[0,5],[0,10],[0,15]], 3),
    ([[1,10],[2,10],[3,10],[4,10]], 4),
    ([[1,2]], 1),
    ([[i, i+1] for i in range(10000)], 1)
]

for i, (intervals, expected) in enumerate(test_cases):
    result = min_meeting_rooms(intervals)
    print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Chronological Ordering (Line Sweep) - Neetcode solution
2. Priority Queue (Min-Heap) - Neetcode solution
3. Balanced Binary Search Tree

Count: 3 solutions (2 Neetcode solutions)

##### Rejected solutions

1. Brute Force: Checking every time slot for all meetings
2. Graph-based approach: Creating a graph of overlapping intervals

#### Worthy Solutions

##### Chronological Ordering (Line Sweep)

```python
from typing import List

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    rooms_needed = 0
    max_rooms = 0
    start_ptr = 0
    end_ptr = 0

    while start_ptr < len(intervals):
        if start_times[start_ptr] < end_times[end_ptr]:
            rooms_needed += 1
            start_ptr += 1
        else:
            rooms_needed -= 1
            end_ptr += 1

        max_rooms = max(max_rooms, rooms_needed)

    return max_rooms
```

Time Complexity: O(n log n)

- Sorting both start and end times takes O(n log n) time, where n is the number of intervals.
- The while loop iterates through all start and end times once, which is O(n).
- Overall, the sorting dominates, so the time complexity is O(n log n).

Space Complexity: O(n)

- We create two new arrays of length n to store the sorted start and end times.
- The space used for sorting (usually O(log n) for in-place sorts like quicksort) is dominated by these arrays.

Intuitions and invariants:

- By separating start and end times, we can process events chronologically.
- A start time increases the room count, an end time decreases it.
- The maximum room count at any point gives the minimum number of rooms needed.
- We only need to compare the current start and end times to decide which event to process next.

##### Priority Queue (Min-Heap)

```python
import heapq
from typing import List

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Min heap to store end times of ongoing meetings
    heap = []

    for start, end in intervals:
        # If the earliest ending meeting ends before or at the start of the current meeting
        if heap and heap[0] <= start:
            # Remove the earliest ending meeting
            heapq.heappop(heap)

        # Add the end time of the current meeting
        heapq.heappush(heap, end)

    # The size of the heap is the number of rooms needed
    return len(heap)
```

Time Complexity: O(n log n)

- Sorting the intervals takes O(n log n) time.
- For each of the n intervals, we perform at most one heappush and one heappop operation, each taking O(log n) time.
- Therefore, the overall time complexity is O(n log n).

Space Complexity: O(n)

- In the worst case, all meetings might be ongoing simultaneously, requiring a heap of size n.
- The space used for sorting (usually O(log n) for in-place sorts) is dominated by the heap size.

Intuitions and invariants:

- The heap maintains the end times of ongoing meetings.
- If a meeting ends before or at the start of a new meeting, we can reuse that room.
- The size of the heap at any point represents the number of rooms currently in use.
- The maximum size of the heap during the process gives the minimum number of rooms needed.

##### Balanced Binary Search Tree

```python
from sortedcontainers import SortedList
from typing import List

def min_meeting_rooms(intervals: List[List[int]]) -> int:
    events = SortedList()
    for start, end in intervals:
        events.add((start, 1))  # 1 indicates start of a meeting
        events.add((end, -1))   # -1 indicates end of a meeting

    rooms = 0
    max_rooms = 0
    for _, event_type in events:
        rooms += event_type
        max_rooms = max(max_rooms, rooms)

    return max_rooms
```

Time Complexity: O(n log n)

- Adding each event to the SortedList takes O(log n) time, and we do this 2n times (for starts and ends).
- Iterating through the sorted events takes O(n) time.
- Overall, the time complexity is O(n log n).

Space Complexity: O(n)

- We store 2n events in the SortedList.

Intuitions and invariants:

- We treat starts and ends as separate events, sorted by their time.
- A start event increases the room count, an end event decreases it.
- By processing events in order, we maintain an accurate count of rooms in use at each point.
- The maximum room count encountered is the minimum number of rooms needed.

#### Rejected Approaches

1. Brute Force: Checking every time slot for all meetings

   - This approach would involve iterating through each possible time slot and counting the number of meetings active at that time.
   - Rejected because: Time complexity would be O(m \* n), where m is the range of possible times and n is the number of meetings. This is inefficient for large time ranges or many meetings.

2. Graph-based approach: Creating a graph of overlapping intervals
   - This approach would involve creating a graph where nodes are meetings and edges represent overlaps.
   - Rejected because: While this could work, it's overly complicated for this problem. The time and space complexity would be at least O(n^2) to check all pairs of intervals for overlap, which is less efficient than our accepted solutions.

#### Final Recommendations

The Chronological Ordering (Line Sweep) approach is recommended as the best solution to learn for this problem. Here's why:

1. It's intuitive and easy to understand conceptually.
2. It has optimal time complexity O(n log n) and space complexity O(n).
3. It doesn't require any complex data structures beyond sorting.
4. It's versatile and can be adapted to solve other interval-related problems.

The Priority Queue solution is also excellent and worth learning, especially if you're comfortable with heap operations. It's particularly useful when you need to dynamically add and remove intervals.

The Balanced Binary Search Tree approach, while valid, is less common in interviews and requires an additional library. It's good to understand conceptually but may not be the first choice in an interview setting.

### Visualization(s)

For the Chronological Ordering approach, we can visualize the process like this:

```
Time:  0  1  2  3  4  5  6  7  8  9 10
       |  |  |  |  |  |  |  |  |  |  |
       S--------------------------E
          S-----E
                   S-----E

Rooms: 1  2  2  2  2  1  1  1  1  1  0

S: Start of a meeting
E: End of a meeting
```

This visualization shows how the number of rooms changes over time as meetings start and end. The maximum number of rooms used at any point (2 in this case) is our answer.
