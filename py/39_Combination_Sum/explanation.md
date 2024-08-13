# Explanation: Combination Sum

## Analysis of problem & input data

This problem is a classic example of a combination search problem with the following key characteristics:

1. Unbounded Knapsack-like problem: We can use each number in the candidates array an unlimited number of times.
2. Distinct integers: All elements in the candidates array are unique.
3. Sum to target: We need to find all combinations that sum up exactly to the target.
4. Unique combinations: The output should not contain duplicate combinations.
5. Order doesn't matter: We can return the combinations in any order.

Key principles that make this problem solvable:

1. Recursive nature: We can build combinations by repeatedly choosing or not choosing each candidate.
2. Backtracking: We can use backtracking to explore all possible combinations efficiently.
3. Sorting can optimize: Although not necessary, sorting the candidates can help prune the search space early.

The constraints (1 <= candidates.length <= 30, 2 <= candidates[i] <= 40, 1 <= target <= 40) suggest that a brute force approach might be feasible, but more efficient solutions exist.

### Test cases

Here are some test cases to consider:

1. Basic case:

   ```python
   candidates = [2, 3, 6, 7]
   target = 7
   # Expected output: [[2, 2, 3], [7]]
   ```

2. Multiple solutions:

   ```python
   candidates = [2, 3, 5]
   target = 8
   # Expected output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
   ```

3. No solution:

   ```python
   candidates = [2]
   target = 1
   # Expected output: []
   ```

4. All candidates can be used:

   ```python
   candidates = [1, 2, 3]
   target = 6
   # Expected output: [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 3], [2, 2, 2], [3, 3]]
   ```

5. Large target, small candidates:

   ```python
   candidates = [2, 3]
   target = 20
   # Expected output: [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 3, 3], [2, 2, 2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3]]
   ```

Here's the executable Python code for these test cases:

```python
def combination_sum(candidates, target):
    # Implementation will be added later
    pass

test_cases = [
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
    ([2], 1),
    ([1, 2, 3], 6),
    ([2, 3], 20)
]

for i, (candidates, target) in enumerate(test_cases, 1):
    print(f"Test case {i}:")
    print(f"Candidates: {candidates}")
    print(f"Target: {target}")
    result = combination_sum(candidates, target)
    print(f"Result: {result}")
    print()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Backtracking (DFS) with sorting
2. Dynamic Programming (Bottom-up)
3. Dynamic Programming (Top-down with memoization)

Count: 3 solutions

#### Rejected solutions

1. Brute Force (generating all possible combinations)
2. BFS (Breadth-First Search)
3. Bitmask approach

### Worthy Solutions

#### 1. Backtracking (DFS) with sorting

```python
from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(start: int, target: int, path: List[int]):
        if target == 0:
            # We've found a valid combination
            result.append(path[:])
            return
        if target < 0:
            # Our combination exceeds the target, so we stop exploring this path
            return

        for i in range(start, len(candidates)):
            # We can use the same number multiple times, so we don't increment 'i'
            # We reduce the target by the current candidate
            backtrack(i, target - candidates[i], path + [candidates[i]])

    candidates.sort()  # Sorting helps to prune the search space
    result = []
    backtrack(0, target, [])
    return result
```

Time Complexity: O(2^target), where target is the target sum. In the worst case, we have a candidate of 1 and we need to generate all combinations.
Space Complexity: O(target/min(candidates)) for the recursion stack.

Intuitions and invariants:

- Sorting the candidates allows us to break early if a candidate is larger than the remaining target.
- We can reuse the same number, so we don't increment the start index in the recursive call.
- The path parameter keeps track of the current combination being built.
- We use backtracking to explore all possible combinations efficiently.

#### 2. Dynamic Programming (Bottom-up)

```python
from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # dp[i] will store all combinations that sum up to i
    dp = [[] for _ in range(target + 1)]

    for c in candidates:
        for i in range(c, target + 1):
            # If i == c, we can form a combination with just this candidate
            if i == c:
                dp[i].append([c])
            # For i > c, we can append this candidate to all combinations that sum up to i-c
            for comb in dp[i - c]:
                dp[i].append(comb + [c])

    return dp[target]
```

Time Complexity: O(target _len(candidates)_ average_combination_length)
Space Complexity: O(target \* number_of_combinations)

Intuitions and invariants:

- We build up solutions for smaller targets to construct solutions for larger targets.
- For each candidate and each possible sum, we consider whether adding this candidate can form new combinations.
- The final answer is stored in dp[target].

#### 3. Dynamic Programming (Top-down with memoization)

```python
from typing import List, Dict, Tuple

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    memo: Dict[Tuple[int, int], List[List[int]]] = {}

    def dfs(start: int, target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if start == len(candidates) or target < 0:
            return []

        if (start, target) in memo:
            return memo[(start, target)]

        result = []

        # Include the current candidate
        for comb in dfs(start, target - candidates[start]):
            result.append([candidates[start]] + comb)

        # Exclude the current candidate
        result.extend(dfs(start + 1, target))

        memo[(start, target)] = result
        return result

    return dfs(0, target)
```

Time Complexity: O(2^N _T), where N is the number of candidates and T is the target.
Space Complexity: O(N_ T) for the memoization dictionary and recursion stack.

Intuitions and invariants:

- We use memoization to avoid redundant computations.
- At each step, we have two choices: include the current candidate or exclude it.
- The base cases are when we reach the target (return an empty combination) or when we've exhausted all candidates or exceeded the target (return no combinations).

### Rejected Approaches

1. Brute Force: Generating all possible combinations would be extremely inefficient, with a time complexity of O(2^N \* N), where N is the length of candidates.

2. BFS (Breadth-First Search): While BFS could work, it would be less efficient than DFS for this problem. BFS would require more memory to store all partial combinations at each level.

3. Bitmask approach: This would not work efficiently because we can use each number multiple times, which is not easily representable with bitmasks.

### Final Recommendations

The backtracking (DFS) approach with sorting is the recommended solution for this problem in an interview setting. It's intuitive, efficient, and demonstrates a good understanding of recursion and backtracking.

The dynamic programming solutions, while interesting, are generally overkill for this problem and may be harder to come up with and implement correctly under interview pressure.

The key insights to communicate are:

1. The ability to reuse numbers leads to a recursive/backtracking approach.
2. Sorting can optimize the search process.
3. Building combinations incrementally allows us to stop early when we exceed the target.

Remember to discuss the time and space complexity, and be prepared to optimize the solution (e.g., by sorting the candidates to enable early termination).

## Visualization(s)

To visualize the backtracking process, we can use a tree structure:

```
                   []
                 /  |  \
               [2] [3] [6] [7]
              /  |  \
          [2,2][2,3][2,6][2,7]
           /   |
      [2,2,2][2,2,3]
       /
  [2,2,2,2]
```

This tree represents the exploration process for the input `[2,3,6,7]` with target 7. Each node represents a partial combination, and we explore deeper until we either reach the target or exceed it.
