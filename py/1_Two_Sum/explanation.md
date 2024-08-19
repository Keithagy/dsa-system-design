# Explanation: Two Sum

## Analysis of problem & input data

The Two Sum problem is a classic algorithmic challenge that tests our ability to efficiently search for complementary pairs in an array. Here are the key aspects of the problem:

1. Input: An array of integers (nums) and a target sum (target).
2. Output: Indices of two numbers in the array that add up to the target.
3. Constraint: Each input has exactly one solution.
4. Constraint: The same element cannot be used twice.

Key principles that make this problem simple:

1. Complement calculation: For any number x, its complement to reach the target is (target - x).
2. Hash table for constant-time lookup: Using a hash table allows us to check if a complement exists in constant time.

The problem's characteristics that guide our solution strategy:

1. The array is not sorted, which rules out certain optimization techniques.
2. The constraint of having exactly one solution simplifies our approach.
3. The large range of possible values (-10^9 to 10^9) suggests that we should be cautious about space complexity.

### Test cases

1. Basic case:
   Input: nums = [2,7,11,15], target = 9
   Expected Output: [0,1]

2. Repeated numbers:
   Input: nums = [3,3], target = 6
   Expected Output: [0,1]

3. Negative numbers:
   Input: nums = [-1,-2,-3,-4,-5], target = -8
   Expected Output: [2,4]

4. Large numbers:
   Input: nums = [1000000000,1000000000], target = 2000000000
   Expected Output: [0,1]

5. Minimum length array:
   Input: nums = [5,5], target = 10
   Expected Output: [0,1]

Here's the Python code for these test cases:

```python
def test_two_sum(two_sum_func):
    test_cases = [
        ([2,7,11,15], 9, [0,1]),
        ([3,3], 6, [0,1]),
        ([-1,-2,-3,-4,-5], -8, [2,4]),
        ([1000000000,1000000000], 2000000000, [0,1]),
        ([5,5], 10, [0,1])
    ]

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = two_sum_func(nums, target)
        assert sorted(result) == expected, f"Test case {i} failed. Expected {expected}, got {result}"
    print("All test cases passed!")

# The two_sum_func should be replaced with the actual implementation
# test_two_sum(two_sum_func)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Hash Table (One-pass)
2. Hash Table (Two-pass)
3. Brute Force

3 solutions worth learning.

#### Rejected solutions

1. Sorting and Two Pointers: While this approach works for finding the values, it doesn't preserve the original indices.
2. Binary Search: Not optimal for unsorted input.

### Worthy Solutions

#### Hash Table (One-pass)

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    # Hash map to store complements and their indices
    complement_map = {}

    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # If the complement exists in our map, we've found the pair
        if complement in complement_map:
            return [complement_map[complement], i]

        # Otherwise, add the current number and its index to the map
        complement_map[num] = i

    # If no solution is found (which shouldn't happen given the problem constraints)
    return []  # or raise an exception
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(n) in the worst case, where we might need to store nearly all elements in the hash map.

Key intuitions and invariants:

- We can find the solution in a single pass through the array.
- For each number, we only need to check if its complement exists.
- The hash map allows us to check for complement existence in O(1) time.
- We're building the hash map as we go, which allows us to find the solution as soon as we encounter the second number of the pair.

#### Hash Table (Two-pass)

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    # First pass: Build the hash map
    num_map = {num: i for i, num in enumerate(nums)}

    # Second pass: Check for complements
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]

    # If no solution is found (which shouldn't happen given the problem constraints)
    return []  # or raise an exception
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(n) to store the hash map.

Key intuitions and invariants:

- We separate the process into two distinct phases: building the map and finding the solution.
- This approach is slightly less efficient than the one-pass solution but may be more intuitive for some.
- The check `num_map[complement] != i` ensures we don't use the same element twice.

#### Brute Force

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    # If no solution is found (which shouldn't happen given the problem constraints)
    return []  # or raise an exception
```

