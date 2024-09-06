## Explanation: Random Pick with Weight

### Analysis of problem & input data

This problem is about implementing a weighted random selection algorithm. The key characteristics of this problem are:

1. We have an array of weights, where each weight corresponds to an index.
2. We need to randomly select an index, but the probability of selecting each index is proportional to its weight.
3. The selection needs to be done efficiently, as it will be called multiple times.

The crucial insight here is that this problem can be transformed into a problem of selecting a random number from a range and then finding where that number falls in a cumulative sum array. This transformation allows us to use efficient data structures and algorithms for the implementation.

Key principles that make this question simple:

1. The cumulative sum array allows us to map a uniformly distributed random number to a weighted random selection.
2. Binary search can be used to efficiently find where a number falls in a sorted array.

### Test cases

1. Edge case: Single element array
   Input: `w = [1]`
   Expected: Always returns 0

2. Two elements with different weights
   Input: `w = [1, 3]`
   Expected: Returns 0 about 25% of the time, 1 about 75% of the time

3. Multiple elements with equal weights
   Input: `w = [1, 1, 1, 1]`
   Expected: Each index should be returned with approximately equal probability

4. Large range of weights
   Input: `w = [1, 10, 100, 1000]`
   Expected: Higher indices should be returned more frequently

5. Maximum constraints
   Input: `w = [10^5] * 10^4` # An array of 10^4 elements, each with weight 10^5
   Expected: Should handle this case efficiently

Here's the Python code for these test cases:

```python
import random

class Solution:
    def __init__(self, w: List[int]):
        self.cumsum = list(itertools.accumulate(w))
        self.total_sum = self.cumsum[-1]

    def pickIndex(self) -> int:
        target = random.random() * self.total_sum
        return bisect.bisect_left(self.cumsum, target)

# Test cases
def run_tests():
    # Test case 1: Single element array
    sol1 = Solution([1])
    assert sol1.pickIndex() == 0, "Test case 1 failed"

    # Test case 2: Two elements with different weights
    sol2 = Solution([1, 3])
    results = [sol2.pickIndex() for _ in range(10000)]
    assert 0.2 < results.count(0) / 10000 < 0.3, "Test case 2 failed"

    # Test case 3: Multiple elements with equal weights
    sol3 = Solution([1, 1, 1, 1])
    results = [sol3.pickIndex() for _ in range(10000)]
    for i in range(4):
        assert 0.2 < results.count(i) / 10000 < 0.3, f"Test case 3 failed for index {i}"

    # Test case 4: Large range of weights
    sol4 = Solution([1, 10, 100, 1000])
    results = [sol4.pickIndex() for _ in range(10000)]
    assert results.count(3) > results.count(2) > results.count(1) > results.count(0), "Test case 4 failed"

    # Test case 5: Maximum constraints
    sol5 = Solution([10**5] * 10**4)
    assert 0 <= sol5.pickIndex() < 10**4, "Test case 5 failed"

    print("All test cases passed!")

run_tests()
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Cumulative Sum + Binary Search (Neetcode solution)
2. Cumulative Sum + Linear Search
3. Reservoir Sampling

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Naive approach: Creating an array with repeated elements based on weights
2. Using a balanced tree structure (e.g., AVL tree or Red-Black tree)

#### Worthy Solutions

##### Cumulative Sum + Binary Search (Neetcode solution)

```python
import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        # Calculate the cumulative sum array
        self.cumsum = list(itertools.accumulate(w))
        # Store the total sum for efficient random number generation
        self.total_sum = self.cumsum[-1]

    def pickIndex(self) -> int:
        # Generate a random number in the range [0, total_sum)
        target = random.random() * self.total_sum
        # Use binary search to find the index where target would be inserted
        return bisect.bisect_left(self.cumsum, target)
```

Time Complexity:

- Initialization: O(n), where n is the length of the input array w. This is because we need to iterate through the array once to calculate the cumulative sum.
- pickIndex: O(log n) for each call, as we're using binary search on the cumulative sum array.

Space Complexity: O(n) to store the cumulative sum array.

Intuition and invariants:

- The cumulative sum array transforms the problem from weighted random selection to finding where a random number falls in a range.
- The probability of selecting each index is proportional to its weight because the size of each "slice" in the cumulative sum array is proportional to the weight.
- Binary search allows for efficient lookup in the sorted cumulative sum array.

##### Cumulative Sum + Linear Search

```python
import random

