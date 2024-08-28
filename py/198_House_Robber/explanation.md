## Explanation: House Robber

### Analysis of problem & input data

This problem is a classic example of dynamic programming. The key characteristics that make it suitable for a DP approach are:

1. Optimal substructure: The optimal solution can be constructed from optimal solutions of its subproblems.
2. Overlapping subproblems: The same subproblems are solved multiple times when using a naive recursive approach.

The constraint of not being able to rob adjacent houses creates a dependency between decisions, making it a perfect candidate for dynamic programming. The problem can be broken down into smaller subproblems, where at each house, we have two choices:

1. Rob the current house and skip the previous one.
2. Skip the current house and take the maximum amount from the previous decision.

The key principle that makes this question simple is the realization that for any house i, the maximum amount we can rob is the maximum of:

1. The amount in the current house plus the maximum amount we could rob from houses 0 to i-2
2. The maximum amount we could rob from houses 0 to i-1 (skipping the current house)

This creates a recurrence relation that forms the basis of our dynamic programming solution.

### Test cases

1. Edge case: Single house
   Input: [5]
   Expected Output: 5

2. Edge case: Two houses
   Input: [3,1]
   Expected Output: 3

3. Typical case: Alternating pattern
   Input: [2,7,9,3,1]
   Expected Output: 12

4. Challenging case: Non-obvious optimal solution
   Input: [2,1,1,2]
   Expected Output: 4

5. Edge case: All zeros
   Input: [0,0,0,0]
   Expected Output: 0

6. Larger input
   Input: [6,3,10,8,2,10,3,5,10,5,3]
   Expected Output: 39

Here's the executable Python code for these test cases:

```python
def test_house_robber(rob_function):
    test_cases = [
        ([5], 5),
        ([3,1], 3),
        ([2,7,9,3,1], 12),
        ([2,1,1,2], 4),
        ([0,0,0,0], 0),
        ([6,3,10,8,2,10,3,5,10,5,3], 39)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = rob_function(nums)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}\n")

# You can use this function to test your implementations
# Example: test_house_robber(rob)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Dynamic Programming with Tabulation (Neetcode solution)
2. Dynamic Programming with Memoization (Neetcode solution)
3. Constant Space Dynamic Programming (Neetcode solution)

Count: 3 solutions (all Neetcode solutions)

##### Rejected solutions

1. Brute Force: Generate all possible combinations of non-adjacent houses and find the maximum sum.
2. Greedy Approach: Always choose the house with the maximum amount, skipping adjacent houses.

#### Worthy Solutions

##### Dynamic Programming with Tabulation

```python
def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # Initialize the DP table
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Fill the DP table
    for i in range(2, len(nums)):
        # Key decision: rob current house and 2 houses before, or skip current house
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    # Return the maximum amount that can be robbed
    return dp[-1]
```

Time Complexity: O(n), where n is the number of houses. We iterate through the array once to fill the DP table.
Space Complexity: O(n) to store the DP table.

Explanation:

- The DP table `dp[i]` represents the maximum amount that can be robbed up to house i.
- The recurrence relation is `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`.
- We initialize the first two elements of the DP table as base cases.
- For each subsequent house, we decide whether to rob it (and add to the amount from two houses before) or skip it (and take the amount from the previous house).
- The final element in the DP table gives us the maximum amount that can be robbed.

##### Dynamic Programming with Memoization

```python
def rob(nums: List[int]) -> int:
    memo = {}

    def dp(i: int) -> int:
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]

        # Key decision: rob current house and skip next, or skip current house
        memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
        return memo[i]

    return dp(0)
```

Time Complexity: O(n), where n is the number of houses. Each house is processed once and stored in the memo.
Space Complexity: O(n) for the memoization dictionary and the recursion stack.

Explanation:

- We use a top-down approach with memoization to avoid redundant calculations.
- The `dp(i)` function represents the maximum amount that can be robbed starting from house i.
- We use a dictionary `memo` to store already computed results.
- For each house, we decide whether to rob it (and move to i+2) or skip it (and move to i+1).
- The base case is when we've passed all houses (i >= len(nums)).
- Memoization ensures that each subproblem is solved only once.

##### Constant Space Dynamic Programming

```python
def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, nums[0]

    for i in range(1, len(nums)):
        # Key decision: rob current house and 2 houses before, or skip current house
        current = max(nums[i] + prev2, prev1)
        prev2, prev1 = prev1, current

    return prev1
