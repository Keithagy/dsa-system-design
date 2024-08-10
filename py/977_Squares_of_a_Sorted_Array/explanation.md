# Explanation: Squares of a Sorted Array

## Analysis of problem & input data

This problem presents several key characteristics that guide us towards efficient solutions:

1. Input array is sorted in non-decreasing order
2. Array contains both negative and positive integers
3. We need to return squares of these numbers in non-decreasing order
4. The array length is between 1 and 10^4
5. The values are between -10^4 and 10^4

The crucial insight here is that while the input array is sorted, squaring the numbers doesn't preserve this order due to negative numbers. The largest squares will be at both ends of the array (largest negative numbers and largest positive numbers), while the smallest squares will be closest to zero.

This observation allows us to pattern-match this problem to the "two-pointer" technique, specifically the "two pointers from ends" pattern. We can compare absolute values from both ends of the array and build our result from largest to smallest.

The key principle that makes this question simple is that in a sorted array with negative and positive numbers, the largest squared values will always be at the ends of the array, moving inwards as we process the numbers.

## Solutions

### Solution 1: Two Pointers

```python
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n  # Initialize result array with zeros
    left, right = 0, n - 1  # Two pointers: left at start, right at end
    for i in range(n - 1, -1, -1):  # Fill result array from right to left
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result
```

Time Complexity: O(n), where n is the length of the input array
Space Complexity: O(n) for the result array (not counting the input)

Intuition and invariants:

- The largest squared value will always be at one of the ends of the input array
- We can compare absolute values to determine which end has the larger square
- By filling the result array from right to left, we ensure it's sorted in non-decreasing order

### Solution 2: Naive Approach (Square and Sort)

```python
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    return sorted(num ** 2 for num in nums)
```

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for the new list

While this solution is correct and straightforward, it doesn't take advantage of the fact that the input is already sorted. It's less efficient than the two-pointer approach.

## Recommendation

The two-pointer solution (Solution 1) is the best one to learn for this problem. It achieves the optimal time complexity of O(n) and demonstrates a deep understanding of the problem's characteristics. This solution showcases:

1. Efficient use of the input array's properties
2. In-place computation of squares
3. Building the result in sorted order without an additional sorting step

Learning this solution will help in recognizing similar patterns in other problems where working from the ends of a sorted array can yield optimal results.

## Test cases

```python
def test_sortedSquares():
    assert sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
    assert sortedSquares([0]) == [0]
    assert sortedSquares([-5,-3,-2,-1]) == [1,4,9,25]
    assert sortedSquares([1,2,3,4,5]) == [1,4,9,16,25]
    print("All test cases passed!")

test_sortedSquares()
```

## Overview of rejected approaches

1. In-place square and sort:

   ```python
   def sortedSquares(nums: List[int]) -> List[int]:
       for i in range(len(nums)):
           nums[i] = nums[i] ** 2
       nums.sort()
       return nums
   ```

   While this approach works and modifies the input array in-place, it still has a time complexity of O(n log n) due to the sorting step. It's correct but not optimal, and doesn't leverage the initial sorted property of the input.

2. Using a heap:

   ```python
   import heapq
   def sortedSquares(nums: List[int]) -> List[int]:
       return heapq.nsmallest(len(nums), (num ** 2 for num in nums))
   ```

   This approach uses a heap to find the n smallest elements after squaring. While it works, it has a time complexity of O(n log n) and doesn't take advantage of the input's sorted nature. It's overcomplicated for this specific problem.

3. Squaring and inserting into a new sorted list:

   ```python
   from bisect import insort
   def sortedSquares(nums: List[int]) -> List[int]:
       result = []
       for num in nums:
           insort(result, num ** 2)
       return result
   ```

   This approach maintains a sorted list as it processes each number. While it produces a correct result, it has a time complexity of O(n^2) due to the repeated insertions into a sorted list. It's inefficient and doesn't leverage the input's properties effectively.

## Visualization(s)

To visualize the two-pointer approach, let's create a simple React component that demonstrates how the pointers move and how the result array is filled:

```tsx
import React, { useState, useEffect } from "react";

const SortedSquaresVisualization = () => {
  const [nums, setNums] = useState([-4, -1, 0, 3, 10]);
  const [result, setResult] = useState(new Array(nums.length).fill(0));
  const [left, setLeft] = useState(0);
  const [right, setRight] = useState(nums.length - 1);
  const [current, setCurrent] = useState(nums.length - 1);
  const [step, setStep] = useState(0);

  useEffect(() => {
    if (step > 0 && current >= 0) {
      const timer = setTimeout(() => {
        if (Math.abs(nums[left]) > Math.abs(nums[right])) {
          const newResult = [...result];
          newResult[current] = nums[left] ** 2;
          setResult(newResult);
          setLeft(left + 1);
        } else {
          const newResult = [...result];
          newResult[current] = nums[right] ** 2;
          setResult(newResult);
          setRight(right - 1);
        }
        setCurrent(current - 1);
        setStep(step + 1);
      }, 1000);
      return () => clearTimeout(timer);
    }
  }, [step, current, left, right, nums, result]);

  const startVisualization = () => {
    setNums([-4, -1, 0, 3, 10]);
    setResult(new Array(5).fill(0));
    setLeft(0);
    setRight(4);
    setCurrent(4);
    setStep(1);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">
        Squares of a Sorted Array Visualization
      </h2>
      <div className="mb-4">
        <button
          onClick={startVisualization}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Start Visualization
        </button>
      </div>
      <div className="flex mb-4">
        {nums.map((num, index) => (
          <div
            key={index}
            className={`w-12 h-12 border border-gray-300 flex items-center justify-center mr-2 ${
              index === left
                ? "bg-green-200"
                : index === right
                  ? "bg-red-200"
                  : ""
            }`}
          >
            {num}
          </div>
        ))}
      </div>
      <div className="flex">
        {result.map((num, index) => (
          <div
            key={index}
            className={`w-12 h-12 border border-gray-300 flex items-center justify-center mr-2 ${
              index === current ? "bg-yellow-200" : ""
            }`}
          >
            {num}
          </div>
        ))}
      </div>
    </div>
  );
};

export default SortedSquaresVisualization;
```

This visualization demonstrates how the two-pointer approach works step by step. The top row represents the input array, with green highlighting the left pointer and red highlighting the right pointer. The bottom row shows the result array being filled from right to left, with yellow highlighting the current position being filled.

To use this visualization:

1. The initial state shows the input array [-4, -1, 0, 3, 10] and an empty result array.
2. Click the "Start Visualization" button to begin the process.
3. Watch as the pointers move and the result array is filled one element at a time.
4. The visualization will automatically step through the entire process, updating every second.

This visual representation helps to understand how the algorithm compares values from both ends of the input array and builds the result array in sorted order without an additional sorting step.
