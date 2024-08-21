## Explanation: 3Sum

### Analysis of problem & input data

The 3Sum problem is a classic algorithmic challenge that requires finding all unique triplets in an array that sum to zero. This problem is particularly interesting because it's a variation of the more general k-Sum problem, where k=3.

Key characteristics of the problem:

1. We're dealing with an unsorted integer array.
2. We need to find all unique triplets, not just one.
3. The order of triplets and elements within triplets doesn't matter.
4. We need to avoid duplicate triplets in the output.

The input data characteristics are crucial:

- Array length is between 3 and 3000, so brute force solutions will likely time out.
- Elements can be positive, negative, or zero, which is important for our solution strategy.
- The range of values is quite large (-10^5 to 10^5), which affects how we handle potential overflow.

The key principle that makes this question simple is the realization that we can reduce it to a series of 2Sum problems after sorting the array. This pattern-matching to the 2Sum problem, combined with sorting, is what enables an efficient solution.

### Test cases

1. Standard case: `[-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`
2. All zeros: `[0,0,0]` → `[[0,0,0]]`
3. No solution: `[1,2,3]` → `[]`
4. Duplicates: `[-2,0,0,2,2]` → `[[-2,0,2]]`
5. Negative numbers: `[-1,-2,-3,4,5,6]` → `[[-3,-2,5],[-3,-1,4]]`
6. Large numbers: `[-100000,50000,50000]` → `[[-100000,50000,50000]]`
7. Minimum length: `[1,1,1]` → `[]`

Here's the Python code for these test cases:

```python
def test_three_sum(three_sum_func):
    test_cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,0,0], [[0,0,0]]),
        ([1,2,3], []),
        ([-2,0,0,2,2], [[-2,0,2]]),
        ([-1,-2,-3,4,5,6], [[-3,-2,5],[-3,-1,4]]),
        ([-100000,50000,50000], [[-100000,50000,50000]]),
        ([1,1,1], [])
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = three_sum_func(nums)
        assert sorted(result) == sorted(expected), f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All test cases passed!")

# Usage:
# test_three_sum(your_three_sum_function)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Sorting + Two Pointers: The most optimal and elegant solution.
2. Sorting + HashSet: A slight variation that uses a set instead of two pointers.
3. No-sort HashSet: A solution that doesn't require sorting but uses more space.

Count: 3 solutions

##### Rejected solutions

1. Brute Force: O(n^3) time complexity, too slow for larger inputs.
2. Binary Search: While tempting, it's not as efficient as the two-pointer approach.

#### Worthy Solutions

##### Sorting + Two Pointers

```python
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to enable two-pointer technique
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicates for the first element of the triplet
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result
```

Time Complexity: O(n^2)
Space Complexity: O(1) if we don't count the space for the output, O(n) if we do.

- The algorithm leverages sorting to enable efficient two-pointer traversal.
- By fixing one element and using two pointers for the other two, we reduce the 3Sum problem to multiple 2Sum problems.
- Sorting allows us to skip duplicates easily, ensuring unique triplets.
- The two-pointer technique exploits the sorted nature of the array to converge on the target sum efficiently.

##### Sorting + HashSet

```python
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        seen = set()
        for j in range(i + 1, n):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], complement, nums[j]])
                while j + 1 < n and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])

    return result
```

Time Complexity: O(n^2)
Space Complexity: O(n)

- This approach still uses sorting but replaces the second pointer with a HashSet.
- It treats the problem as finding a complement in a set for each pair of elements.
- The HashSet allows for O(1) lookups, potentially speeding up the inner loop.
- Duplicate handling is still necessary to ensure unique triplets.

##### No-sort HashSet

```python
from typing import List
from collections import Counter

def threeSum(nums: List[int]) -> List[List[int]]:
    result = set()
    dups = set()
    seen = {}
    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    result.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
    return [list(x) for x in result]