class Solution:
    def __init__(self, w: List[int]):
        # Calculate the cumulative sum array
        self.cumsum = list(itertools.accumulate(w))
        # Store the total sum for efficient random number generation
        self.total_sum = self.cumsum[-1]

    def pickIndex(self) -> int:
        # Generate a random number in the range [0, total_sum)
        target = random.random() * self.total_sum
        # Use linear search to find the first index where cumsum exceeds target
        for i, cum_weight in enumerate(self.cumsum):
            if target < cum_weight:
                return i
```

Time Complexity:

- Initialization: O(n), where n is the length of the input array w, to calculate the cumulative sum.
- pickIndex: O(n) for each call, as we might need to iterate through the entire cumulative sum array in the worst case.

Space Complexity: O(n) to store the cumulative sum array.

Intuition and invariants:

- This approach uses the same cumulative sum concept as the binary search solution.
- The linear search is simpler to implement but less efficient for large arrays.
- This method can be more efficient for very small arrays where the overhead of binary search might outweigh its benefits.

##### Reservoir Sampling

```python
import random

class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.total_weight = sum(w)

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_weight)
        current_sum = 0
        for i, weight in enumerate(self.w):
            current_sum += weight
            if current_sum >= target:
                return i
```

Time Complexity:

- Initialization: O(n) to calculate the total weight.
- pickIndex: O(n) for each call, as we might need to iterate through the entire weight array in the worst case.

Space Complexity: O(1) additional space, as we're using the input array directly.

Intuition and invariants:

- This approach is based on the concept of reservoir sampling, adapted for weighted random selection.
- It simulates drawing a random number from the total weight and finding which weight "bucket" it falls into.
- This method doesn't require preprocessing, which can be advantageous if the weights change frequently.

#### Rejected Approaches

1. Naive approach: Creating an array with repeated elements based on weights

   - This approach would involve creating a new array where each index is repeated according to its weight.
   - Rejected because: It's extremely space-inefficient, especially for large weights. The space complexity would be O(sum(w)), which could be much larger than O(n).

2. Using a balanced tree structure (e.g., AVL tree or Red-Black tree)
   - This approach would involve creating a balanced tree where each node represents a weight range.
   - Rejected because: While it would provide O(log n) time complexity for pickIndex, it's overly complex for this problem. The initialization would be O(n log n), which is worse than the O(n) of the cumulative sum approach.

#### Final Recommendations

The Cumulative Sum + Binary Search approach (Neetcode solution) is the best to learn and use for this problem. Here's why:

1. Efficiency: It provides O(log n) time complexity for pickIndex operations, which is optimal for large datasets.
2. Space efficiency: It uses O(n) space, which is the minimum required to preprocess the weights for efficient selection.
3. Simplicity: Despite using binary search, the implementation is relatively straightforward and easy to understand.
4. Scalability: This approach works well for both small and large datasets.

The other approaches, while valid, have drawbacks:

- Linear search is less efficient for large datasets.
- Reservoir sampling, while space-efficient, is less time-efficient for pickIndex operations.

Therefore, mastering the Cumulative Sum + Binary Search approach will provide the best balance of efficiency, simplicity, and applicability to various scenarios you might encounter in coding interviews.

### Visualization(s)

To visualize the Cumulative Sum + Binary Search approach, we can create a simple React component that demonstrates the process:

```tsx
import React, { useState } from "react";

const WeightedRandomPick = () => {
  const [weights, setWeights] = useState([1, 3, 2, 4]);
  const [selectedIndex, setSelectedIndex] = useState(null);

  const cumsum = weights.reduce(
    (acc, w, i) => [...acc, (acc[i - 1] || 0) + w],
    [],
  );
  const totalSum = cumsum[cumsum.length - 1];

  const pickIndex = () => {
    const target = Math.random() * totalSum;
    const index = cumsum.findIndex((sum) => sum > target);
    setSelectedIndex(index);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">
        Weighted Random Pick Visualization
      </h2>
      <div className="flex mb-4">
        {weights.map((weight, index) => (
          <div
            key={index}
            className={`h-20 flex items-end justify-center ${index === selectedIndex ? "bg-blue-500" : "bg-gray-300"}`}
            style={{ width: `${(weight / totalSum) * 100}%` }}
          >
            <span className="mb-2">{weight}</span>
          </div>
        ))}
      </div>
      <button
        onClick={pickIndex}
        className="bg-green-500 text-white px-4 py-2 rounded"
      >
        Pick Index
      </button>
      {selectedIndex !== null && (
        <p className="mt-4">Selected Index: {selectedIndex}</p>
      )}
    </div>
  );
};

export default WeightedRandomPick;
```

This visualization represents each weight as a bar, with the width proportional to its weight. When you click "Pick Index", it simulates the random selection process and highlights the selected bar. This helps to visually understand how the probability of selection is proportional to the weight of each item.
