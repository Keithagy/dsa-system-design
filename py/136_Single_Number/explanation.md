## Explanation: Single Number

### Analysis of problem & input data

This problem presents a unique challenge in finding a single element that appears only once in an array where every other element appears twice. The key characteristics of this problem are:

1. The array is non-empty.
2. All elements appear twice except for one.
3. We need to find the element that appears only once.
4. The solution must have linear time complexity O(n) and constant space complexity O(1).

The constraints on time and space complexity are crucial here, as they rule out some straightforward approaches like sorting or using a hash map.

The key principle that makes this question simple is the property of XOR (exclusive or) operation:

1. XOR of a number with itself is 0.
2. XOR of a number with 0 is the number itself.
3. XOR is commutative and associative.

These properties of XOR allow us to cancel out all the pairs of numbers that appear twice, leaving us with the single number that appears only once.

### Test cases

1. Basic case: `[2,2,1]` → Output: `1`
2. Multiple pairs: `[4,1,2,1,2]` → Output: `4`
3. Single element: `[1]` → Output: `1`
4. Negative numbers: `[-1,-1,-2]` → Output: `-2`
5. Large numbers: `[100000,100000,99999]` → Output: `99999`
6. Mixed positive and negative: `[-1,1,1,-2,-2]` → Output: `-1`

Here's the executable Python code for these test cases:

```python
def single_number(nums: List[int]) -> int:
    # Implementation will be added here
    pass

# Test cases
test_cases = [
    [2,2,1],
    [4,1,2,1,2],
    [1],
    [-1,-1,-2],
    [100000,100000,99999],
    [-1,1,1,-2,-2]
]

for i, case in enumerate(test_cases, 1):
    result = single_number(case)
    print(f"Test case {i}: {case} → Output: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. XOR approach (Bit Manipulation)
2. Math approach (Set operations)

Count: 2 solutions

##### Rejected solutions

1. Sorting approach
2. Hash Map approach
3. Brute Force approach

#### Worthy Solutions

##### XOR approach (Bit Manipulation)

```python
from typing import List

def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we only use a single variable regardless of input size.

Intuitions and invariants:

- XOR of a number with itself is 0.
- XOR of a number with 0 is the number itself.
- XOR is commutative and associative, so the order of operations doesn't matter.
- By XORing all numbers, pairs cancel out, leaving only the single number.

The algorithm leverages the XOR operation to efficiently cancel out all pairs of numbers, leaving only the single number that appears once. This approach is elegant and optimal for this problem, satisfying both the time and space complexity requirements.

##### Math approach (Set operations)

```python
from typing import List

def single_number(nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(n) in the worst case, as we create a set from the input array.

Intuitions and invariants:

- Set eliminates duplicates, keeping only unique elements.
- Sum of set gives sum of all unique numbers.
- Multiplying this sum by 2 accounts for each number appearing twice.
- Subtracting the sum of the original array leaves only the single number.

While this approach is mathematically elegant and easy to understand, it doesn't strictly meet the constant space requirement. However, it's worth learning for its clever use of set properties and arithmetic.

#### Rejected Approaches

1. Sorting approach: Sorting the array and then finding the element without a pair would take O(n log n) time, violating the linear time requirement.

2. Hash Map approach: Using a hash map to count occurrences would take O(n) time but O(n) space, violating the constant space requirement.

3. Brute Force approach: Checking each element against all others would take O(n^2) time, violating the linear time requirement.

These approaches, while potentially correct, are not optimal for this specific problem due to their time or space complexity.

#### Final Recommendations

The XOR approach is the best solution to learn for this problem. It elegantly satisfies both the time and space complexity requirements, leveraging a clever bit manipulation technique. This solution demonstrates a deep understanding of bitwise operations and their applications in algorithmic problem-solving, making it highly valuable in a technical interview setting.

### Visualization(s)

To visualize the XOR approach, let's create a simple React component that demonstrates how XOR cancels out pairs and leaves the single number:

```tsx
import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

const XORVisualization = () => {
  const [numbers, setNumbers] = useState([4, 1, 2, 1, 2]);
  const [currentStep, setCurrentStep] = useState(0);

  const xorOperation = (a, b) => a ^ b;

  const reset = () => {
    setCurrentStep(0);
  };

  const nextStep = () => {
    setCurrentStep((prev) => Math.min(prev + 1, numbers.length));
  };

  const result = numbers.reduce(xorOperation, 0);

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-4">XOR Approach Visualization</h2>
      <div className="mb-4">
        <Input
          type="text"
          value={numbers.join(", ")}
          onChange={(e) => setNumbers(e.target.value.split(",").map(Number))}
          placeholder="Enter numbers separated by commas"
          className="w-full p-2 border rounded"
        />
      </div>
      <div className="mb-4">
        <p className="font-semibold">Current XOR Result:</p>
        <p className="text-3xl font-bold">
          {numbers.slice(0, currentStep).reduce(xorOperation, 0)}
        </p>
      </div>
      <div className="flex space-x-2 mb-4">
        <Button onClick={reset} className="bg-red-500 text-white">
          Reset
        </Button>
        <Button
          onClick={nextStep}
          disabled={currentStep >= numbers.length}
          className="bg-blue-500 text-white"
        >
          Next Step
        </Button>
      </div>
      <div>
        {numbers.map((num, index) => (
          <div
            key={index}
            className={`p-2 mb-2 ${index < currentStep ? "bg-green-200" : "bg-gray-200"} rounded`}
          >
            {num}
          </div>
        ))}
      </div>
      <p className="mt-4 font-semibold">Final Result: {result}</p>
    </div>
  );
};

export default XORVisualization;
```

This visualization allows users to input their own set of numbers and step through the XOR process, helping to build intuition for how the algorithm works.
