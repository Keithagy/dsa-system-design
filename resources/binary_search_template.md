# Binary Search Template

[Source](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)

## Intro

Binary Search is quite easy to understand conceptually. Basically, it splits the search space into two halves and only keep the half that probably has the search target and throw away the other half that would not possibly have the answer. In this manner, we reduce the search space to half the size at every step, until we find the target. Binary Search helps us reduce the search time from linear O(n) to logarithmic O(log n). But when it comes to implementation, it's rather difficult to write a bug-free code in just a few minutes. Some of the most common problems include:

- When to exit the loop? Should we use `left < right` or `left <= right` as the while loop condition?
- How to initialize the boundary variable left and right?
- How to update the boundary? How to choose the appropriate combination from `left = mid`, `left = mid + 1` and `right = mid`, `right = mid - 1`?

A rather common misunderstanding of binary search is that people often think this technique could only be used in simple scenario like "Given a sorted array, find a specific value in it". As a matter of fact, it can be applied to much more complicated situations.

After a lot of practice in LeetCode, I've made a powerful binary search template and solved many Hard problems by just slightly twisting this template. I'll share the template with you guys in this post. I don't want to just show off the code and leave. Most importantly, I want to share the logical thinking: how to apply this general template to all sorts of problems. Hopefully, after reading this post, people wouldn't be pissed off any more when LeetCoding, "This problem could be solved with binary search! Why didn't I think of that before!"

## Most Generalized Binary Search

Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascending order. For most tasks, we can transform the requirement into the following generalized form:

Minimize k, s.t. condition(k) is True

The following code is the most generalized binary search template:

```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

What's really nice of this template is that, for most of the binary search problems, we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

1. Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;
2. Decide return value. Is it `return left` or `return left - 1`? Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

Below I'll show you guys how to apply this powerful template to many LeetCode problems.

## Basic Application

### 278. First Bad Version [Easy]

You are a product manager and currently leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API bool isBadVersion(version) which will return whether version is bad.

Example:

Given n = 5, and version = 4 is the first bad version.

```
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
```

Then 4 is the first bad version.

First, we initialize `left = 1` and `right = n` to include all possible values. Then we notice that we don't even need to design the condition function. It's already given by the isBadVersion API. Finding the first bad version is equivalent to finding the minimal k satisfying isBadVersion(k) is True. Our template can fit in very nicely:

```python
class Solution:
    def firstBadVersion(self, n) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

### 69. Sqrt(x) [Easy]

Implement int sqrt(int x). Compute and return the square root of x, where x is guaranteed to be a non-negative integer. Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example:

```
Input: 4
Output: 2

Input: 8
Output: 2
```

Easy one. First we need to search for minimal k satisfying condition k^2 > x, then k - 1 is the answer to the question. We can easily come up with the solution. Notice that I set `right = x + 1` instead of `right = x` to deal with special input cases like x = 0 and x = 1.

```python
def mySqrt(x: int) -> int:
    left, right = 0, x + 1
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1  # `left` is the minimum k value, `k - 1` is the answer
```

### 35. Search Insert Position [Easy]

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

Example:

```
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1
```

Very classic application of binary search. We are looking for the minimal k value satisfying nums[k] >= target, and we can just copy-paste our template. Notice that our solution is correct regardless of whether the input array nums has duplicates. Also notice that the input target might be larger than all elements in nums and therefore needs to placed at the end of the array. That's why we should initialize `right = len(nums)` instead of `right = len(nums) - 1`.

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
```

## Advanced Application

The above problems are quite easy to solve, because they already give us the array to be searched. We'd know that we should use binary search to solve them at first glance. However, more often are the situations where the search space and search target are not so readily available. Sometimes we won't even realize that the problem should be solved with binary search -- we might just turn to dynamic programming or DFS and get stuck for a very long time.

As for the question "When can we use binary search?", my answer is that, If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.

### 1011. Capacity To Ship Packages Within D Days [Medium]

A conveyor belt has packages that must be shipped from one port to another within D days. The i-th package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Example:

```
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
```

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Binary search probably would not come to our mind when we first meet this problem. We might automatically treat weights as search space and then realize we've entered a dead end after wasting lots of time. In fact, we are looking for the minimal one among all feasible capacities. We dig out the monotonicity of this problem: if we can successfully ship all packages within D days with capacity m, then we can definitely ship them all with any capacity larger than m. Now we can design a condition function, let's call it feasible, given an input capacity, it returns whether it's possible to ship all packages within D days. This can run in a greedy way: if there's still room for the current package, we put this package onto the conveyor belt, otherwise we wait for the next day to place this package. If the total days needed exceeds D, we return False, otherwise we return True.

Next, we need to initialize our boundary correctly. Obviously capacity should be at least max(weights), otherwise the conveyor belt couldn't ship the heaviest package. On the other hand, capacity need not be more than sum(weights), because then we can ship all packages in just one day.

Now we've got all we need to apply our binary search template:

```python
def shipWithinDays(weights: List[int], D: int) -> int:
    def feasible(capacity) -> bool:
        days = 1
        total = 0
        for weight in weights:
            total += weight
            if total > capacity:  # too heavy, wait for the next day
                total = weight
                days += 1
                if days > D:  # cannot ship within D days
                    return False
        return True

    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

