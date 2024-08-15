# Explanation: Partition Equal Subset Sum

## Analysis of problem & input data

This problem is a variation of the classic subset sum problem, which is NP-complete. The key insight is that if we can partition the array into two subsets with equal sums, then each subset must have a sum equal to half of the total sum of the array.

Key characteristics:

1. The problem can be reduced to finding a subset with a sum equal to half of the total sum.
2. We're dealing with positive integers, which simplifies our approach.
3. The constraint on array length (<=200) and element values (<=100) suggests that a dynamic programming approach might be feasible.
4. The total sum of the array must be even for a valid partition to exist.

The principle that makes this question tractable is that we can build up our solution incrementally, considering one element at a time and determining if we can achieve various sum values up to our target sum.

## Test cases

1. Basic cases:

   - `[1,5,11,5]` -> `True` (partitions: [1,5,5] and [11])
   - `[1,2,3,5]` -> `False` (no valid partition)

2. Edge cases:

   - `[1]` -> `False` (single element, can't be partitioned)
   - `[1,1]` -> `True` (equal elements)
   - `[100,100,100,100]` -> `True` (multiple equal elements)

3. Challenging inputs:
   - `[1,2,3,4,5,6,7]` -> `True` (multiple ways to partition)
   - `[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,99]` -> `False` (large number of small values and one large value)

Here's the Python code for these test cases:

```python
def test_can_partition(can_partition_func):
    test_cases = [
        ([1,5,11,5], True),
        ([1,2,3,5], False),
        ([1], False),
        ([1,1], True),
        ([100,100,100,100], True),
        ([1,2,3,4,5,6,7], True),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,99], False)
    ]

    for nums, expected in test_cases:
        result = can_partition_func(nums)
        assert result == expected, f"Failed for input {nums}. Expected {expected}, got {result}"

    print("All test cases passed!")

# Usage:
# test_can_partition(your_can_partition_function)
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Dynamic Programming (Bottom-Up, 2D array)
2. Dynamic Programming (Bottom-Up, 1D array)
3. Dynamic Programming (Top-Down with Memoization)
4. Bit Manipulation

Number of solutions: 4

#### Rejected solutions

1. Brute Force (generate all subsets)
2. Greedy Approach
3. Sorting and Two Pointers

### Worthy Solutions

#### 1. Dynamic Programming (Bottom-Up, 2D array)

```python
from typing import List

def can_partition(nums: List[int]) -> bool:
    total_sum = sum(nums)

    # If the total sum is odd, it can't be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(nums)

    # dp[i][j] represents whether it's possible to achieve sum j using first i elements
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: it's always possible to achieve sum 0 with any number of elements
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if j < nums[i-1]:
                # If current sum is less than the number, we can't include it
                dp[i][j] = dp[i-1][j]
            else:
                # We have two choices: include the number or exclude it
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

    return dp[n][target_sum]
```

Time Complexity: O(n \* target_sum), where n is the length of nums.
Space Complexity: O(n \* target_sum)

Intuitions and invariants:

- We build a 2D table where dp[i][j] represents whether it's possible to achieve sum j using the first i elements.
- For each element, we have two choices: include it or exclude it.
- We leverage the solutions to smaller subproblems to solve larger ones.

#### 2. Dynamic Programming (Bottom-Up, 1D array)

```python
from typing import List

def can_partition(nums: List[int]) -> bool:
    total_sum = sum(nums)

    # If the total sum is odd, it can't be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2

    # dp[j] represents whether it's possible to achieve sum j
    dp = [False] * (target_sum + 1)
    dp[0] = True  # Base case: it's always possible to achieve sum 0

    for num in nums:
        # Iterate backwards to avoid using the same number multiple times
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target_sum]
```

Time Complexity: O(n \* target_sum), where n is the length of nums.
Space Complexity: O(target_sum)

Intuitions and invariants:

- We optimize the space usage by using only a 1D array.
- The backward iteration prevents us from using the same number multiple times in a single iteration.
- Each position in the dp array represents a possible sum we can achieve.

#### 3. Dynamic Programming (Top-Down with Memoization)

```python
from typing import List

