## Explanation: Majority Element

### Analysis of problem & input data

This problem is about finding the majority element in an array, which is defined as an element that appears more than ⌊n / 2⌋ times, where n is the length of the array. The key aspects of this problem are:

1. The majority element is guaranteed to exist in the array.
2. The array size can be quite large (up to 5 \* 10^4).
3. The elements can be any integer within a large range (-10^9 to 10^9).

The characteristics of this problem make it suitable for several algorithmic approaches. The key principle that makes this question simple is the fact that the majority element appears more than half the time. This property allows for efficient solutions that don't necessarily require sorting or counting all elements.

Pattern-matching to solution strategies:

1. Voting algorithms (Boyer-Moore Voting Algorithm)
2. Divide and Conquer
3. Bit manipulation (for constant space)
4. Sorting-based approach
5. Counting-based approach (hash map)

The follow-up question asking for a linear time and constant space solution narrows down the optimal approach to the Boyer-Moore Voting Algorithm or a bit manipulation technique.

### Test cases

1. Basic case: `[3, 2, 3]` (odd length)
2. Larger case: `[2, 2, 1, 1, 1, 2, 2]` (even length)
3. All elements are the same: `[1, 1, 1, 1]`
4. Minimum array length: `[5]`
5. Majority element at the beginning: `[7, 7, 7, 7, 1, 2, 3]`
6. Majority element at the end: `[1, 2, 3, 7, 7, 7, 7]`
7. Large numbers: `[1000000000, -1000000000, 1000000000]`

Here's the Python code for these test cases:

```python
def test_majority_element(func):
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [1, 1, 1, 1],
        [5],
        [7, 7, 7, 7, 1, 2, 3],
        [1, 2, 3, 7, 7, 7, 7],
        [1000000000, -1000000000, 1000000000]
    ]

    for i, case in enumerate(test_cases):
        result = func(case)
        print(f"Test case {i + 1}: {case}")
        print(f"Result: {result}\n")

# Example usage:
# test_majority_element(majority_element)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Boyer-Moore Voting Algorithm (optimal time and space)
2. Bit Manipulation (optimal space, but potentially slower for large integers)
3. Divide and Conquer (good for understanding recursive approaches)
4. Sorting (simple to implement and understand)
5. Hash Map Counting (intuitive but not optimal space)

Total count: 5 solutions

##### Rejected solutions

1. Brute Force (checking each element against all others)
2. Randomized Selection (while it can work, it's not guaranteed to be O(n) in the worst case)

#### Worthy Solutions

##### Boyer-Moore Voting Algorithm

```python
def majority_element(nums: List[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
```

Runtime complexity: O(n)
Space complexity: O(1)

- Intuition:
  - The majority element appears more than n/2 times, so it will always "outvote" the other elements.
  - We can pair off different elements, and the majority element will always remain.
- Invariants:
  - If count becomes 0, we've seen an equal number of the candidate and other elements.
  - The majority element will always survive the pairing process.

##### Bit Manipulation (with bitwise NOT for negative numbers)

```python
def majority_element(nums: List[int]) -> int:
    n = len(nums)
    majority = 0

    for bit in range(32):  # Assuming 32-bit integers
        bit_count = sum((num >> bit) & 1 for num in nums)
        if bit_count > n // 2:
            majority |= (1 << bit)

    # Handle the case where the majority element is negative
    if majority > 2**31 - 1:
        majority = ~majority + 1

    return majority
```

Runtime complexity: O(32n) = O(n)
Space complexity: O(1)

- Intuition:
  - The majority element's bits will be the majority bits in each position.
  - We can construct the majority element by checking each bit position.
  - For negative numbers, we use the two's complement conversion formula directly.
- Invariants:
  - For each bit position, if the majority element has a 1, more than half of the numbers will have a 1 in that position.
  - The final constructed number will be the majority element.
  - If the constructed number is greater than 2^31 - 1, it represents a negative number in two's complement form.

This approach demonstrates a deep understanding of binary representations and two's complement arithmetic, which could be particularly impressive in interviews focusing on low-level operations or embedded systems programming.

##### Divide and Conquer

```python
def majority_element(nums: List[int]) -> int:
    def majority_element_rec(lo: int, hi: int) -> int:
        # Base case: the only element in an array of size 1 is the majority element
        if lo == hi:
            return nums[lo]

        # Divide the array into two halves
        mid = (hi - lo) // 2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid + 1, hi)

        # If the two halves agree on the majority element, return it
        if left == right:
            return left

        # Otherwise, count each element and return the winner
        left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums) - 1)
