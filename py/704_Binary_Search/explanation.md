## Explanation: Binary Search

### Analysis of problem & input data

This problem is a classic implementation of the binary search algorithm. The key characteristics that make binary search applicable here are:

1. The input array `nums` is sorted in ascending order.
2. We're searching for a specific `target` value.
3. The problem requires an O(log n) runtime complexity.

The sorted nature of the array is crucial because it allows us to eliminate half of the remaining search space in each iteration. This is the fundamental principle that makes binary search efficient and achieves the required O(log n) complexity.

The key principle that makes this question simple is the divide-and-conquer strategy. By comparing the middle element with the target, we can determine which half of the array to continue searching in, effectively halving our search space with each comparison.

### Test cases

Here are some important test cases to consider:

1. Normal case: Target exists in the middle of the array
2. Edge cases:
   - Target is the first element
   - Target is the last element
3. Target doesn't exist:
   - Target is smaller than all elements
   - Target is larger than all elements
   - Target is between existing elements
4. Array with a single element:
   - Target matches the single element
   - Target doesn't match the single element
5. Empty array (though not allowed by the constraints, it's good to consider)

Here's the Python code for these test cases:

```python
def test_binary_search(search_function):
    assert search_function([-1,0,3,5,9,12], 9) == 4, "Normal case failed"
    assert search_function([-1,0,3,5,9,12], -1) == 0, "First element failed"
    assert search_function([-1,0,3,5,9,12], 12) == 5, "Last element failed"
    assert search_function([-1,0,3,5,9,12], -2) == -1, "Smaller than all failed"
    assert search_function([-1,0,3,5,9,12], 15) == -1, "Larger than all failed"
    assert search_function([-1,0,3,5,9,12], 2) == -1, "Between elements failed"
    assert search_function([5], 5) == 0, "Single element (match) failed"
    assert search_function([5], 3) == -1, "Single element (no match) failed"
    print("All test cases passed!")

# The binary_search function will be implemented later
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Iterative Binary Search (most worth learning)
2. Recursive Binary Search
3. Binary Search with Python's `bisect` module (least worth learning for interviews, but good to know)

Count: 3 solutions

##### Rejected solutions

1. Linear Search: O(n) complexity, doesn't meet the O(log n) requirement
2. Hash Table: While O(1) lookup, it requires O(n) preprocessing and O(n) space

#### Worthy Solutions

1. Iterative Binary Search

```python
from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid potential integer overflow

        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found
```

- Time Complexity: O(log n), where n is the length of the input array
- Space Complexity: O(1), as we only use a constant amount of extra space

Key intuitions and invariants:

- The search space is continuously halved in each iteration
- The `left` and `right` pointers always maintain the current search range
- The loop continues as long as there's a valid search range (`left <= right`)
- The middle element is calculated using `left + (right - left) // 2` to avoid potential integer overflow

2. Recursive Binary Search

```python
from typing import List

def search(nums: List[int], target: int) -> int:
    def binary_search_recursive(left: int, right: int) -> int:
        if left > right:
            return -1  # Base case: target not found

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            return binary_search_recursive(mid + 1, right)  # Search right half
        else:
            return binary_search_recursive(left, mid - 1)  # Search left half

    return binary_search_recursive(0, len(nums) - 1)
```

- Time Complexity: O(log n), where n is the length of the input array
- Space Complexity: O(log n) due to the recursive call stack

Key intuitions and invariants:

- The recursive approach maintains the same invariants as the iterative version
- Each recursive call reduces the search space by half
- The base case handles when the target is not found (`left > right`)
- The recursive nature makes the divide-and-conquer strategy more explicit

3. Binary Search with Python's `bisect` module

```python
from typing import List
import bisect

def search(nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)
    return index if index < len(nums) and nums[index] == target else -1
```

- Time Complexity: O(log n), where n is the length of the input array
- Space Complexity: O(1)

Key intuitions and invariants:

- `bisect.bisect_left` finds the insertion point for `target` in the sorted array
- If the target exists, its index will be returned
- We need to check if the found index is valid and if the element at that index matches the target

#### Rejected Approaches

1. Linear Search: While correct, it has O(n) time complexity, which doesn't meet the problem's requirement of O(log n).

2. Hash Table: Although it provides O(1) lookup time, it requires O(n) preprocessing to build the hash table and O(n) extra space. Moreover, it doesn't leverage the sorted nature of the input array.

#### Final Recommendations

The iterative binary search is the best solution to learn and use in interviews. It's efficient, easy to implement, and doesn't have the space overhead of the recursive approach. The iterative approach is also generally preferred in real-world scenarios due to its constant space complexity.

### Visualization(s)

For a visual representation of how binary search works, we can use a simple ASCII art diagram:

```
Initial array: [-1, 0, 3, 5, 9, 12]
Target: 9

Iteration 1:
[-1, 0, 3, 5, 9, 12]
          ^
        mid=5 (value=9)
Target found!

If target was 3:
Iteration 1:
[-1, 0, 3, 5, 9, 12]
          ^
        mid=5 (value=9)
9 > 3, so search left half

Iteration 2:
[-1, 0, 3, 5]
      ^
    mid=3 (value=3)
Target found!
```

This visualization helps to illustrate how the algorithm narrows down the search space in each iteration by comparing the middle element with the target value.

```tsx
import React, { useState } from "react";
import { Button, Input, Alert } from "@/components/ui";

const BinarySearchVisualization = () => {
  const [numbers, setNumbers] = useState([-1, 0, 3, 5, 9, 12]);
  const [target, setTarget] = useState(9);
  const [currentStep, setCurrentStep] = useState(0);
  const [left, setLeft] = useState(0);
  const [right, setRight] = useState(numbers.length - 1);
  const [mid, setMid] = useState(Math.floor((left + right) / 2));
  const [found, setFound] = useState(false);

  const reset = () => {
    setCurrentStep(0);
    setLeft(0);
    setRight(numbers.length - 1);
    setMid(Math.floor((left + right) / 2));
    setFound(false);
  };

  const nextStep = () => {
    if (found || left > right) return;

    setCurrentStep(currentStep + 1);
    if (numbers[mid] === target) {
      setFound(true);
    } else if (numbers[mid] < target) {
      setLeft(mid + 1);
    } else {
      setRight(mid - 1);
    }
    setMid(Math.floor((left + right) / 2));
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4">Binary Search Visualization</h2>
      <div className="mb-4">
        <Input
          type="text"
          value={numbers.join(", ")}
          onChange={(e) => setNumbers(e.target.value.split(",").map(Number))}
          placeholder="Enter comma-separated numbers"
          className="mb-2"
        />
        <Input
          type="number"
          value={target}
          onChange={(e) => setTarget(Number(e.target.value))}
          placeholder="Enter target number"
        />
      </div>
      <div className="flex space-x-2 mb-4">
        <Button onClick={reset}>Reset</Button>
        <Button onClick={nextStep}>Next Step</Button>
      </div>
      <div className="mb-4">
        <p>Step: {currentStep}</p>
        <p>
          Left: {left}, Right: {right}, Mid: {mid}
        </p>
      </div>
      <div className="flex flex-wrap gap-2 mb-4">
        {numbers.map((num, index) => (
          <div
            key={index}
            className={`w-10 h-10 flex items-center justify-center border ${
              index === mid
                ? "bg-yellow-200"
                : index >= left && index <= right
                  ? "bg-blue-100"
                  : "bg-gray-100"
            }`}
          >
            {num}
          </div>
        ))}
      </div>
      {found && (
        <Alert variant="success">
          Target {target} found at index {mid}!
        </Alert>
      )}
      {!found && left > right && (
        <Alert variant="error">Target {target} not found in the array.</Alert>
      )}
    </div>
  );
};

export default BinarySearchVisualization;
```

This interactive visualization allows users to input their own array of numbers and target value, then step through the binary search algorithm to see how it narrows down the search space in each iteration. The current search range is highlighted in blue, with the middle element in yellow. This visual representation helps reinforce the concepts of how binary search efficiently finds the target or determines its absence in the array.