Time Complexity: O(n^2), where n is the length of the input array.
Space Complexity: O(1), as we only use a constant amount of extra space.

Key intuitions and invariants:

- This approach checks all possible pairs of numbers.
- The inner loop starts from `i + 1` to avoid using the same element twice and to prevent duplicate checking of pairs.
- While simple to understand, this solution is inefficient for large inputs.

### Rejected Approaches

1. Sorting and Two Pointers:

   - Why it seems correct: Sorting allows us to use two pointers to efficiently find the pair that sums to the target.
   - Why it's not suitable: Sorting the array would change the indices of the elements, losing the original position information required by the problem.

2. Binary Search:
   - Why it seems tempting: Binary search is an efficient way to find a specific value in a sorted array.
   - Why it's not optimal: The input array is not sorted, and sorting it would change the indices. Even if we sorted a copy of the array, we'd still need to do n searches, resulting in O(n log n) time complexity, which is worse than our O(n) hash table solution.

### Final Recommendations

The Hash Table (One-pass) solution is the best one to learn for this problem. Here's why:

1. Time Efficiency: It solves the problem in O(n) time, which is optimal for this problem.
2. Space Efficiency: While it uses O(n) space, this is generally acceptable given the time efficiency gained.
3. Elegance: It solves the problem in a single pass through the array, demonstrating a clean and efficient approach.
4. Demonstrable Skills: It showcases your understanding of hash tables and your ability to optimize for both time and space.

The Two-pass Hash Table solution is also worth understanding as it might be more intuitive for some interviewers or in certain variations of the problem.

The Brute Force solution, while correct, is not worth learning deeply for interviews. It's good to mention it as a starting point to show your problem-solving process, but you should quickly move on to more efficient solutions.

Remember, in a real interview setting, it's often good to start by mentioning the brute force approach to show you can solve the problem, then work your way towards the optimal solution. This demonstrates your problem-solving process and ability to optimize.

## Visualization(s)

Here's a simple visualization of how the one-pass hash table solution works:

```tsx
import React, { useState } from "react";

const TwoSumVisualization = () => {
  const [step, setStep] = useState(0);
  const nums = [2, 7, 11, 15];
  const target = 9;
  const steps = [
    { map: {}, current: null, complement: null, found: false },
    { map: { 2: 0 }, current: 7, complement: 2, found: true },
    { map: { 2: 0, 7: 1 }, current: null, complement: null, found: true },
  ];

  const currentStep = steps[step];

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Two Sum Visualization</h2>
      <div className="mb-4">
        <span className="font-bold">Input:</span> nums = [{nums.join(", ")}],
        target = {target}
      </div>
      <div className="mb-4">
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
          onClick={() => setStep(Math.max(0, step - 1))}
          disabled={step === 0}
        >
          Previous
        </button>
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          onClick={() => setStep(Math.min(steps.length - 1, step + 1))}
          disabled={step === steps.length - 1}
        >
          Next
        </button>
      </div>
      <div className="mb-4">
        <span className="font-bold">Step:</span> {step + 1}
      </div>
      <div className="mb-4">
        <span className="font-bold">Hash Map:</span>{" "}
        {JSON.stringify(currentStep.map)}
      </div>
      {currentStep.current !== null && (
        <div className="mb-4">
          <span className="font-bold">Current Number:</span>{" "}
          {currentStep.current}
        </div>
      )}
      {currentStep.complement !== null && (
        <div className="mb-4">
          <span className="font-bold">Complement:</span>{" "}
          {currentStep.complement}
        </div>
      )}
      {currentStep.found && (
        <div className="text-green-500 font-bold">
          Solution found! Indices: [{currentStep.map[currentStep.complement]},{" "}
          {step}]
        </div>
      )}
    </div>
  );
};

export default TwoSumVisualization;
```

This visualization shows how the hash map is built and used to find the solution in the one-pass approach. You can step through the process to see how the algorithm works.
