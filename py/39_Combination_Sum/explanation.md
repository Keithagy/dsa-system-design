# Explanation: Combination Sum

## Analysis of problem & input data

This problem is a classic backtracking problem with several key characteristics:

1. **Distinct integers**: The input array `candidates` contains distinct integers, which simplifies our solution as we don't need to handle duplicates in the input.

2. **Unlimited use of numbers**: We can use the same number from `candidates` an unlimited number of times. This is crucial for our approach, as it allows us to consider the same number multiple times in our combinations.

3. **Target sum**: We need to find all unique combinations that sum up to the target. This suggests a sum-based approach where we keep track of the current sum as we build our combinations.

4. **Unique combinations**: The order of numbers within a combination doesn't matter, but the frequency of numbers does. This hints at using a sorted approach to avoid duplicates.

5. **Constraints**: The constraints are relatively small (candidates.length <= 30, target <= 40), which suggests that a backtracking solution would be efficient enough.

The key principle that makes this question approachable is that we can build our solution incrementally, making choices at each step whether to include a number or not, and backtrack when we exceed the target sum.

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

4. All numbers can be used:

   ```python
   candidates = [1, 2, 3]
   target = 6
   # Expected output: [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 3], [2, 2, 2], [3, 3]]
   ```

5. Large numbers:

   ```python
   candidates = [8, 10, 15, 20]
   target = 40
   # Expected output: [[8, 8, 8, 8, 8], [8, 8, 8, 16], [8, 16, 16], [10, 10, 10, 10], [10, 10, 20], [10, 15, 15], [20, 20]]
   ```

Here's the executable Python code for these test cases:

```python
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    # Implementation goes here
    pass

# Test cases
test_cases = [
    ([2, 3, 6, 7], 7),
    ([2, 3, 5], 8),
    ([2], 1),
    ([1, 2, 3], 6),
    ([8, 10, 15, 20], 40)
]

for i, (candidates, target) in enumerate(test_cases, 1):
    result = combinationSum(candidates, target)
    print(f"Test case {i}:")
    print(f"Input: candidates = {candidates}, target = {target}")
    print(f"Output: {result}")
    print()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Backtracking with sorting (most optimal and elegant)
2. Dynamic Programming (bottom-up)
3. Dynamic Programming (top-down with memoization)

Count: 3 solutions

#### Rejected solutions

1. Brute Force (generating all possible combinations)
2. Greedy Approach (always choosing the largest possible candidate)

### Worthy Solutions

#### 1. Backtracking with sorting

```python
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(start: int, target: int, path: List[int]):
        if target == 0:
            # We've found a valid combination
            result.append(path[:])
            return
        if target < 0:
            # Our sum has exceeded the target, so we backtrack
            return

        for i in range(start, len(candidates)):
            # We include candidates[i] in our path
            path.append(candidates[i])
            # We continue to use candidates[i] and onwards (hence i, not i+1)
            backtrack(i, target - candidates[i], path)
            # We backtrack by removing candidates[i] from our path
            path.pop()

    result = []
    candidates.sort()  # Sort to handle candidates in ascending order
    backtrack(0, target, [])
    return result
```

Time Complexity: O(2^n), where n is the number of candidates. In the worst case, each candidate can be either included or excluded.
Space Complexity: O(target/min(candidates)), which is the maximum depth of the recursion tree.

Key intuitions and invariants:

- Sorting the candidates allows us to handle them in ascending order, which helps in pruning the search space.
- The backtracking approach builds the solution incrementally, exploring all possible combinations.
- We can reuse the same number multiple times, so we pass `i` instead of `i+1` in the recursive call.
- The base cases (target == 0 and target < 0) help us identify valid combinations and when to stop exploring.

#### 2. Dynamic Programming (bottom-up)

```python
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    # Initialize dp table: dp[i] will store all combinations that sum up to i
    dp = [[] for _ in range(target + 1)]

    # Sort candidates to ensure we build solutions in order
    candidates.sort()

    for i in range(1, target + 1):
        for num in candidates:
            # If the current number is too large, break the loop
            if num > i:
                break

            # If the current number equals i, it forms a combination by itself
            if num == i:
                dp[i].append([num])
            else:
                # Combine current number with all combinations that sum up to i-num
                for comb in dp[i - num]:
                    # Only add combinations where num is not smaller than the last element
                    # This ensures we don't generate duplicate combinations
                    if not comb or num >= comb[-1]:
                        dp[i].append(comb + [num])

    return dp[target]
```

Time Complexity: O(target \* len(candidates) \* x), where x is the average length of combinations.
Space Complexity: O(target \* y), where y is the total number of combinations.

Key intuitions and invariants:

- We build solutions for smaller targets and use them to construct solutions for larger targets.
- By sorting candidates, we can ensure we don't generate duplicate combinations.
- The condition `num >= comb[-1]` helps maintain the order and avoid duplicates.

#### 3. Dynamic Programming (top-down with memoization)

```python
from typing import List, Tuple
from functools import lru_cache

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()  # Sort candidates to ensure order

    @lru_cache(maxsize=None)
    def dp(target: int, index: int) -> List[Tuple[int, ...]]:
        if target == 0:
            return [()]
        if target < 0 or index == len(candidates):
            return []

        # Don't include the current candidate
        result = dp(target, index + 1)

        # Include the current candidate
        with_current = dp(target - candidates[index], index)
        result += tuple((candidates[index],) + comb for comb in with_current)

        return result

    # Convert tuples back to lists
    return [list(comb) for comb in dp(target, 0)]
```

Time Complexity: O(2^n), where n is the number of candidates. However, memoization can significantly reduce this in practice.
Space Complexity: O(target \* len(candidates)) for the memoization cache.

Key intuitions and invariants:

- We use memoization to avoid recomputing subproblems.
- The recursive structure allows us to make decisions about including or excluding each candidate.
- Sorting candidates helps maintain order and avoid duplicate combinations.

### Rejected Approaches

1. Brute Force: Generating all possible combinations and checking their sum would be inefficient, with a time complexity of O(2^n \* n), where n is the length of candidates.

2. Greedy Approach: Always choosing the largest possible candidate might seem intuitive, but it doesn't guarantee finding all valid combinations. For example, with candidates [2, 3, 6, 7] and target 7, a greedy approach might only find [7] and miss [2, 2, 3].

### Final Recommendations

The backtracking solution (Solution 1) is the most recommended approach for this problem in an interview setting. Here's why:

1. It's intuitive and directly solves the problem without requiring extra space beyond the recursion stack.
2. It's efficient, especially when combined with sorting to prune the search space.
3. It demonstrates a good understanding of recursion and backtracking, which are important concepts in coding interviews.
4. It's relatively easy to explain and implement compared to the dynamic programming solutions.

The dynamic programming solutions, while interesting, are more complex and might be overkill for this specific problem. They're worth knowing but might be harder to come up with and explain in an interview setting.

A common mistake to avoid is trying to use a greedy approach, which won't work for all cases. Another pitfall is forgetting to handle the case where the same number can be used multiple times, which is a key aspect of this problem.

## Visualization(s)

To visualize the backtracking process, let's consider a simple example with candidates [2, 3, 6, 7] and target 7. Here's a tree representation of the backtracking process:

```
                    []
                /   |   \   \
               2    3    6   7
             / | \  |
            2  3 6  3
           /
          2
         /
        1 (backtrack)
```

This tree shows how the algorithm explores different combinations. When it reaches a sum of 7 ([2,2,3] or [7]), it adds that combination to the result. When it exceeds 7, it backtracks. The sorting of candidates helps prune branches early (e.g., after trying 6, we don't need to try 7 in that branch).
