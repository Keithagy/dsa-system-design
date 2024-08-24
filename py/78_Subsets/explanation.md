## Explanation: Subsets

### Analysis of problem & input data

This problem is a classic combinatorial problem that falls under the category of "generating all possible combinations." The key characteristics of the input and problem are:

1. The input is an array of integers.
2. All elements in the input array are unique.
3. We need to generate all possible subsets, including the empty set and the full set.
4. The order of elements within each subset doesn't matter.
5. The order of subsets in the final result doesn't matter.

The core principle that makes this question manageable is the realization that for each element in the input array, we have two choices: include it in a subset or not. This binary choice for each element leads to 2^n possible subsets, where n is the number of elements in the input array.

This problem is well-suited for recursive backtracking or iterative bit manipulation approaches. It's also a great example of how we can build a solution incrementally, either by adding one element at a time (recursion) or by using binary representations (bit manipulation).

### Test cases

1. Empty array: `[]`
   - Expected output: `[[]]` (only the empty subset)
2. Single element: `[1]`
   - Expected output: `[[], [1]]`
3. Two elements: `[1, 2]`
   - Expected output: `[[], [1], [2], [1, 2]]`
4. Three elements (as given in the problem): `[1, 2, 3]`
   - Expected output: `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`
5. Negative numbers: `[-1, 0, 1]`
   - Expected output: `[[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]`
6. Maximum length array (edge case): `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
   - Output will have 2^10 = 1024 subsets

Here's the executable Python code for these test cases:

```python
def test_subsets(func):
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [-1, 0, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]

    for i, case in enumerate(test_cases):
        result = func(case)
        print(f"Test case {i + 1}: {case}")
        print(f"Output: {result}")
        print(f"Number of subsets: {len(result)}")
        print()

# You can call this function with your implementation, e.g.:
# test_subsets(subsets)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Recursive backtracking (DFS)
2. Iterative using bit manipulation
3. Iterative using cascading
4. Lexicographic (binary sorted) subsets

Count: 4 solutions

##### Rejected solutions

1. Brute force generation of all possible combinations
2. Dynamic programming (not necessary for this problem)

#### Worthy Solutions

##### Recursive backtracking (DFS)

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(start: int, current: List[int]):
        # Add the current subset to the result
        result.append(current[:])

        # Explore all possible elements to add to the current subset
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current.append(nums[i])
            # Recurse with the next index and updated current subset
            backtrack(i + 1, current)
            # Backtrack: remove nums[i] to explore other possibilities
            current.pop()

    result = []
    backtrack(0, [])
    return result
```

Time complexity: O(2^n), where n is the length of nums
Space complexity: O(n) for the recursion stack

Explanation:

- Time complexity: We have 2^n subsets in total (for each element, we have two choices: include it or not). The algorithm explores all these possibilities.
- Space complexity: The maximum depth of the recursion stack is n, corresponding to the longest subset (which includes all elements).

Intuitions and invariants:

- Each element has two states: included or not included in the current subset.
- The `start` parameter ensures we only consider elements after the current position, avoiding duplicates and maintaining order.
- Backtracking allows us to explore all possibilities efficiently by building subsets incrementally.
- The base case is implicit: when `start` reaches the end of the array, we stop recursing.

##### Iterative using bit manipulation

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []

    # Generate all possible bit masks from 0 to 2^n - 1
    for i in range(1 << n):  # 1 << n is equivalent to 2^n
        subset = []
        for j in range(n):
            # Check if the j-th bit is set in i
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)

    return result
```

Time complexity: O(n _2^n), where n is the length of nums
Space complexity: O(n_ 2^n) for storing all subsets

Explanation:

- Time complexity: We generate 2^n subsets, and for each subset, we perform n operations to check which elements to include.
- Space complexity: We store 2^n subsets, and each subset can have up to n elements.

Intuitions and invariants:

- Each number from 0 to 2^n - 1 represents a unique subset when viewed in binary.
- The i-th bit in the binary representation corresponds to the inclusion/exclusion of the i-th element in nums.
- This approach leverages the natural mapping between binary numbers and subset selection.

##### Iterative using cascading

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = [[]]

    for num in nums:
        # Create new subsets by adding the current number to existing subsets
        new_subsets = [subset + [num] for subset in result]
        result.extend(new_subsets)

    return result
```

Time complexity: O(n _2^n), where n is the length of nums
Space complexity: O(n_ 2^n) for storing all subsets

Explanation:

- Time complexity: For each of the n elements, we double the number of subsets, leading to 2^n total operations.
- Space complexity: We store 2^n subsets, and each subset can have up to n elements.

Intuitions and invariants:

- Start with an empty subset and iteratively build larger subsets.
- For each new element, we create new subsets by adding it to all existing subsets.
- This approach builds the solution incrementally, leveraging previously computed subsets.

##### Lexicographic (binary sorted) subsets

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)

    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(nums[j])
        result.append(subset)

    return result
```

Time complexity: O(n _2^n), where n is the length of nums
Space complexity: O(n_ 2^n) for storing all subsets

