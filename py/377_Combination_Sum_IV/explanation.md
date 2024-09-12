## Explanation: Combination Sum IV

### Analysis of problem & input data

This problem is a classic dynamic programming question that falls into the category of "counting combinations" or "coin change" problems. The key aspects to note are:

1. We're counting the number of combinations, not the combinations themselves.
2. The order of elements matters (different sequences count as different combinations).
3. Elements can be reused multiple times.
4. All numbers are positive integers.
5. The array contains distinct integers.

The fact that order matters distinguishes this problem from typical "combination sum" problems and makes it more similar to a "permutation" problem. This is crucial because it affects how we approach the solution.

The key principle that makes this question simple is the concept of subproblems in dynamic programming. We can build the solution for larger targets using solutions for smaller targets. This is because if we know the number of combinations for a smaller target, we can use that information to calculate the combinations for a larger target by adding one more number.

### Test cases

1. Basic case: `nums = [1,2,3], target = 4`
2. Single element array: `nums = [1], target = 4`
3. No solution: `nums = [5], target = 3`
4. Large target: `nums = [1,2,3], target = 32`
5. Single element solution: `nums = [3], target = 3`

```python
def test_combination_sum4(combination_sum4):
    assert combination_sum4([1,2,3], 4) == 7
    assert combination_sum4([1], 4) == 1
    assert combination_sum4([5], 3) == 0
    assert combination_sum4([1,2,3], 32) == 181997601  # Large number
    assert combination_sum4([3], 3) == 1
    print("All tests passed!")

# Run the tests
test_combination_sum4(combination_sum4)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Dynamic Programming (Bottom-up) [Neetcode solution]
2. Dynamic Programming (Top-down with memoization)
3. Mathematical Approach (Generating Function)

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force (Recursive without memoization): This approach would work but is highly inefficient for larger inputs.
2. Backtracking: While this could generate all combinations, it's overkill as we only need the count, not the actual combinations.

#### Worthy Solutions

##### Dynamic Programming (Bottom-up)

```python
from typing import List

def combination_sum4(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: one way to make sum 0 (by choosing nothing)

    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]

    return dp[target]
```

Time Complexity: O(target \* len(nums))

- We iterate through each number from 1 to target once.
- For each number, we iterate through all elements in nums.

Space Complexity: O(target)

- We use an array of size target + 1 to store intermediate results.

Explanation:

- This solution builds up the number of combinations for each sum from 0 to target.
- `dp[i]` represents the number of combinations that sum up to i.
- For each sum i, we check if we can use each number in nums to form this sum.
- If we can use a number (i.e., i >= num), we add the number of combinations that sum up to (i - num) to our current count.
- This works because if we know how many ways we can make sum (i - num), we can make sum i by adding num to each of those combinations.

Key intuitions:

- The problem has optimal substructure: solutions to larger problems can be built from solutions to smaller problems.
- The order matters, so we consider all positions for each number, which is handled implicitly by our bottom-up approach.
- We can reuse numbers, which is why we don't change the nums array as we go through the dp array.

##### Dynamic Programming (Top-down with memoization)

```python
from typing import List

def combination_sum4(nums: List[int], target: int) -> int:
    memo = {}

    def dfs(remain: int) -> int:
        if remain == 0:
            return 1
        if remain < 0:
            return 0
        if remain in memo:
            return memo[remain]

        count = 0
        for num in nums:
            count += dfs(remain - num)

        memo[remain] = count
        return count

    return dfs(target)
```

Time Complexity: O(target \* len(nums))

- In the worst case, we might need to compute the result for each value from 1 to target.
- For each value, we iterate through all numbers in nums.

Space Complexity: O(target)

- The recursion stack can go as deep as the target value.
- We also use a memo dictionary that can store up to target key-value pairs.

Explanation:

- This solution uses a top-down approach with memoization to avoid redundant calculations.
- We start from the target and recursively break it down into smaller subproblems.
- The `dfs` function returns the number of combinations that sum up to the given `remain` value.
- We use memoization (`memo` dictionary) to store and reuse results for subproblems we've already solved.

Key intuitions:

- The recursive nature of the solution naturally handles the fact that order matters and numbers can be reused.
- Memoization is crucial for efficiency, as there are many overlapping subproblems.
- The base cases (remain == 0 and remain < 0) are important for correctly counting combinations and stopping the recursion.

##### Mathematical Approach (Generating Function)

```python
from typing import List
from math import factorial

def combination_sum4(nums: List[int], target: int) -> int:
    nums.sort()

    def coefficient(n: int, k: int) -> int:
        return factorial(n) // (factorial(k) * factorial(n - k))

    def expand(index: int, remain: int) -> int:
        if remain == 0:
            return 1
        if index == len(nums) or remain < nums[index]:
            return 0

        total = 0
        for count in range(remain // nums[index] + 1):
            total += coefficient(remain - count * nums[index] + count, count) * expand(index + 1, remain - count * nums[index])

        return total

    return expand(0, target)
```

Time Complexity: O(target^(len(nums)))

- In the worst case, we might need to consider all possible combinations of counts for each number.
- The actual runtime is usually much better due to early termination in many branches.

Space Complexity: O(len(nums))

- The recursion depth is at most the length of nums.

Explanation:

- This solution uses the concept of generating functions from combinatorics.
- We consider each number in nums and determine how many times it can be used (from 0 to target // num).
- For each count, we calculate the number of ways to arrange these occurrences among the remaining slots (using the combination formula).
- We multiply this by the number of ways to form the remaining sum using the next numbers.
- The recursion builds up the full generating function expansion.

Key intuitions:

- This approach directly calculates the coefficient of x^target in the expansion of (1 + x + x^2 + ...)^(len(nums)).
- It's more mathematically sophisticated and can be more efficient for certain input distributions.
- Sorting nums allows for early termination when the current number becomes too large.

#### Rejected Approaches

1. Brute Force (Recursive without memoization):
   This approach would involve generating all possible combinations recursively. While correct, it would have a time complexity of O(n^target) where n is the length of nums, making it impractical for larger inputs.

2. Backtracking:
   A backtracking approach could generate all combinations, but it's unnecessary as we only need the count, not the actual combinations. It would be less efficient than the DP solutions.

3. BFS or DFS on a graph:
   While it's possible to model this problem as a graph where each node represents a sum and edges represent adding a number, this approach would be less intuitive and potentially less efficient than DP.

#### Final Recommendations

The Dynamic Programming (Bottom-up) solution is recommended as the best to learn for this problem. Here's why:

1. It's the most efficient in terms of both time and space complexity.
2. It's more intuitive and easier to implement compared to the top-down approach.
3. It avoids the potential stack overflow issues that could occur with the recursive approach for large targets.
4. It's a classic DP problem-solving pattern that's applicable to many similar problems.

The top-down DP approach is also worth understanding as it can be more intuitive for some people and is a good general technique. The mathematical approach, while interesting, is more complex and less generalizable to other problems, making it less suitable as a primary solution in an interview setting.

### Visualization(s)

To visualize the bottom-up DP approach, we can imagine filling a table:

```
nums = [1, 2, 3], target = 4

dp array:
Index:  0   1   2   3   4
Value: [1] [1] [2] [4] [7]

Filling process:
dp[0] = 1 (base case)
dp[1] = dp[0] = 1
dp[2] = dp[1] + dp[0] = 2
dp[3] = dp[2] + dp[1] + dp[0] = 4
dp[4] = dp[3] + dp[2] + dp[1] = 7
```

This visualization shows how we build up the solution for larger sums using the solutions for smaller sums. Each cell represents the number of ways to sum up to that index using the given numbers.
