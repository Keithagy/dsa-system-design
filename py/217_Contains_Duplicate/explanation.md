## Explanation: Contains Duplicate

### Analysis of problem & input data

This problem is fundamentally about detecting repetition within a collection of integers. The key characteristics to note are:

1. We're dealing with an array of integers.
2. The size of the array can be quite large (up to 10^5 elements).
3. The integers can have a wide range of values (-10^9 to 10^9).
4. We only need to find if there's at least one duplicate; we don't need to identify all duplicates or count them.

The core principle that makes this question simple is the pigeonhole principle: if we have n+1 items to put into n boxes, at least one box must contain more than one item. In our case, if we've seen more numbers than unique values, we must have a duplicate.

This problem is a classic example where hash-based data structures shine. The large range of possible integer values and the need for quick lookups make hash sets an ideal choice. However, it's also a problem where sorting can be leveraged, trading off time complexity for space efficiency.

### Test cases

We should consider the following test cases:

1. Array with no duplicates: `[1, 2, 3, 4, 5]`
2. Array with one duplicate: `[1, 2, 3, 4, 2]`
3. Array with multiple duplicates: `[1, 2, 2, 3, 3, 4, 4]`
4. Array with all elements the same: `[1, 1, 1, 1]`
5. Array with only one element: `[1]`
6. Array with negative numbers: `[-1, -2, -3, -1]`
7. Array with the maximum allowed size and no duplicates
8. Array with the maximum allowed size and one duplicate at the end

Here's the Python code for these test cases:

```python
def contains_duplicate(nums: List[int]) -> bool:
    # Implementation will go here
    pass

# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], False),
    ([1, 2, 3, 4, 2], True),
    ([1, 2, 2, 3, 3, 4, 4], True),
    ([1, 1, 1, 1], True),
    ([1], False),
    ([-1, -2, -3, -1], True),
    (list(range(100000)), False),
    (list(range(99999)) + [0], True)
]

for i, (nums, expected) in enumerate(test_cases):
    result = contains_duplicate(nums)
    print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Hash Set Approach
2. Sorting Approach
3. Bit Manipulation Approach (for specific constraints)

Count: 3 solutions

##### Rejected solutions

1. Naive Nested Loop Approach
2. Counter-based Approach (similar to Hash Set but less efficient for this specific problem)

#### Worthy Solutions

##### Hash Set Approach

```python
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    seen = set()  # Hash set to store seen numbers
    for num in nums:
        if num in seen:
            return True  # Found a duplicate
        seen.add(num)  # Add the number to the set
    return False  # No duplicates found
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(n) in the worst case, where all elements are unique.

- Leverages the constant-time average case lookup and insertion of hash sets
- Maintains an invariant: at any point, `seen` contains all unique elements encountered so far
- Stops as soon as a duplicate is found, avoiding unnecessary iterations

##### Sorting Approach

```python
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False  # An array of length 0 or 1 cannot have duplicates

    nums.sort()  # Sort the array in-place
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True  # Found adjacent duplicate elements
    return False  # No duplicates found
```

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) or O(n), depending on the sorting algorithm used

- Utilizes the property that duplicates will be adjacent after sorting
- Trades time complexity for space efficiency compared to the hash set approach
- Useful when memory is constrained or when the input array can be modified

##### Bit Manipulation Approach (for specific constraints)

```python
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    seen = 0  # Bitset to represent seen numbers
    for num in nums:
        if num < 0 or num >= 64:  # Check if number is within valid range
            return True  # This approach only works for 0 <= num < 64
        mask = 1 << num
        if seen & mask:  # Check if the bit is already set
            return True
        seen |= mask  # Set the bit
    return False
```

Time Complexity: O(n)
Space Complexity: O(1)

- Uses a 64-bit integer as a bitset to represent seen numbers
- Extremely memory-efficient, but only works for a limited range of non-negative integers
- Demonstrates clever use of bitwise operations for specific problem constraints

#### Rejected Approaches

1. Naive Nested Loop Approach: Using two nested loops to compare each element with every other element. This has a time complexity of O(n^2) and is inefficient for large inputs.

2. Counter-based Approach: Using a Counter object from the collections module. While this would work, it's overkill for this problem as we don't need to count occurrences, just detect duplicates. The hash set approach is more direct and slightly more efficient.

#### Final Recommendations

The Hash Set Approach is generally the best solution to learn and use in interviews. It offers the best balance of time and space complexity for most scenarios. It's also straightforward to implement and explain, which is valuable in an interview setting.

The Sorting Approach is worth knowing as an alternative when in-place modification of the input is allowed and memory usage is a concern.

The Bit Manipulation Approach, while clever, is too specific to be generally applicable. However, it's an excellent example of how understanding the constraints of a problem can lead to highly optimized solutions.

### Visualization(s)

For the Hash Set Approach, we can visualize the process using a simple React component:

```tsx
import React, { useState } from "react";
import { Button } from "@/components/ui/button";

const HashSetVisualization = () => {
  const [nums, setNums] = useState([1, 2, 3, 1]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [seen, setSeen] = useState(new Set());
  const [isDuplicate, setIsDuplicate] = useState(false);

  const reset = () => {
    setCurrentIndex(0);
    setSeen(new Set());
    setIsDuplicate(false);
  };

  const step = () => {
    if (currentIndex < nums.length && !isDuplicate) {
      const num = nums[currentIndex];
      if (seen.has(num)) {
        setIsDuplicate(true);
      } else {
        setSeen(new Set([...seen, num]));
      }
      setCurrentIndex(currentIndex + 1);
    }
  };

  return (
    <div className="p-4 border rounded-lg">
      <h3 className="text-lg font-bold mb-2">
        Hash Set Approach Visualization
      </h3>
      <div className="mb-4">Input: [{nums.join(", ")}]</div>
      <div className="mb-4">
        Current number:{" "}
        {currentIndex < nums.length ? nums[currentIndex] : "Done"}
      </div>
      <div className="mb-4">Seen set: {[...seen].join(", ")}</div>
      <div className="mb-4">
        Result: {isDuplicate ? "Duplicate found!" : "No duplicate yet"}
      </div>
      <Button
        onClick={step}
        disabled={currentIndex >= nums.length || isDuplicate}
        className="mr-2"
      >
        Step
      </Button>
      <Button onClick={reset}>Reset</Button>
    </div>
  );
};

export default HashSetVisualization;
```

This visualization allows you to step through the algorithm, seeing how the hash set grows and how duplicates are detected. It's an interactive way to understand the process.
