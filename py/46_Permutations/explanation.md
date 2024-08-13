# Explanation: Permutations

## Analysis of problem & input data

This problem asks us to generate all possible permutations of a given array of distinct integers. The key aspects to consider are:

1. The input is an array of distinct integers, which simplifies our approach as we don't need to handle duplicates.
2. The length of the input array is limited (1 <= nums.length <= 6), which means the total number of permutations will be manageable (at most 6! = 720).
3. The order of the output doesn't matter, giving us flexibility in how we generate and return the permutations.
4. All integers in the input are unique, which allows us to use each number exactly once in each permutation without additional checks.

The key principle that makes this question conceptually simple is that we can build permutations recursively: for each number in the array, we can place it at the current position and then recursively generate all permutations of the remaining numbers.

### Test cases

Let's consider some test cases to cover various scenarios:

1. Standard case: `[1, 2, 3]`
   Expected output: `[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]`

2. Two elements: `[0, 1]`
   Expected output: `[[0,1], [1,0]]`

3. Single element: `[1]`
   Expected output: `[[1]]`

4. Empty array: `[]`
   Expected output: `[[]]`

5. Negative numbers: `[-1, 0, 1]`
   Expected output: `[[-1,0,1], [-1,1,0], [0,-1,1], [0,1,-1], [1,-1,0], [1,0,-1]]`

6. Maximum length: `[1, 2, 3, 4, 5, 6]`
   (Output would be all 720 permutations)

Here's the Python code for these test cases:

```python
def test_permutations(func):
    test_cases = [
        ([1, 2, 3], 6),
        ([0, 1], 2),
        ([1], 1),
        ([], 1),
        ([-1, 0, 1], 6),
        ([1, 2, 3, 4, 5, 6], 720)
    ]

    for i, (nums, expected_count) in enumerate(test_cases):
        result = func(nums)
        print(f"Test case {i + 1}:")
        print(f"Input: {nums}")
        print(f"Output length: {len(result)}, Expected length: {expected_count}")
        print(f"Is length correct? {len(result) == expected_count}")
        print(f"Are all permutations unique? {len(set(tuple(p) for p in result)) == len(result)}")
        print(f"Do all permutations have correct length? {all(len(p) == len(nums) for p in result)}")
        print()

# Usage:
# test_permutations(permute)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Backtracking (recursive)
2. Iterative approach using Heap's algorithm
3. Built-in itertools.permutations (not recommended for interviews, but worth knowing)

Count: 3 solutions

#### Rejected solutions

1. Brute force generation of all possible combinations (inefficient)
2. Dynamic programming (unnecessary complexity for this problem)

### Worthy Solutions

### 1. Backtracking (recursive)

```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(start: int):
        # Base case: if we've used all numbers, add the current permutation
        if start == len(nums):
            result.append(nums[:])
            return

        # Recursive case: try all possible numbers for the current position
        for i in range(start, len(nums)):
            # Swap the current number into position
            nums[start], nums[i] = nums[i], nums[start]

            # Recursively generate permutations for the rest of the array
            backtrack(start + 1)

            # Backtrack: undo the swap to try the next possibility
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result
```

Time Complexity: O(n!), where n is the length of the input array.
Space Complexity: O(n) for the recursion stack.

Intuition and invariants:

- We build permutations by fixing one number at a time and recursively permuting the rest.
- The `start` parameter keeps track of which position we're currently filling.
- Swapping allows us to consider each number in each position without using extra space.
- Backtracking (un-swapping) ensures we explore all possibilities.

### 2. Iterative approach using Heap's algorithm

```python
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def generate_permutations(k: int):
        if k == 1:
            # Base case: add the current permutation
            result.append(nums[:])
        else:
            # Generate permutations for k-1
            generate_permutations(k - 1)

            # Generate permutations for k by rotating the last k elements
            for i in range(k - 1):
                if k % 2 == 0:
                    nums[i], nums[k-1] = nums[k-1], nums[i]
                else:
                    nums[0], nums[k-1] = nums[k-1], nums[0]
                generate_permutations(k - 1)

    result = []
    generate_permutations(len(nums))
    return result
```

Time Complexity: O(n!), where n is the length of the input array.
Space Complexity: O(n) for the recursion stack.

Intuition and invariants:

- Heap's algorithm generates all permutations by recursively generating permutations of size k from permutations of size k-1.
- It maintains the invariant that we have all permutations of the first k-1 elements, followed by all permutations of the remaining elements.
- The algorithm switches between swapping the k-th element with each of the first k-1 elements (for odd k) and always with the first element (for even k).

### 3. Built-in itertools.permutations

```python
from typing import List
import itertools

def permute(nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))
```

Time Complexity: O(n!), where n is the length of the input array.
Space Complexity: O(n!) to store all permutations.

Intuition and invariants:

- This solution leverages Python's built-in `itertools.permutations` function, which internally uses an efficient algorithm to generate all permutations.
- While this is the simplest solution, it's generally not recommended in interview settings as it doesn't demonstrate understanding of the underlying algorithm.

### Rejected Approaches

1. Brute force generation:

   - Generating all possible combinations and then filtering for valid permutations would be inefficient, with a time complexity worse than O(n!).
   - This approach doesn't leverage the problem's structure and would involve unnecessary computations.

2. Dynamic programming:
   - While DP can be powerful for many combinatorial problems, it's not well-suited for generating permutations.
   - Permutations don't have the optimal substructure property that DP typically exploits.
   - The space complexity for storing all subproblems would be excessive compared to more direct methods.

### Final Recommendations

For a coding interview, I recommend learning and implementing the backtracking solution (Solution 1). Here's why:

1. It demonstrates a clear understanding of the problem and how to generate permutations efficiently.
2. The recursive approach with backtracking is a fundamental technique that can be applied to many other problems.
3. It has optimal time complexity (O(n!)) and good space efficiency (O(n) excluding the output).
4. The implementation is concise yet clearly shows the thought process.

The iterative Heap's algorithm (Solution 2) is also worth understanding, as it provides an alternative perspective on generating permutations and can be useful in scenarios where recursion is problematic.

The built-in `itertools.permutations` solution, while correct, is not recommended for interviews as it doesn't demonstrate your problem-solving skills or understanding of the underlying algorithm.

Avoid the brute force approach, as it's inefficient and doesn't leverage the problem's structure. Similarly, dynamic programming is unnecessarily complex for this problem and doesn't offer any advantages over the recommended solutions.

## Visualization(s)

To visualize the backtracking process, let's consider a small example with the input `[1, 2, 3]`:

```
                    [1, 2, 3]
                   /    |    \
            [1, 2, 3] [2, 1, 3] [3, 2, 1]
             /     \    /    \    /    \
        [1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 2, 1] [3, 1, 2]
```

This tree represents the recursion process:

1. At the root, we have the initial array.
2. At each level, we fix one more position (shown by the bold number).
3. Leaves represent complete permutations.
4. Backtracking occurs when we move back up the tree to explore other branches.

This visualization helps to understand how the algorithm systematically explores all possibilities while using the input array itself to store intermediate states.
