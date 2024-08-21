# Comprehensive Guide to Greedy Algorithms in LeetCode

## 1. LeetCode Questions with Greedy Solutions

1. \#55 - Jump Game
2. \#121 - Best Time to Buy and Sell Stock
3. \#455 - Assign Cookies
4. \#678 - Valid Parenthesis String
5. \#763 - Partition Labels
6. \#1029 - Two City Scheduling
7. \#1046 - Last Stone Weight
8. \#1221 - Split a String in Balanced Strings
9. \#1323 - Maximum 69 Number
10. \#1710 - Maximum Units on a Truck

## 2. LeetCode Questions Where Greedy Might Seem Correct But Isn't

1. \#45 - Jump Game II
2. \#122 - Best Time to Buy and Sell Stock II
3. \#309 - Best Time to Buy and Sell Stock with Cooldown
4. \#714 - Best Time to Buy and Sell Stock with Transaction Fee
5. \#991 - Broken Calculator
6. \#1326 - Minimum Number of Taps to Open to Water a Garden
7. \#1578 - Minimum Time to Make Rope Colorful

## 3. Optimal Solutions

### Greedy Solutions

1. \#55 - Jump Game

   ```python
   def canJump(nums):
       max_reach = 0
       for i, jump in enumerate(nums):
           if i > max_reach:
               return False
           max_reach = max(max_reach, i + jump)
       return True
   ```

2. \#121 - Best Time to Buy and Sell Stock

   ```python
   def maxProfit(prices):
       min_price = float('inf')
       max_profit = 0
       for price in prices:
           min_price = min(min_price, price)
           max_profit = max(max_profit, price - min_price)
       return max_profit
   ```

3. \#455 - Assign Cookies

   ```python
   def findContentChildren(g, s):
       g.sort()
       s.sort()
       child = cookie = 0
       while child < len(g) and cookie < len(s):
           if s[cookie] >= g[child]:
               child += 1
           cookie += 1
       return child
   ```

4. \#678 - Valid Parenthesis String

   ```python
   def checkValidString(s):
       lo = hi = 0
       for c in s:
           lo += 1 if c == '(' else -1
           hi += 1 if c != ')' else -1
           if hi < 0:
               break
           lo = max(lo, 0)
       return lo == 0
   ```

5. \#763 - Partition Labels

   ```python
   def partitionLabels(s):
       last = {c: i for i, c in enumerate(s)}
       j = anchor = 0
       ans = []
       for i, c in enumerate(s):
           j = max(j, last[c])
           if i == j:
               ans.append(i - anchor + 1)
               anchor = i + 1
       return ans
   ```

### Non-Greedy Solutions

1. \#45 - Jump Game II (Dynamic Programming)

   ```python
   def jump(nums):
       n = len(nums)
       dp = [float('inf')] * n
       dp[0] = 0
       for i in range(1, n):
           for j in range(i):
               if j + nums[j] >= i:
                   dp[i] = min(dp[i], dp[j] + 1)
       return dp[-1]
   ```

2. \#122 - Best Time to Buy and Sell Stock II (Dynamic Programming)

   ```python
   def maxProfit(prices):
       profit = 0
       for i in range(1, len(prices)):
           if prices[i] > prices[i-1]:
               profit += prices[i] - prices[i-1]
       return profit
   ```

3. \#309 - Best Time to Buy and Sell Stock with Cooldown (Dynamic Programming)

   ```python
   def maxProfit(prices):
       if len(prices) < 2:
           return 0
       sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
       for price in prices[1:]:
           prev_buy = buy
           buy = max(prev_sell - price, prev_buy)
           prev_sell = sell
           sell = max(prev_buy + price, prev_sell)
       return sell
   ```

## 4. Features to Consider for Greedy Algorithms

1. **Optimal Substructure**: The problem can be solved by making locally optimal choices at each step.
2. **Greedy Choice Property**: A locally optimal choice leads to a globally optimal solution.
3. **No Need for Look-ahead**: Decisions can be made solely based on the current state without considering future consequences.
4. **Irreversibility**: Once a choice is made, it's not reconsidered in future steps.
5. **Problem Structure**: The problem can be solved by iterating through the input in a specific order (e.g., sorted).

## 5. When to Rule Out Greedy Algorithms

1. **Global Optimization Required**: If the problem requires considering the entire input or future states to make optimal decisions.
2. **Dependent Subproblems**: If choices at one step affect the options available in future steps.
3. **Need for Backtracking**: If the solution might require undoing previous choices.
4. **Complex State Transitions**: If the problem state changes in ways that can't be captured by simple local decisions.
5. **Multiple Interacting Parameters**: If optimizing for multiple parameters simultaneously, greedy might not find the best balance.

Remember, recognizing whether a problem is suitable for a greedy approach often comes with practice and familiarity with problem patterns. Always consider alternative approaches like dynamic programming or backtracking when a greedy solution isn't immediately apparent or provably optimal.
