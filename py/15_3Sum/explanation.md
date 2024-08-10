# Explanation: 3Sum

## Analysis of problem & input data

This problem, known as 3Sum, is a classic algorithmic challenge that requires finding all unique triplets in an array that sum to zero. Let's break down the key aspects of the problem:

1. Input characteristics:

   - An integer array `nums`
   - Array length is between 3 and 3000
   - Array elements are in the range [-10^5, 10^5]

2. Output requirements:

   - All unique triplets [nums[i], nums[j], nums[k]] where i ≠ j ≠ k and nums[i] + nums[j] + nums[k] = 0
   - No duplicate triplets in the result

3. Key observations:

   - The problem is a variation of the two-sum problem, extended to three numbers
   - The array is not sorted, which affects our approach
   - The constraint on array length (up to 3000) suggests that O(n^2) solutions might be acceptable
   - The range of numbers is large, which makes hash-based solutions viable

4. Pattern-matching insights:

   - This problem falls into the category of "k-sum" problems, where k=3
   - It can be solved using a combination of sorting and two-pointer technique
   - Hash table-based solutions can also be applied

5. Key principle:
   - By fixing one element and then finding pairs that sum to its negation, we can reduce the 3Sum problem to multiple instances of the 2Sum problem

## Solutions

Solution approaches include: Brute Force, Sorting + Two Pointers, Hash Table (3 in total)

### 1. Sorting + Two Pointers

```python
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to enable two-pointer technique
    n = len(nums)
    result = []

    for i in range(n - 2):
        # Skip duplicates for the first element of the triplet
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Use two pointers to find pairs that sum to -nums[i]
        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result
```

Time Complexity: O(n^2)
Space Complexity: O(1) or O(n) depending on the sorting algorithm used

Intuition and invariants:

- Sorting the array allows us to skip duplicates easily and use the two-pointer technique
- By fixing one element, we reduce the problem to finding two numbers that sum to the negation of the fixed element
- The two-pointer technique works because as we move the left pointer right, the sum increases, and as we move the right pointer left, the sum decreases
- Skipping duplicates ensures we don't produce duplicate triplets

### 2. Hash Table Approach

```python
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()  # Sort to handle duplicates easily
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        seen = set()
        for j in range(i + 1, n):
            complement = -nums[i] - nums[j]
            if complement in seen:
                triplet = [nums[i], complement, nums[j]]
                if triplet not in result:  # Avoid duplicates
                    result.append(triplet)
            seen.add(nums[j])

    return result
```

Time Complexity: O(n^2)
Space Complexity: O(n)

Intuition and invariants:

- We fix the first element and then use a hash set to find pairs that sum to its negation
- Sorting helps in skipping duplicates for the first element
- The hash set allows for O(1) lookup time when checking for the complement
- We still need to check for duplicate triplets in the result

### 3. Brute Force Approach

```python
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = set()

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet to avoid duplicates
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)

    return [list(t) for t in result]
```

Time Complexity: O(n^3)
Space Complexity: O(n) for the result set

Intuition and invariants:

- Check all possible triplets
- Use a set to store unique triplets
- Sort each triplet before adding to the set to avoid duplicates

## Recommendation

The Sorting + Two Pointers approach is the best solution to learn for this problem. Here's why:

1. Optimal time complexity: It achieves O(n^2) time complexity, which is the best we can do for this problem without additional constraints.
2. Space efficiency: It uses O(1) extra space (excluding the space for the output).
3. Elegant and intuitive: The solution is straightforward to understand and implement.
4. Handles duplicates efficiently: By sorting and skipping duplicates, it naturally avoids generating duplicate triplets.
5. Generalizable: This approach can be extended to solve k-sum problems for k > 3.

The Hash Table approach is also worth learning as it demonstrates a different technique and can be more efficient for certain input distributions. However, it's slightly more complex and uses more space.

The Brute Force approach, while correct, is not worth learning for interview settings due to its poor time complexity.

## Test cases

```python
def test_threeSum():
    assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert threeSum([0,1,1]) == []
    assert threeSum([0,0,0]) == [[0,0,0]]
    assert threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]]
    assert threeSum([]) == []
    assert threeSum([0]) == []
    print("All test cases passed!")

test_threeSum()
```

## Overview of rejected approaches

1. Binary Search Approach: One might be tempted to use binary search to find the third number after fixing two numbers. While this would improve the time complexity to O(n^2 log n), it's not as efficient as the two-pointer approach and is more complex to implement correctly.

2. Three-pointer Approach: Some might try to use three pointers moving independently. This approach is incorrect as it doesn't guarantee finding all triplets and can be very complex to implement correctly.

3. Dynamic Programming: While DP is often useful for sum problems, it's not suitable here. The problem doesn't have the optimal substructure property required for DP, and we need to find all triplets, not just count them or find the best one.

4. Bit Manipulation: Although bit manipulation can sometimes offer clever solutions, it's not applicable here due to the range of input numbers and the nature of the problem.

## Visualization(s)

For the Sorting + Two Pointers approach, a visual representation can help understand the algorithm:

```tsx
import React, { useState } from "react";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const ThreeSumVisualization = () => {
  const [step, setStep] = useState(0);
  const nums = [-1, 0, 1, 2, -1, -4];
  const sortedNums = [-4, -1, -1, 0, 1, 2];

  const steps = [
    { text: "Initial array", array: nums },
    { text: "Sorted array", array: sortedNums },
    {
      text: "Fix -4, left=1, right=5",
      array: sortedNums,
      i: 0,
      left: 1,
      right: 5,
    },
    {
      text: "Fix -1, left=2, right=5",
      array: sortedNums,
      i: 1,
      left: 2,
      right: 5,
    },
    {
      text: "Found triplet: [-1,-1,2]",
      array: sortedNums,
      i: 1,
      left: 2,
      right: 5,
      highlight: [1, 2, 5],
    },
    {
      text: "Fix -1, left=3, right=4",
      array: sortedNums,
      i: 2,
      left: 3,
      right: 4,
    },
    {
      text: "Found triplet: [-1,0,1]",
      array: sortedNums,
      i: 2,
      left: 3,
      right: 4,
      highlight: [2, 3, 4],
    },
  ];

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader className="text-xl font-bold">3Sum Visualization</CardHeader>
      <CardContent>
        <div className="flex justify-center mb-4">
          {steps[step].array.map((num, index) => (
            <div
              key={index}
              className={`w-10 h-10 flex items-center justify-center border border-gray-300 m-1 ${
                index === steps[step].i
                  ? "bg-blue-200"
                  : index === steps[step].left
                    ? "bg-green-200"
                    : index === steps[step].right
                      ? "bg-red-200"
                      : steps[step].highlight?.includes(index)
                        ? "bg-yellow-200"
                        : ""
              }`}
            >
              {num}
            </div>
          ))}
        </div>
        <p className="text-center mb-4">{steps[step].text}</p>
        <div className="flex justify-between">
          <Button
            onClick={() => setStep(Math.max(0, step - 1))}
            disabled={step === 0}
          >
            Previous
          </Button>
          <Button
            onClick={() => setStep(Math.min(steps.length - 1, step + 1))}
            disabled={step === steps.length - 1}
          >
            Next
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};

export default ThreeSumVisualization;
```

This visualization demonstrates the key steps of the Sorting + Two Pointers approach, showing how we fix one element and use two pointers to find the other two elements of the triplet.
