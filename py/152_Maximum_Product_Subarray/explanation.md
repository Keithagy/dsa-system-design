## Explanation: Maximum Product Subarray

### Analysis of problem & input data

This problem is a variation of the classic "maximum subarray" problem, but with a crucial twist: we're dealing with products instead of sums. This change introduces several key considerations:

1. **Sign of numbers**: Unlike the sum problem, negative numbers can potentially lead to the maximum product if there's an even number of them.
2. **Zero handling**: Zeros effectively "reset" our product, splitting the array into subarrays.
3. **Range of values**: The product can grow or shrink exponentially, unlike sums which grow linearly.

The key principle that makes this question manageable is the observation that at each index, the maximum product ending at that index is either:
a) The number itself
b) The product of the number and the maximum product ending at the previous index
c) The product of the number and the minimum product ending at the previous index (in case of negative numbers)

This insight allows us to use dynamic programming or a sliding window approach to solve the problem efficiently.
[Neetcode video](https://www.youtube.com/watch?v=lXVy6YWFcRM)

### Test cases

1. **Basic case**: `[2,3,-2,4]` → 6 (subarray [2,3])
2. **All positive**: `[1,2,3,4]` → 24 (whole array)
3. **All negative**: `[-1,-2,-3]` → 6 (subarray [-2,-3])
4. **Contains zero**: `[-2,0,-1]` → 0
5. **Negative result**: `[-1,-2,-3,-4]` → 24 (whole array)
6. **Single element**: `[5]` → 5
7. **Two elements**: `[-4,-3]` → 12
8. **Alternating signs**: `[1,-2,3,-4]` → 24 (whole array)

```python
def test_max_product_subarray(func):
    test_cases = [
        ([2,3,-2,4], 6),
        ([1,2,3,4], 24),
        ([-1,-2,-3], 6),
        ([-2,0,-1], 0),
        ([-1,-2,-3,-4], 24),
        ([5], 5),
        ([-4,-3], 12),
        ([1,-2,3,-4], 24)
    ]
    for i, (nums, expected) in enumerate(test_cases):
        result = func(nums)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
        if result != expected:
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Dynamic Programming (Kadane's Algorithm variation) [Neetcode solution]
2. Two-pass approach
3. Sliding window with prefix and suffix products

Count: 3 (1 Neetcode solution)

##### Rejected solutions

1. Brute force (checking all subarrays)
2. Recursive approach (without memoization)
3. Sorting-based approach

#### Worthy Solutions

##### Dynamic Programming (Kadane's Algorithm variation)

```python
def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max

        result = max(max_so_far, result)

    return result
```

Time Complexity: O(n), where n is the length of the input array. We iterate through the array once.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation:

- This solution is a variation of Kadane's algorithm, adapted for the product instead of sum.
- We maintain two variables: `max_so_far` and `min_so_far`, representing the maximum and minimum product ending at the current position.
- For each element, we calculate three possibilities:
  1. The element itself
  2. The product of the element and the previous maximum
  3. The product of the element and the previous minimum
- We update `max_so_far` and `min_so_far` based on these calculations.
- We keep track of the overall maximum product in the `result` variable.

Key intuitions:

- A negative number can turn the smallest previous product into the largest current product.
- We need to keep track of both the maximum and minimum products because the sign changes can affect which one leads to the maximum overall product.
- This approach effectively handles zeros by resetting the product sequence.

##### Two-pass approach

```python
def maxProduct(nums: List[int]) -> int:
    def one_pass(nums):
        result = float('-inf')
        product = 1
        for num in nums:
            product *= num
            result = max(result, product)
            if product == 0:
                product = 1
        return result

    return max(one_pass(nums), one_pass(nums[::-1]))
```

Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation:

- This solution performs two passes through the array: one forward and one backward.
- In each pass, we maintain a running product and update the maximum result seen so far.
- If we encounter a zero, we reset the product to 1.
- The key insight is that by doing both a forward and backward pass, we ensure that we capture the maximum product subarray even if it's split by an odd number of negative numbers.

Key intuitions:

- A subarray with the maximum product will either start from the left or end at the right of the array.
- By doing both passes, we cover all possible subarrays without explicitly checking all of them.
- This approach naturally handles zeros by resetting the product.

##### Sliding window with prefix and suffix products

```python
def maxProduct(nums: List[int]) -> int:
    prefix, suffix, max_so_far = 0, 0, float('-inf')
    for i in range(len(nums)):
        prefix = (prefix or 1) * nums[i]
        suffix = (suffix or 1) * nums[~i]
        max_so_far = max(max_so_far, prefix, suffix)
    return max_so_far
```

Time Complexity: O(n), where n is the length of the input array. We iterate through the array once.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation:

- This solution uses a sliding window approach, calculating prefix and suffix products simultaneously.
- We iterate through the array once, updating both prefix (from left to right) and suffix (from right to left) products.
- The `~i` notation is used to access elements from the end of the array.
- We use the `or` operator to reset the product to 1 if it becomes 0.
- At each step, we update the maximum product seen so far.

Key intuitions:

- By calculating both prefix and suffix products, we cover all possible subarrays.
- This approach efficiently handles cases where the maximum product subarray is split by an odd number of negative numbers.
- The sliding window technique allows us to consider all subarrays without explicitly generating them.

#### Rejected Approaches

1. **Brute Force**: Checking all possible subarrays would result in O(n^2) time complexity, which is inefficient for large inputs.

2. **Recursive Approach (without memoization)**: This would lead to redundant calculations and potentially exponential time complexity.

3. **Sorting-based Approach**: Sorting the array would destroy the original order, which is crucial for finding contiguous subarrays.

#### Final Recommendations

The Dynamic Programming (Kadane's Algorithm variation) approach is the most recommended solution to learn. It's efficient, intuitive, and demonstrates a clear understanding of the problem's characteristics. This approach:

1. Has optimal time (O(n)) and space (O(1)) complexity.
2. Elegantly handles both positive and negative numbers.
3. Naturally deals with zero values.
4. Demonstrates a good understanding of dynamic programming principles.

The two-pass and sliding window approaches are also worth understanding as they provide alternative perspectives on the problem and might be more intuitive for some people.

### Visualization(s)

For this problem, a visualization of how the maximum and minimum products change as we iterate through the array can be helpful. Here's a simple React component that demonstrates this for the Dynamic Programming approach:

```tsx
import React, { useState } from "react";
import { Button, Input } from "@/components/ui/button";

const MaxProductSubarrayViz = () => {
  const [nums, setNums] = useState([2, 3, -2, 4]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [maxSoFar, setMaxSoFar] = useState(nums[0]);
  const [minSoFar, setMinSoFar] = useState(nums[0]);
  const [result, setResult] = useState(nums[0]);

  const reset = () => {
    setCurrentIndex(0);
    setMaxSoFar(nums[0]);
    setMinSoFar(nums[0]);
    setResult(nums[0]);
  };

  const step = () => {
    if (currentIndex >= nums.length - 1) return;

    const i = currentIndex + 1;
    const curr = nums[i];
    const tempMax = Math.max(curr, maxSoFar * curr, minSoFar * curr);
    const tempMin = Math.min(curr, maxSoFar * curr, minSoFar * curr);

    setMaxSoFar(tempMax);
    setMinSoFar(tempMin);
    setResult(Math.max(tempMax, result));
    setCurrentIndex(i);
  };

  return (
    <div className="p-4 space-y-4">
      <div>
        <Input
          type="text"
          value={nums.join(",")}
          onChange={(e) => {
            const newNums = e.target.value.split(",").map(Number);
            setNums(newNums);
            reset();
          }}
          className="w-full"
        />
      </div>
      <div className="flex space-x-2">
        <Button onClick={reset}>Reset</Button>
        <Button onClick={step}>Step</Button>
      </div>
      <div className="space-y-2">
        <div>Current Index: {currentIndex}</div>
        <div>Max So Far: {maxSoFar}</div>
        <div>Min So Far: {minSoFar}</div>
        <div>Result: {result}</div>
      </div>
      <div className="flex">
        {nums.map((num, i) => (
          <div
            key={i}
            className={`w-10 h-10 border flex items-center justify-center ${
              i === currentIndex ? "bg-blue-200" : ""
            }`}
          >
            {num}
          </div>
        ))}
      </div>
    </div>
  );
};

export default MaxProductSubarrayViz;
```

This visualization allows users to step through the algorithm, seeing how the maximum and minimum products change at each step, and how the overall maximum product is updated. It also allows for inputting custom arrays to experiment with different scenarios.