```

Runtime complexity: O(n log n)
Space complexity: O(log n) due to the recursion stack

- Intuition:
  - The majority element in the whole array must be the majority element in at least one of its halves.
  - We can recursively find the majority element in each half and then determine which one is the overall majority.
- Invariants:
  - The majority element in a subarray is always a candidate for the majority element in the entire array.
  - The base case (single element) is always the majority element of itself.

##### Sorting

```python
def majority_element(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]
```

Runtime complexity: O(n log n)
Space complexity: O(1) or O(n) depending on the sorting algorithm

- Intuition:
  - After sorting, the majority element will always be at the middle index.
  - This is because the majority element appears more than n/2 times.
- Invariants:
  - The element at index n//2 in a sorted array containing a majority element is always the majority element.

##### Hash Map Counting

```python
from collections import Counter

def majority_element(nums: List[int]) -> int:
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)
```

Runtime complexity: O(n)
Space complexity: O(n)

- Intuition:
  - Count the occurrences of each element and return the one with the highest count.
  - The majority element will always have the highest count.
- Invariants:
  - The element with the highest count in the hash map is the majority element.

#### Rejected Approaches

1. Brute Force: Checking each element against all others (O(n^2) time complexity) is inefficient and not worth learning for this problem.

2. Randomized Selection: While this approach can work and has an expected O(n) time complexity, it's not guaranteed to be O(n) in the worst case. It's also more complex to implement and understand compared to the Boyer-Moore Voting Algorithm.

#### Final Recommendations

The Boyer-Moore Voting Algorithm is the best solution to learn for this problem. It achieves linear time complexity and constant space complexity, meeting the follow-up challenge. It's also elegant and demonstrates a deep understanding of the problem's properties. The Bit Manipulation approach is also worth understanding as an alternative constant-space solution, especially for interviews where bit manipulation skills are valued.

### Visualization(s)

To visualize the Boyer-Moore Voting Algorithm, we can use a simple React component that shows the process step by step:

```tsx
import React, { useState } from "react";
import { Button } from "@/components/ui/button";

const BoyerMooreVisualization = () => {
  const [nums] = useState([2, 2, 1, 1, 1, 2, 2]);
  const [step, setStep] = useState(0);
  const [candidate, setCandidate] = useState(null);
  const [count, setCount] = useState(0);

  const nextStep = () => {
    if (step < nums.length) {
      const num = nums[step];
      if (count === 0) {
        setCandidate(num);
        setCount(1);
      } else {
        setCount(count + (num === candidate ? 1 : -1));
      }
      setStep(step + 1);
    }
  };

  const reset = () => {
    setStep(0);
    setCandidate(null);
    setCount(0);
  };

  return (
    <div className="p-4 bg-gray-100 rounded-lg">
      <h2 className="text-xl font-bold mb-4">Boyer-Moore Voting Algorithm</h2>
      <div className="mb-4">
        <span className="font-semibold">Array: </span>
        {nums.map((num, i) => (
          <span
            key={i}
            className={`px-2 py-1 m-1 ${i < step ? "bg-green-200" : "bg-gray-200"} rounded`}
          >
            {num}
          </span>
        ))}
      </div>
      <div className="mb-4">
        <span className="font-semibold">Current candidate: </span>
        <span className="px-2 py-1 bg-blue-200 rounded">
          {candidate !== null ? candidate : "None"}
        </span>
      </div>
      <div className="mb-4">
        <span className="font-semibold">Count: </span>
        <span className="px-2 py-1 bg-yellow-200 rounded">{count}</span>
      </div>
      <Button onClick={nextStep} disabled={step >= nums.length}>
        Next Step
      </Button>
      <Button onClick={reset} className="ml-2">
        Reset
      </Button>
    </div>
  );
};

export default BoyerMooreVisualization;
```

This visualization helps to understand how the Boyer-Moore Voting Algorithm works by showing the process step by step, updating the candidate and count as it goes through the array.