def can_partition(nums: List[int]) -> bool:
    total_sum = sum(nums)

    # If the total sum is odd, it can't be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    memo = {}  # Memoization hash map

    def dfs(index: int, current_sum: int) -> bool:
        # Base cases
        if current_sum == target_sum:
            return True
        if index >= len(nums) or current_sum > target_sum:
            return False

        # Check memoization
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]

        # Recursive cases: include or exclude current number
        result = dfs(index + 1, current_sum + nums[index]) or dfs(index + 1, current_sum)

        # Memoize result
        memo[(index, current_sum)] = result
        return result

    return dfs(0, 0)
```

Time Complexity: O(n \* target_sum), where n is the length of nums.
Space Complexity: O(n \* target_sum) due to memoization and recursion stack.

Intuitions and invariants:

- We use depth-first search to explore all possible combinations.
- Memoization prevents redundant computations by storing results of subproblems.
- The recursive structure naturally handles the decision to include or exclude each number.

#### 4. Bit Manipulation

```python
from typing import List

def can_partition(nums: List[int]) -> bool:
    total_sum = sum(nums)

    # If the total sum is odd, it can't be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    dp = 1  # Binary representation of possible sums, initially only 0 is possible

    for num in nums:
        dp |= dp << num  # Shift and OR to add new possible sums

    return dp & (1 << target_sum) != 0  # Check if target_sum is achievable
```

Time Complexity: O(n \* max(nums)), where n is the length of nums.
Space Complexity: O(1) as we use a single integer for dp.

Intuitions and invariants:

- We represent all possible sums as bits in an integer.
- Each bit shift represents adding a new number to our existing sums.
- The final check determines if the target sum is among the achievable sums.

### Rejected Approaches

1. Brute Force (generate all subsets):

   - Time complexity: O(2^n)
   - Reason: Exponential time complexity makes it impractical for larger inputs.

2. Greedy Approach:

   - Reason: This problem requires considering all possible combinations, which a greedy approach can't guarantee.

3. Sorting and Two Pointers:
   - Reason: While sorting can help in some subset sum problems, it doesn't provide a clear advantage here as we need to consider all combinations.

### Final Recommendations

The Dynamic Programming approach with a 1D array (Solution 2) is the best one to learn for this problem. It offers an optimal balance between time and space complexity, and it's conceptually straightforward once you understand the underlying principle.

The Bit Manipulation approach (Solution 4) is very clever and space-efficient, but it might be harder to come up with in an interview setting and could be less intuitive to explain.

The Top-Down DP with Memoization (Solution 3) is also worth understanding as it demonstrates how to apply memoization to recursive solutions, a technique applicable to many other problems.

The 2D DP solution (Solution 1) is correct but uses more space than necessary. It's a good starting point for understanding the problem, but the 1D version should be preferred in practice.

Approaches that might seem correct but aren't include:

1. Sorting the array and trying to build two equal subsets from the largest elements down. This fails because it doesn't consider all possible combinations.
2. Using a greedy approach that tries to balance two subsets by always adding the current element to the smaller subset. This can fail for inputs like [1,2,5].

## Visualization(s)

For the Dynamic Programming approach (1D array), we can visualize the dp array as it's being filled:

```
nums = [1,5,11,5]
target_sum = 11

Initial dp: [T, F, F, F, F, F, F, F, F, F, F, F]
After 1:    [T, T, F, F, F, F, F, F, F, F, F, F]
After 5:    [T, T, F, F, F, T, T, F, F, F, F, F]
After 11:   [T, T, F, F, F, T, T, F, F, F, F, T]
After 5:    [T, T, F, F, F, T, T, F, F, F, T, T]

Final dp:   [T, T, F, F, F, T, T, F, F, F, T, T]
```

This visualization shows how the possible sums are built up as we process each number in the input array. The final 'T' at index 11 indicates that it's possible to create a subset with sum 11, which is half of the total sum, confirming that the array can be partitioned into two equal subsets.