Explanation:

- Time complexity: We generate 2^n subsets, and for each subset, we perform n operations to check which elements to include.
- Space complexity: We store 2^n subsets, and each subset can have up to n elements.

Intuitions and invariants:

- This approach is similar to the bit manipulation method but generates subsets in lexicographic order.
- The binary representation of numbers from 0 to 2^n - 1 naturally maps to all possible subsets.
- By iterating through these numbers, we ensure we generate all subsets exactly once.

#### Rejected Approaches

1. Brute force generation of all possible combinations:

   - While this would work, it's inefficient and unnecessarily complex.
   - It would involve generating all possible combinations of all lengths, which is harder to implement and less efficient than the backtracking or bit manipulation approaches.

2. Dynamic programming:
   - Although this problem involves generating combinations, it doesn't have the optimal substructure property that makes dynamic programming beneficial.
   - The problem doesn't require optimization or counting, which are typical use cases for dynamic programming.
   - Using DP would unnecessarily complicate the solution without providing any benefits in terms of time or space complexity.

#### Final Recommendations

For learning and interview purposes, I recommend focusing on two approaches:

1. Recursive backtracking (DFS): This solution is intuitive, easy to explain, and demonstrates a fundamental technique in combinatorial problems. It's also a good starting point for more complex backtracking problems.

2. Iterative using bit manipulation: This solution is very efficient and showcases a clever use of bitwise operations. Understanding this approach can be beneficial for other combinatorial problems and demonstrates strong problem-solving skills.

Both of these solutions are efficient and widely applicable. The recursive approach is generally easier to come up with and explain in an interview setting, while the bit manipulation approach shows a deeper understanding of algorithmic techniques and can be impressive if explained well.

### Visualization(s)

For the recursive backtracking approach, we can visualize the process using a decision tree:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" />
    </marker>
  </defs>

  <!-- Tree structure -->
  <line x1="400" y1="50" x2="200" y2="150" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="400" y1="50" x2="600" y2="150" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>

  <line x1="200" y1="150" x2="100" y2="250" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="200" y1="150" x2="300" y2="250" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>

  <line x1="600" y1="150" x2="500" y2="250" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="600" y1="150" x2="700" y2="250" stroke="black" stroke-width="2" marker-end="url(#arrowhead)"/>

  <!-- Nodes -->
  <circle cx="400" cy="50" r="30" fill="lightblue" stroke="black" stroke-width="2"/>
  <circle cx="200" cy="150" r="30" fill="lightgreen" stroke="black" stroke-width="2"/>
  <circle cx="600" cy="150" r="30" fill="lightgreen" stroke="black" stroke-width="2"/>
  <circle cx="100" cy="250" r="30" fill="lightpink" stroke="black" stroke-width="2"/>
  <circle cx="300" cy="250" r="30" fill="lightpink" stroke="black" stroke-width="2"/>
  <circle cx="500" cy="250" r="30" fill="lightpink" stroke="black" stroke-width="2"/>
  <circle cx="700" cy="250" r="30" fill="lightpink" stroke="black" stroke-width="2"/>

  <!-- Labels -->
  <text x="400" y="55" text-anchor="middle" font-size="14">[]</text>
  <text x="200" y="155" text-anchor="middle" font-size="14">[1]</text>
  <text x="600" y="155" text-anchor="middle" font-size="14">[]</text>
  <text x="100" y="255" text-anchor="middle" font-size="14">[1,2]</text>
  <text x="300" y="255" text-anchor="middle" font-size="14">[1]</text>
  <text x="500" y="255" text-anchor="middle" font-size="14">[2]</text>
  <text x="700" y="255" text-anchor="middle" font-size="14">[]</text>

  <!-- Decision labels -->
  <text x="270" y="90" text-anchor="middle" font-size="12" fill="blue">Include 1</text>
  <text x="530" y="90" text-anchor="middle" font-size="12" fill="red">Exclude 1</text>
  <text x="120" y="190" text-anchor="middle" font-size="12" fill="blue">Include 2</text>
  <text x="280" y="190" text-anchor="middle" font-size="12" fill="red">Exclude 2</text>
  <text x="520" y="190" text-anchor="middle" font-size="12" fill="blue">Include 2</text>
  <text x="680" y="190" text-anchor="middle" font-size="12" fill="red">Exclude 2</text>

  <!-- Legend -->
  <rect x="50" y="320" width="20" height="20" fill="lightblue" stroke="black"/>
  <text x="80" y="335" font-size="12">Start</text>

  <rect x="150" y="320" width="20" height="20" fill="lightgreen" stroke="black"/>
  <text x="180" y="335" font-size="12">Intermediate</text>

  <rect x="280" y="320" width="20" height="20" fill="lightpink" stroke="black"/>
  <text x="310" y="335" font-size="12">Final subsets</text>
</svg>

```

This visualization demonstrates how the recursive backtracking approach builds subsets by making decisions to include or exclude each element. Each path from the root to a leaf represents a unique subset.