### 410. Split Array Largest Sum [Hard]

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Example:

```
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

If you take a close look, you would probably see how similar this problem is with LC 1011 above. Similarly, we can design a feasible function: given an input threshold, then decide if we can split the array into several subarrays such that every subarray-sum is less than or equal to threshold. In this way, we discover the monotonicity of the problem: if feasible(m) is True, then all inputs larger than m can satisfy feasible function. You can see that the solution code is exactly the same as LC 1011.

```python
def splitArray(nums: List[int], m: int) -> int:
    def feasible(threshold) -> bool:
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > threshold:
                total = num
                count += 1
                if count > m:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

But we probably would have doubts: It's true that left returned by our solution is the minimal value satisfying feasible, but how can we know that we can split the original array to actually get this subarray-sum? For example, let's say nums = [7,2,5,10,8] and m = 2. We have 4 different ways to split the array to get 4 different largest subarray-sum correspondingly: 25:[[7], [2,5,10,8]], 23:[[7,2], [5,10,8]], 18:[[7,2,5], [10,8]], 24:[[7,2,5,10], [8]]. Only 4 values. But our search space [max(nums), sum(nums)] = [10, 32] has much more that just 4 values. That is, no matter how we split the input array, we cannot get most of the values in our search space.

Let's say k is the minimal value satisfying feasible function. We can prove the correctness of our solution with proof by contradiction. Assume that no subarray's sum is equal to k, that is, every subarray sum is less than k. The variable total inside feasible function keeps track of the total weights of current load. If our assumption is correct, then total would always be less than k. As a result, feasible(k - 1) must be True, because total would at most be equal to k - 1 and would never trigger the if-clause if total > threshold, therefore feasible(k - 1) must have the same output as feasible(k), which is True. But we already know that k is the minimal value satisfying feasible function, so feasible(k - 1) has to be False, which is a contradiction. So our assumption is incorrect. Now we've proved that our algorithm is correct.

### 875. Koko Eating Bananas [Medium]

Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards have gone and will come back in H hours. Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas, and eats K bananas from that pile. If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back. Return the minimum integer K such that she can eat all the bananas within H hours.

Example:

```
Input: piles = [3,6,7,11], H = 8
Output: 4

Input: piles = [30,11,23,4,20], H = 5
Output: 30

Input: piles = [30,11,23,4,20], H = 6
Output: 23
```

Very similar to LC 1011 and LC 410 mentioned above. Let's design a feasible function, given an input speed, determine whether Koko can finish all bananas within H hours with hourly eating speed speed. Obviously, the lower bound of the search space is 1, and upper bound is max(piles), because Koko can only choose one pile of bananas to eat every hour.

```python
def minEatingSpeed(piles: List[int], H: int) -> int:
    def feasible(speed) -> bool:
        # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower
        return sum((pile - 1) // speed + 1 for pile in piles) <= H  # faster

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
right = mid
else:
left = mid + 1
return left
```

### 1482. Minimum Number of Days to Make m Bouquets [Medium]

Given an integer array bloomDay, an integer m and an integer k. We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden. The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet. Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Examples:

```
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
```

This problem follows the same pattern as the previous ones. We can use binary search to find the minimum number of days required. Let's break it down:

1. The search space is from 1 to the maximum value in bloomDay.
2. We need to design a feasible function that checks if it's possible to make m bouquets in a given number of days.
3. We'll use our binary search template to find the minimum number of days.

Here's the implementation:

```python
def minDays(bloomDay: List[int], m: int, k: int) -> int:
    def feasible(days) -> bool:
        bouquets, flowers = 0, 0
        for bloom in bloomDay:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
            if bouquets == m:
                return True
        return False

    if len(bloomDay) < m * k:
        return -1

    left, right = 1, max(bloomDay)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

In this solution:

1. We first check if it's possible to make m bouquets with the given flowers. If not, we return -1.
2. The feasible function checks if we can make m bouquets in a given number of days.
3. We use binary search to find the minimum number of days needed.

This problem demonstrates how versatile the binary search template can be. Even though the problem doesn't explicitly mention searching, we can transform it into a search problem and apply our template.

## Conclusion

The power of this binary search template lies in its flexibility. By designing an appropriate feasible function, we can apply it to a wide range of problems, even those that don't look like typical binary search problems at first glance.

Key points to remember:

1. Identify the search space and what you're minimizing or maximizing.
2. Design a feasible function that checks if a given value satisfies the conditions.
3. Use the template, adjusting the boundaries and return value as needed.

With practice, you'll be able to recognize more problems where this template can be applied, significantly expanding your problem-solving toolkit.
