# Explanation: Maximum Subarray

## Analysis of problem & input data

This problem is a classic example of the "Maximum Subarray Problem," which asks us to find a contiguous subarray with the largest sum within a given array of integers. Let's break down the key aspects of this problem:

1. Input characteristics:

   - The input is an integer array `nums`.
   - The array length is between 1 and 10^5, inclusive.
   - Each element in the array is between -10^4 and 10^4, inclusive.
   - The array can contain both positive and negative integers.

2. Problem characteristics:

   - We need to find a contiguous subarray (non-empty sequence of elements).
   - The goal is to maximize the sum of elements in the subarray.
   - The subarray can be the entire array, a single element, or any contiguous portion.
   - We only need to return the sum, not the actual subarray.

3. Key principle:
   The fundamental insight that makes this problem solvable in O(n) time is the following: At any given position, we only need to know whether it's more beneficial to start a new subarray at that position or to extend the existing subarray. This principle allows us to make a local decision at each step that contributes to the global optimal solution.

4. Pattern matching:

   - This problem can be solved using dynamic programming or a greedy approach (Kadane's algorithm).
   - It's also a good candidate for the divide-and-conquer method, as mentioned in the follow-up.

5. Edge cases to consider:
   - An array with all negative numbers
   - An array with a single element
   - An array with alternating positive and negative numbers

Understanding these aspects helps us recognize that we can solve this problem efficiently by iterating through the array once, making local decisions that lead to the global optimum.

## Solutions

### Solution 1: Kadane's Algorithm (Dynamic Programming)

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current_sum and max_sum with the first element
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Decide whether to start a new subarray or extend the existing one
            current_sum = max(num, current_sum + num)

            # Update the maximum sum if necessary
            max_sum = max(max_sum, current_sum)

        return max_sum
```

This solution uses Kadane's algorithm, which is a form of dynamic programming. Here's the intuition behind the algorithm:

- We iterate through the array, maintaining two variables:

  1. `current_sum`: The maximum sum ending at the current position.
  2. `max_sum`: The overall maximum sum found so far.

- At each step, we make a decision:

  - If `current_sum + num` is greater than `num` itself, we extend the current subarray.
  - Otherwise, we start a new subarray beginning at the current number.

- We update `max_sum` if the `current_sum` is greater than the previous `max_sum`.

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we only use a constant amount of extra space.

### Solution 2: Divide and Conquer

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # Find the maximum subarray sum in the left and right halves
            left_sum = divide_and_conquer(left, mid)
            right_sum = divide_and_conquer(mid + 1, right)

            # Find the maximum subarray sum that crosses the midpoint
            left_border_sum = right_border_sum = 0
            current_sum = 0

            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_border_sum = max(left_border_sum, current_sum)

            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_border_sum = max(right_border_sum, current_sum)

            cross_sum = left_border_sum + right_border_sum

            # Return the maximum of the three sums
            return max(left_sum, right_sum, cross_sum)

        return divide_and_conquer(0, len(nums) - 1)
```

This solution uses the divide-and-conquer approach. Here's the intuition:

1. We recursively divide the array into two halves.
2. For each subproblem, we consider three cases:
   a. The maximum subarray is entirely in the left half.
   b. The maximum subarray is entirely in the right half.
   c. The maximum subarray crosses the midpoint.
3. We solve for each case and return the maximum of the three.

Time Complexity: O(n log n), where n is the length of the input array.
Space Complexity: O(log n) due to the recursive call stack.

## Recommendation

I recommend learning and mastering the Kadane's Algorithm (Solution 1) for several reasons:

1. It's more efficient, with O(n) time complexity compared to O(n log n) for the divide-and-conquer approach.
2. It's easier to implement and understand, making it more suitable for interview situations.
3. It demonstrates a good grasp of dynamic programming concepts, which are valuable in many other problems.
4. It uses constant space, which is often preferred in interview settings.

The divide-and-conquer solution is worth understanding conceptually, but it's less likely to be the optimal solution in an interview context unless specifically asked for.

## Test cases

```python
def test_max_subarray():
    solution = Solution()

    # Test case 1: Mixed positive and negative numbers
    assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

    # Test case 2: All positive numbers
    assert solution.maxSubArray([1,2,3,4,5]) == 15

    # Test case 3: All negative numbers
    assert solution.maxSubArray([-1,-2,-3,-4,-5]) == -1

    # Test case 4: Single element array
    assert solution.maxSubArray([42]) == 42

    # Test case 5: Array with zeroes
    assert solution.maxSubArray([-2,0,1,-3,0,4,-1,2,1,-5,4]) == 6

    print("All test cases passed!")

test_max_subarray()
```

## Overview of rejected approaches

1. Brute Force Approach (O(n^2) time complexity):

   - Compute the sum of all possible subarrays and keep track of the maximum.
   - Rejected because it's inefficient for large inputs and doesn't demonstrate understanding of more advanced algorithms.

2. Cumulative Sum Approach (O(n) time, O(n) space):

   - Create a cumulative sum array and find the maximum difference between two elements.
   - While correct, it uses unnecessary extra space and doesn't clearly demonstrate the dynamic programming concept.

3. Recursive Approach without Memoization:

   - Recursively consider including or excluding each element.
   - Rejected due to exponential time complexity and potential for stack overflow on large inputs.

4. Using Built-in Functions:
   - For example, in Python: `max(accumulate(nums, lambda x, y: max(y, x + y)))`
   - While concise, it doesn't clearly demonstrate understanding of the underlying algorithm and may be considered "magical" in an interview setting.

These approaches are either inefficient, use unnecessary space, or don't clearly demonstrate understanding of fundamental algorithmic concepts, making them less suitable for interview situations.

## Visualization(s)

To visualize Kadane's algorithm, let's create a simple React component that shows how the algorithm progresses through the array:

```tsx
import React, { useState, useEffect } from "react";

const KadaneVisualization = () => {
  const [nums, setNums] = useState([-2, 1, -3, 4, -1, 2, 1, -5, 4]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [currentSum, setCurrentSum] = useState(nums[0]);
  const [maxSum, setMaxSum] = useState(nums[0]);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    if (isRunning && currentIndex < nums.length - 1) {
      const timer = setTimeout(() => {
        setCurrentIndex((prevIndex) => prevIndex + 1);
        setCurrentSum((prevSum) =>
          Math.max(nums[currentIndex + 1], prevSum + nums[currentIndex + 1]),
        );
        setMaxSum((prevMax) =>
          Math.max(
            prevMax,
            Math.max(
              nums[currentIndex + 1],
              currentSum + nums[currentIndex + 1],
            ),
          ),
        );
      }, 1000);
      return () => clearTimeout(timer);
    } else if (currentIndex === nums.length - 1) {
      setIsRunning(false);
    }
  }, [isRunning, currentIndex, nums, currentSum]);

  const startVisualization = () => {
    setCurrentIndex(0);
    setCurrentSum(nums[0]);
    setMaxSum(nums[0]);
    setIsRunning(true);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">
        Kadane's Algorithm Visualization
      </h2>
      <div className="flex space-x-2 mb-4">
        {nums.map((num, index) => (
          <div
            key={index}
            className={`w-10 h-10 flex items-center justify-center border ${
              index === currentIndex ? "bg-blue-200" : "bg-gray-100"
            }`}
          >
            {num}
          </div>
        ))}
      </div>
      <div className="mb-4">
        <p>Current Sum: {currentSum}</p>
        <p>Max Sum: {maxSum}</p>
      </div>
      <button
        onClick={startVisualization}
        disabled={isRunning}
        className="px-4 py-2 bg-blue-500 text-white rounded disabled:bg-gray-300"
      >
        {isRunning ? "Running..." : "Start Visualization"}
      </button>
    </div>
  );
};

export default KadaneVisualization;
```

This React component visualizes Kadane's algorithm step by step. It shows:

1. The input array with the current element highlighted.
2. The current sum at each step.
3. The maximum sum found so far.

The visualization progresses automatically, updating every second to show how the algorithm makes decisions at each step. This helps in understanding how Kadane's algorithm maintains and updates the current sum and maximum sum as it iterates through the array.
