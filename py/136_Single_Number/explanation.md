Thank you for providing the problem description. I'll present different solutions to the "Single Number" problem, explain their complexities, and recommend the best approach. Let's start with the solutions:

1. Brute Force Approach (Not Recommended)

```python
def single_number(nums: List[int]) -> int:
    for i in range(len(nums)):
        is_unique = True
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                is_unique = False
                break
        if is_unique:
            return nums[i]
    return -1  # This line should never be reached given the problem constraints
```

Time Complexity: O(n^2) - We have nested loops, each iterating through the array.
Space Complexity: O(1) - We only use a constant amount of extra space.

This approach is not recommended as it doesn't meet the linear runtime complexity requirement.

2. Sorting Approach (Not Recommended)

```python
def single_number(nums: List[int]) -> int:
    nums.sort()  # Sort the array
    for i in range(0, len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]  # If we reached here, the last element is the single one
```

Time Complexity: O(n log n) - Dominated by the sorting operation.
Space Complexity: O(1) or O(n) depending on the sorting algorithm used.

This approach is not recommended as it doesn't meet the linear runtime complexity requirement.

3. Hash Table Approach (Not Recommended for this specific problem)

```python
from collections import defaultdict

def single_number(nums: List[int]) -> int:
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
    for num, freq in count.items():
        if freq == 1:
            return num
    return -1  # This line should never be reached given the problem constraints
```

Time Complexity: O(n) - We iterate through the array twice.
Space Complexity: O(n) - In the worst case, we store n/2 + 1 elements in the hash table.

While this approach meets the linear runtime complexity requirement, it doesn't satisfy the constant extra space requirement.

4. XOR Approach (Recommended Solution)

```python
def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result
```

Time Complexity: O(n) - We iterate through the array once.
Space Complexity: O(1) - We only use a single variable to store the result.

This is the recommended solution as it meets both the linear runtime complexity and constant extra space requirements.

Explanation of the XOR approach:

- XOR (exclusive or) operation has the following properties:
  1. a ^ 0 = a
  2. a ^ a = 0
  3. a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
- By XORing all numbers in the array, the duplicate numbers will cancel out (property 2), and we'll be left with the single number (property 3).

Let's create a visualization to help explain the XOR approach:

```tsx
import React, { useState } from "react";
import { Card, CardHeader, CardContent } from "@/components/ui/card";

const XORVisualization = () => {
  const [step, setStep] = useState(0);
  const nums = [4, 1, 2, 1, 2];
  const results = nums.reduce(
    (acc, num) => [...acc, acc[acc.length - 1] ^ num],
    [0],
  );

  const binaryString = (num) => num.toString(2).padStart(8, "0");

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>XOR Approach Visualization</CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div>Input: [{nums.join(", ")}]</div>
          <div className="flex justify-between items-center">
            <button
              onClick={() => setStep(Math.max(0, step - 1))}
              className="px-4 py-2 bg-blue-500 text-white rounded"
              disabled={step === 0}
            >
              Previous
            </button>
            <span>
              Step {step + 1} of {nums.length + 1}
            </span>
            <button
              onClick={() => setStep(Math.min(nums.length, step + 1))}
              className="px-4 py-2 bg-blue-500 text-white rounded"
              disabled={step === nums.length}
            >
              Next
            </button>
          </div>
          <div className="space-y-2">
            <div>Current: {binaryString(results[step])}</div>
            {step < nums.length && (
              <>
                <div>XOR</div>
                <div>Next num: {binaryString(nums[step])}</div>
                <div>Result: {binaryString(results[step + 1])}</div>
              </>
            )}
          </div>
          {step === nums.length && (
            <div className="font-bold">
              Final result: {results[step]} (Single number)
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
};

export default XORVisualization;
```

This visualization allows you to step through the XOR process, showing how each number in the input array affects the result. You can see how the duplicate numbers cancel out, leaving only the single number at the end.

Now, let's provide some test cases:

```python
def test_single_number():
    assert single_number([2,2,1]) == 1
    assert single_number([4,1,2,1,2]) == 4
    assert single_number([1]) == 1
    assert single_number([1,3,1,-1,3]) == -1
    print("All test cases passed!")

test_single_number()
```

These test cases cover the examples provided in the problem description and add an additional case with negative numbers.

In conclusion, the XOR approach (Solution 4) is the recommended solution for this problem. It satisfies both the linear time complexity and constant space complexity requirements. It's also elegant and efficient, leveraging the properties of the XOR operation to solve the problem in a single pass through the array.