```

Time Complexity: O(n), where n is the number of houses. We iterate through the array once.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation:

- This solution optimizes the space complexity by only keeping track of the two previous maximum amounts.
- `prev2` represents the maximum amount that could be robbed two houses ago.
- `prev1` represents the maximum amount that could be robbed from the previous house.
- For each house, we update the current maximum and shift our "sliding window" of two previous values.
- This approach is based on the observation that we only need the results from the two previous steps to make a decision for the current house.

#### Rejected Approaches

1. Brute Force Approach:

   - Generate all possible combinations of non-adjacent houses and find the maximum sum.
   - Rejected because it has an exponential time complexity of O(2^n), making it impractical for large inputs.

2. Greedy Approach:
   - Always choose the house with the maximum amount, skipping adjacent houses.
   - Rejected because it doesn't guarantee the optimal solution. For example, in the case [2,1,1,2], the greedy approach would choose [2,1] for a total of 3, while the optimal solution is [2,2] for a total of 4.

#### Final Recommendations

The Constant Space Dynamic Programming solution is the best to learn and use in an interview setting. It combines the efficiency of dynamic programming with optimal space complexity. This solution demonstrates a deep understanding of the problem and showcases the ability to optimize both time and space complexity.

The tabulation and memoization approaches are also worth understanding as they represent standard DP techniques and can be useful in solving similar problems or when additional information needs to be stored during the process.

### Visualization(s)

For this problem, a visual representation of the dynamic programming process can be helpful. Here's a simple ASCII art visualization of how the constant space DP solution works for the input [2,7,9,3,1]:

```
[2, 7, 9, 3, 1]
 ^
 |
prev2 = 0
prev1 = 2

[2, 7, 9, 3, 1]
    ^
    |
prev2 = 2
prev1 = 7

[2, 7, 9, 3, 1]
       ^
       |
prev2 = 7
prev1 = 11 (9 + 2)

[2, 7, 9, 3, 1]
          ^
          |
prev2 = 11
prev1 = 11 (max(3 + 7, 11))

[2, 7, 9, 3, 1]
             ^
             |
prev2 = 11
prev1 = 12 (1 + 11)

Final result: 12
```

This visualization shows how we only need to keep track of the two previous maximum values as we iterate through the array, demonstrating the constant space usage of the optimal solution.

##### Backtracking Solution

```python
def rob(nums: List[int]) -> int:
    def backtrack(index: int, current_sum: int) -> int:
        if index >= len(nums):
            return current_sum

        # Option 1: Rob the current house
        rob_current = backtrack(index + 2, current_sum + nums[index])

        # Option 2: Skip the current house
        skip_current = backtrack(index + 1, current_sum)

        return max(rob_current, skip_current)

    return backtrack(0, 0)
```

Time Complexity: O(2^n), where n is the number of houses. In the worst case, we explore two options (rob or skip) for each house.
Space Complexity: O(n) due to the recursion stack.

Explanation:

- The backtracking function explores two options at each step: rob the current house or skip it.
- We keep track of the current sum and the index of the house we're considering.
- The base case is when we've considered all houses (index >= len(nums)).
- We return the maximum of the two options: robbing the current house and skipping to index+2, or skipping the current house and moving to index+1.

#### Analysis of the Backtracking Approach

Pros:

1. Intuitive and straightforward implementation.
2. Explores all possible combinations, guaranteeing the optimal solution.
3. Can be easily modified to return the actual sequence of houses robbed, not just the maximum amount.

Cons:

1. Exponential time complexity (O(2^n)), making it impractical for large inputs.
2. Redundant calculations, as it solves the same subproblems multiple times.
3. Does not leverage the optimal substructure of the problem efficiently.

#### Would I recommend it?

While the backtracking solution is a valid approach and can be useful for understanding the problem, I would not recommend it as the primary solution to learn or use in an interview setting for the following reasons:

1. Inefficiency: The exponential time complexity makes it unsuitable for larger inputs, which could be a concern in real-world scenarios or when dealing with stricter time constraints in an interview.

2. Existence of better alternatives: The dynamic programming solutions (tabulation, memoization, and constant space) we discussed earlier are more efficient and demonstrate a deeper understanding of the problem's structure.

3. Interview expectations: In a coding interview, especially for a problem like House Robber, interviewers typically expect candidates to recognize the dynamic programming nature of the problem and implement a more efficient solution.

However, the backtracking solution could be valuable in the following contexts:

1. As a stepping stone: If you're struggling to see the dynamic programming solution, starting with a backtracking approach and then optimizing it (e.g., by adding memoization) can be a good problem-solving strategy.

2. When asked for all solutions: If the interviewer asks for all possible combinations that yield the maximum amount, a modified backtracking approach could be useful.

3. To demonstrate problem-solving versatility: Mentioning that a backtracking solution exists (but explaining why it's not optimal) can show a broader understanding of algorithmic approaches.

#### Final Recommendation

While it's good to be aware of the backtracking approach, I still recommend focusing on the dynamic programming solutions, particularly the constant space DP solution, as the primary approach to learn and use for the House Robber problem. If you have time in an interview, you could mention the existence of a backtracking solution to demonstrate your comprehensive understanding of the problem space.
