## Explanation: Rotate Array

### Analysis of problem & input data

This problem is about rotating an array to the right by a given number of steps. The key characteristics of this problem are:

1. We're dealing with a 1D array of integers.
2. The rotation is to the right, which means elements at the end of the array will wrap around to the beginning.
3. The number of rotation steps (k) can be any non-negative integer, potentially larger than the array length.
4. The array can have any length from 1 to 10^5^, which means we need to consider both small and large arrays.
5. The rotation needs to be done in-place with O(1) extra space (as per the follow-up question).

The key principle that makes this question simple is understanding that rotating an array by its length (or multiples of its length) results in the original array. This means we can simplify our rotation by taking k modulo the length of the array.

Another important insight is that rotating an array can be achieved by reversing specific portions of the array. This leads to an elegant in-place solution.

### Test cases

1. Normal case: `nums = [1,2,3,4,5,6,7], k = 3`
2. Small array: `nums = [1,2], k = 1`
3. k greater than array length: `nums = [1,2,3], k = 5`
4. k equal to array length: `nums = [1,2,3,4], k = 4`
5. Single element array: `nums = [1], k = 3`
6. k = 0 (no rotation): `nums = [1,2,3], k = 0`
7. Large array: `nums = list(range(100000)), k = 54321`

Here's the executable Python code for these test cases:

```python
def rotate(nums: List[int], k: int) -> None:
    # Implementation will go here
    pass

test_cases = [
    ([1,2,3,4,5,6,7], 3),
    ([1,2], 1),
    ([1,2,3], 5),
    ([1,2,3,4], 4),
    ([1], 3),
    ([1,2,3], 0),
    (list(range(100000)), 54321)
]

for nums, k in test_cases:
    nums_copy = nums.copy()
    rotate(nums_copy, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {nums_copy}")
    print()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Reverse Method (Neetcode solution)
2. Cyclic Replacements
3. Using Extra Array
4. Slice Assignment (Python-specific)

Count: 4 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force (rotate one-by-one)
2. Recursive Approach

#### Worthy Solutions

##### Reverse Method

```python
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n  # Normalize k

    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the remaining n-k elements
    reverse(k, n - 1)
```

Time Complexity: O(n), where n is the length of the array. We reverse the entire array once and then reverse two portions of the array.
Space Complexity: O(1), as we're modifying the array in-place.

Explanation:

- This solution leverages the fact that reversing specific portions of the array can achieve rotation.
- By reversing the entire array, then reversing the first k elements, and finally reversing the remaining n-k elements, we effectively rotate the array to the right by k positions.
- The key insight is that reversing brings the last element to the front, and reversing parts of the array puts those elements in the correct order.

##### Cyclic Replacements

```python
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    count = 0

    for start in range(n):
        if count >= n:  # All elements have been moved
            return

        current = start
        prev = nums[start]

        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1

            if start == current:
                break
```

Time Complexity: O(n), where n is the length of the array. Each element is moved exactly once.
Space Complexity: O(1), as we're using only a constant amount of extra space.

Explanation:

- This solution uses the concept of cyclic replacements.
- We start from each index and follow the cycle of replacements until we return to the starting index.
- The key insight is that each element will be placed k positions ahead of its current position.
- We use modulo operation to wrap around the array when we reach the end.
- We keep track of the number of moves to ensure we don't exceed n moves (which would cover all elements).

##### Using Extra Array

```python
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    temp = [0] * n

    for i in range(n):
        temp[(i + k) % n] = nums[i]

    nums[:] = temp
```

Time Complexity: O(n), where n is the length of the array. We iterate through the array once.
Space Complexity: O(n), as we use an additional array of the same size as the input array.

Explanation:

- This solution uses an extra array to store the rotated elements.
- We calculate the new position of each element using the formula (i + k) % n.
- After placing all elements in their new positions in the temporary array, we copy it back to the original array.
- The key insight is that we can easily calculate the new position of each element without actually rotating.

##### Slice Assignment (Python-specific)

```python
def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    nums[:] = nums[n-k:] + nums[:n-k]
```

Time Complexity: O(n), where n is the length of the array. Although it looks simple, Python internally creates a new list and then assigns it back to nums.
Space Complexity: O(n), as a new list is created internally.

Explanation:

- This solution leverages Python's slice assignment feature.
- We split the array into two parts: the last k elements and the first n-k elements.
- We then concatenate these parts in the reverse order and assign the result back to nums.
- The key insight is that rotation can be achieved by rearranging two slices of the array.

#### Rejected Approaches

1. Brute Force (rotate one-by-one):
   This approach would involve rotating the array one step at a time, k times. While correct, it has a time complexity of O(n\*k), which is inefficient for large k.

2. Recursive Approach:
   A recursive solution might seem elegant, but it would use O(k) space for the call stack and doesn't offer any significant advantages over the iterative solutions.

#### Final Recommendations

The Reverse Method (Neetcode solution) is the best to learn for several reasons:

1. It's in-place, satisfying the O(1) space requirement.
2. It has a clear and intuitive logic that's easy to understand and explain.
3. It's efficient with O(n) time complexity.
4. It demonstrates a clever use of array manipulation that can be applied to other problems.

The Cyclic Replacements method is also worth understanding as it provides a different perspective on array manipulation and can be useful in other array rotation or permutation problems.

### Visualization(s)

For the Reverse Method, here's a simple visualization:

```tsx
import React, { useState } from "react";
import { Button } from "@/components/ui/button";

const RotateArrayVisualization = () => {
  const [array, setArray] = useState([1, 2, 3, 4, 5, 6, 7]);
  const [step, setStep] = useState(0);
  const k = 3;

  const reverse = (arr, start, end) => {
    const result = [...arr];
    while (start < end) {
      [result[start], result[end]] = [result[end], result[start]];
      start++;
      end--;
    }
    return result;
  };

  const steps = [
    { description: "Initial array", array: [1, 2, 3, 4, 5, 6, 7] },
    {
      description: "Reverse entire array",
      array: reverse([1, 2, 3, 4, 5, 6, 7], 0, 6),
    },
    {
      description: `Reverse first ${k} elements`,
      array: reverse([7, 6, 5, 4, 3, 2, 1], 0, k - 1),
    },
    {
      description: `Reverse last ${7 - k} elements`,
      array: reverse([5, 6, 7, 4, 3, 2, 1], k, 6),
    },
  ];

  const nextStep = () =>
    setStep((prevStep) => Math.min(prevStep + 1, steps.length - 1));
  const prevStep = () => setStep((prevStep) => Math.max(prevStep - 1, 0));

  return (
    <div className="p-4 max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
      <h2 className="text-xl font-bold mb-4">Rotate Array Visualization</h2>
      <div className="mb-4">
        <p className="font-semibold">
          Step {step + 1}: {steps[step].description}
        </p>
        <div className="flex justify-center items-center space-x-2 my-4">
          {steps[step].array.map((num, index) => (
            <div
              key={index}
              className="w-10 h-10 flex items-center justify-center border border-gray-300 rounded"
            >
              {num}
            </div>
          ))}
        </div>
      </div>
      <div className="flex justify-between">
        <Button onClick={prevStep} disabled={step === 0}>
          Previous
        </Button>
        <Button onClick={nextStep} disabled={step === steps.length - 1}>
          Next
        </Button>
      </div>
    </div>
  );
};

export default RotateArrayVisualization;
```

This visualization demonstrates the steps of the Reverse Method for rotating the array [1, 2, 3, 4, 5, 6, 7] by k=3 positions to the right. You can step through the process to see how the array changes at each stage of the algorithm.