```

Time Complexity: O(n^2)
Space Complexity: O(n)

- This approach avoids sorting the input array.
- It uses a HashSet to keep track of seen values and to store the final result (as tuples to allow hashing).
- The algorithm handles duplicates by using sets and only processing each unique value once.
- While it has the same time complexity as the sorted approaches, it may be slower in practice due to the overhead of set operations.

#### Rejected Approaches

1. Brute Force (O(n^3)):

   ```python
   def threeSum(nums: List[int]) -> List[List[int]]:
       n = len(nums)
       result = []
       for i in range(n-2):
           for j in range(i+1, n-1):
               for k in range(j+1, n):
                   if nums[i] + nums[j] + nums[k] == 0:
                       result.append([nums[i], nums[j], nums[k]])
       return [list(x) for x in set(tuple(sorted(r)) for r in result)]
   ```

   This approach is correct but extremely inefficient for large inputs. It's not worth learning because it doesn't scale well and doesn't teach any useful algorithmic techniques.

2. Binary Search (O(n^2 log n)):
   While using binary search to find the third number after fixing two numbers might seem like a good idea, it's actually less efficient than the two-pointer approach. The two-pointer method achieves O(n) for the inner loop, while binary search would be O(log n) for each pair, resulting in a total of O(n^2 log n).

#### Final Recommendations

The Sorting + Two Pointers approach is the best to learn for several reasons:

1. It's the most efficient in both time and space complexity.
2. It teaches important concepts like sorting for optimization and the two-pointer technique.
3. It's elegant and relatively easy to understand and implement.
4. It's a pattern that can be applied to other similar problems (e.g., 4Sum).

The other approaches are worth understanding conceptually, but the two-pointer method should be your go-to solution for 3Sum and similar problems in interview settings.

### Visualization(s)

To visualize the two-pointer approach, we can use a simple React component that shows how the pointers move:

```tsx
import React, { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";

const ThreeSumVisualization = () => {
  const [nums, setNums] = useState([-1, 0, 1, 2, -1, -4]);
  const [i, setI] = useState(0);
  const [left, setLeft] = useState(1);
  const [right, setRight] = useState(nums.length - 1);
  const [result, setResult] = useState([]);
  const [step, setStep] = useState(0);

  useEffect(() => {
    setNums([...nums].sort((a, b) => a - b));
  }, []);

  const nextStep = () => {
    if (i >= nums.length - 2) return;

    const sum = nums[i] + nums[left] + nums[right];

    if (sum === 0) {
      setResult([...result, [nums[i], nums[left], nums[right]]]);
      setLeft(left + 1);
      setRight(right - 1);
    } else if (sum < 0) {
      setLeft(left + 1);
    } else {
      setRight(right - 1);
    }

    if (left >= right) {
      setI(i + 1);
      setLeft(i + 2);
      setRight(nums.length - 1);
    }

    setStep(step + 1);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">3Sum Visualization</h2>
      <div className="mb-4">
        {nums.map((num, index) => (
          <span
            key={index}
            className={`inline-block p-2 m-1 rounded ${
              index === i
                ? "bg-blue-500 text-white"
                : index === left
                  ? "bg-green-500 text-white"
                  : index === right
                    ? "bg-red-500 text-white"
                    : "bg-gray-200"
            }`}
          >
            {num}
          </span>
        ))}
      </div>
      <div className="mb-4">
        <p>Fixed: {nums[i]}</p>
        <p>Left: {nums[left]}</p>
        <p>Right: {nums[right]}</p>
        <p>Sum: {nums[i] + nums[left] + nums[right]}</p>
      </div>
      <div className="mb-4">
        <h3 className="font-bold">Result:</h3>
        {result.map((triplet, index) => (
          <p key={index}>[{triplet.join(", ")}]</p>
        ))}
      </div>
      <Button onClick={nextStep}>Next Step</Button>
    </div>
  );
};

export default ThreeSumVisualization;
```

This visualization component demonstrates how the two-pointer approach works step-by-step. You can see how the fixed pointer (blue), left pointer (green), and right pointer (red) move through the array to find triplets that sum to zero.
