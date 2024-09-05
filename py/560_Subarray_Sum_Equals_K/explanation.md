## Explanation: Subarray Sum Equals K

### Analysis of problem & input data

This problem is a classic example of the "subarray sum" category of problems. The key aspects to consider are:

1. We're dealing with contiguous subarrays, not just any subset of the array.
2. The array can contain both positive and negative integers.
3. The target sum (k) can be positive, negative, or zero.
4. We need to count all subarrays that sum to k, not just find one or report if one exists.

The fact that we're looking for contiguous subarrays suggests that we might be able to use some form of sliding window or cumulative sum approach. However, the presence of negative numbers complicates the use of a simple sliding window, as the sum doesn't monotonically increase or decrease as we expand the window.

The key principle that makes this question simple is the use of cumulative sums (prefix sums) and the property that the sum of any subarray can be calculated by the difference of two cumulative sums. This allows us to transform the problem into finding pairs of indices where the difference between their cumulative sums is k.

### Test cases

1. Basic case: `nums = [1,1,1], k = 2`
2. Zero sum: `nums = [1,-1,0], k = 0`
3. Negative numbers: `nums = [-1,-1,1], k = 0`
4. Single element as sum: `nums = [1], k = 1`
5. No valid subarray: `nums = [1,2,3], k = 6`
6. Multiple valid subarrays: `nums = [3,4,7,2,-3,1,4,2], k = 7`
7. Large array with repeated elements: `nums = [1]*10000 + [-1]*10000, k = 0`

```python
def test_subarray_sum(subarraySum):
    assert subarraySum([1,1,1], 2) == 2
    assert subarraySum([1,-1,0], 0) == 3
    assert subarraySum([-1,-1,1], 0) == 1
    assert subarraySum([1], 1) == 1
    assert subarraySum([1,2,3], 6) == 0
    assert subarraySum([3,4,7,2,-3,1,4,2], 7) == 4
    assert subarraySum([1]*10000 + [-1]*10000, 0) == 100010000
    print("All tests passed!")

# Run tests
test_subarray_sum(subarraySum)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Cumulative Sum with HashMap (Neetcode solution)
2. Brute Force
3. Sliding Window (for positive numbers only)

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Binary Search: Not applicable as the array is not sorted and may contain negative numbers.
2. Two Pointers: Not optimal due to the presence of negative numbers.

#### Worthy Solutions

##### Cumulative Sum with HashMap

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        sum_counts = {0: 1}  # Initialize with 0 sum seen once

        for num in nums:
            cum_sum += num
            # If (cum_sum - k) exists in sum_counts, it means we've found a subarray with sum k
            if cum_sum - k in sum_counts:
                count += sum_counts[cum_sum - k]
            # Update the count of the current cumulative sum
            sum_counts[cum_sum] = sum_counts.get(cum_sum, 0) + 1

        return count
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(n) in the worst case, where all prefix sums are unique.

Explanation:

- We iterate through the array once, which gives us O(n) time complexity.
- For each element, we perform constant time operations (addition, dictionary lookup, and update).
- The space complexity is O(n) because in the worst case, we might need to store counts for all prefix sums in the dictionary.

Intuition and invariants:

- The cumulative sum at any index i represents the sum of all elements from index 0 to i.
- If we have two indices i and j where the difference between their cumulative sums is k, it means the subarray from i+1 to j sums to k.
- We use a hashmap to store the counts of cumulative sums we've seen so far.
- At each step, we check if (current_sum - k) exists in our hashmap. If it does, it means we've found a subarray that sums to k.
- The count of (current_sum - k) in the hashmap represents the number of valid subarrays ending at the current index.

##### Brute Force

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum == k:
                    count += 1

        return count
```

Time Complexity: O(n^2), where n is the length of the input array.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation:

- We use two nested loops to consider all possible subarrays, giving us O(n^2) time complexity.
- For each subarray, we calculate its sum and check if it equals k.
- We use constant extra space, regardless of the input size, resulting in O(1) space complexity.

Intuition and invariants:

- This approach considers all possible subarrays by using two pointers: start and end.
- For each start index, we consider all possible end indices and calculate the sum of the subarray.
- We increment the count whenever we find a subarray sum equal to k.
- This method is straightforward but inefficient for large inputs due to its quadratic time complexity.

##### Sliding Window (for positive numbers only)

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if any(num < 0 for num in nums):
            raise ValueError("This solution only works for non-negative numbers")

        count = 0
        window_sum = 0
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= k:
                if window_sum == k:
                    count += 1
                window_sum -= nums[left]
                left += 1

        return count
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we only use a constant amount of extra space.

Explanation:

- We iterate through the array once with the right pointer, giving us O(n) time complexity.
- The left pointer also moves from left to right, never moving backwards, ensuring we don't exceed O(n) operations.
- We use constant extra space, regardless of the input size, resulting in O(1) space complexity.

Intuition and invariants:

- This approach uses a sliding window technique, which is efficient for arrays with non-negative numbers.
- We maintain a window where the sum is less than or equal to k.
- When the window sum exceeds k, we shrink the window from the left until it's no longer greater than k.
- This method is very efficient but only works when all numbers are non-negative, as it relies on the property that the sum always increases when we expand the window to the right.

#### Rejected Approaches

1. Binary Search: This approach is not applicable here because the array is not sorted, and even if we sorted it, we'd lose the contiguity of subarrays. Moreover, the presence of negative numbers means that the cumulative sum is not monotonically increasing, which is a requirement for binary search to work effectively.

2. Two Pointers: While a two-pointer approach can work for some subarray sum problems, it's not optimal here due to the presence of negative numbers. The two-pointer method typically relies on a monotonic property (e.g., sum always increases when we move the right pointer), which doesn't hold when we have negative numbers.

3. Dynamic Programming: Although DP can solve this problem, it would require O(n^2) time and O(n) space, which is less efficient than the cumulative sum with hashmap approach. DP is overkill for this problem and doesn't provide any significant advantage.

#### Final Recommendations

The Cumulative Sum with HashMap approach (Neetcode solution) is the best to learn for this problem. It's optimal in both time and space complexity, and it works for all cases, including negative numbers and zero. This approach demonstrates a clever use of a hashmap to solve a seemingly complex problem in linear time, which is a common pattern in many array and string problems.

The Brute Force solution, while intuitive, is not efficient for large inputs. However, it's worth understanding as a baseline approach and for solving similar problems with small input sizes or in constrained environments.

The Sliding Window approach, while efficient, is limited to non-negative numbers. It's still worth learning as it's applicable to many other subarray problems and demonstrates the sliding window technique well.

### Visualization(s)

For the Cumulative Sum with HashMap approach, we can visualize the process using a simple table:

```
Index | Number | Cumulative Sum | Sum Counts | cum_sum - k | Count
------+--------+----------------+------------+-------------+------
  0   |   1    |       1        |  {0:1, 1:1}|     -1      |  0
  1   |   1    |       2        |{0:1, 1:1, 2:1}|   0      |  1
  2   |   1    |       3        |{0:1, 1:1, 2:1, 3:1}| 1   |  2
```

This visualization helps to understand how we're building up the sum_counts dictionary and how we're checking for subarrays that sum to k at each step.
