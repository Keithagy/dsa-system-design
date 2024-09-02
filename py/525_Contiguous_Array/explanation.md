## Explanation: Contiguous Array

### Analysis of problem & input data

This problem is about finding the longest contiguous subarray with an equal number of 0s and 1s in a binary array. The key characteristics of this problem are:

1. Binary input: The array contains only 0s and 1s.
2. Contiguous subarray: We're looking for a continuous sequence of elements.
3. Equal number of 0s and 1s: The goal is to find the longest such subarray where the count of 0s equals the count of 1s.

The problem's nature suggests a few potential approaches:

1. Prefix Sum with Hash Map: This problem can be transformed into a prefix sum problem where we treat 0 as -1. This transformation allows us to use a cumulative sum approach, where a sum of 0 indicates an equal number of 0s and 1s.

2. Dynamic Programming: While possible, it's not the most efficient for this problem due to the potential for O(n^2) time complexity.

3. Two Pointers: This approach might seem intuitive but isn't optimal due to the need to consider all possible subarrays.

The key principle that makes this question simple is the realization that we can transform the problem into a prefix sum problem by treating 0 as -1. This allows us to use a hash map to store the first occurrence of each sum, enabling us to find the longest subarray with equal 0s and 1s in a single pass.

### Test cases

1. Basic cases:

   - `[0,1]` → 2
   - `[0,1,0]` → 2

2. Longer sequences:

   - `[0,1,0,1,1,1,0,0,0]` → 6

3. All zeros or all ones:

   - `[0,0,0,0]` → 0
   - `[1,1,1,1]` → 0

4. Equal number of zeros and ones:

   - `[0,0,1,1]` → 4

5. Unequal total number of zeros and ones:

   - `[0,0,0,1,1,1,1]` → 6

6. Single element:

   - `[0]` → 0
   - `[1]` → 0

7. Empty array:
   - `[]` → 0

Here's the executable Python code for these test cases:

```python
def test_contiguous_array(func):
    test_cases = [
        ([0,1], 2),
        ([0,1,0], 2),
        ([0,1,0,1,1,1,0,0,0], 6),
        ([0,0,0,0], 0),
        ([1,1,1,1], 0),
        ([0,0,1,1], 4),
        ([0,0,0,1,1,1,1], 6),
        ([0], 0),
        ([1], 0),
        ([], 0)
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = func(nums)
        assert result == expected, f"Test case {i+1} failed. Expected {expected}, but got {result} for input {nums}"
    print("All test cases passed!")

# The solution function will be defined later
# test_contiguous_array(find_max_length)
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Prefix Sum with Hash Map (Neetcode solution)
2. Brute Force (for understanding)

Count: 2 solutions (1 Neetcode solution)

##### Rejected solutions

1. Dynamic Programming: While it can solve the problem, it's not as efficient as the prefix sum approach.
2. Two Pointers: This approach is not suitable for this problem as it cannot efficiently handle all cases.

#### Worthy Solutions

##### Prefix Sum with Hash Map

```python
from typing import List

def find_max_length(nums: List[int]) -> int:
    count = 0
    max_length = 0
    count_map = {0: -1}  # Initialize with 0 count at index -1

    for i, num in enumerate(nums):
        # Treat 0 as -1, so the count changes by -1 for 0 and +1 for 1
        count += 1 if num == 1 else -1

        if count == 0:
            # If count is 0, we have equal 0s and 1s from the start
            max_length = i + 1
        elif count in count_map:
            # If we've seen this count before, we have equal 0s and 1s in between
            max_length = max(max_length, i - count_map[count])
        else:
            # Record the first occurrence of this count
            count_map[count] = i

    return max_length
```

Time Complexity: O(n), where n is the length of the input array.

- We iterate through the array once, performing constant time operations for each element.
- Hash map lookups and insertions are generally O(1) on average.

Space Complexity: O(n)

- In the worst case, we might store n different count values in the hash map.

Explanation:

- This solution uses a clever transformation of the problem into a prefix sum problem.
- We treat 0 as -1 and 1 as 1, so the sum of a subarray with equal 0s and 1s will be 0.
- We keep track of the running sum (count) and store the first occurrence of each sum in a hash map.
- If we encounter the same sum again, it means the subarray between the first occurrence and the current index has an equal number of 0s and 1s.
- We use a hash map to store the first occurrence of each sum, allowing us to quickly compute the length of valid subarrays.

Key Intuitions:

- Treating 0 as -1 transforms the problem into finding the longest subarray with a sum of 0.
- A reoccurrence of a sum indicates a balanced subarray (equal 0s and 1s) in between.
- The hash map allows us to "remember" the first occurrence of each sum, enabling O(1) lookups.

##### Brute Force

```python
from typing import List

def find_max_length_brute_force(nums: List[int]) -> int:
    max_length = 0
    n = len(nums)

    for start in range(n):
        zeros = ones = 0
        for end in range(start, n):
            if nums[end] == 0:
                zeros += 1
            else:
                ones += 1

            if zeros == ones:
                max_length = max(max_length, end - start + 1)

    return max_length
```

Time Complexity: O(n^2), where n is the length of the input array.

- We have two nested loops, each potentially iterating through all elements.

Space Complexity: O(1)

- We only use a constant amount of extra space for variables.

Explanation:

- This solution checks all possible subarrays by using two pointers: start and end.
- For each start index, we iterate through all possible end indices.
- We count the number of zeros and ones in each subarray.
- If the count of zeros equals the count of ones, we update the max_length if necessary.

Key Intuitions:

- Every subarray needs to be checked to ensure we don't miss the longest one.
- We can count zeros and ones on the fly, avoiding the need for extra space.
- This approach is intuitive but not efficient for large inputs.

#### Rejected Approaches

1. Dynamic Programming: While it's possible to solve this problem using DP, it would require O(n^2) time and O(n^2) space, which is less efficient than the prefix sum approach. The DP solution would involve creating a 2D table to store the counts of 0s and 1s for each subarray, which is unnecessary given the more efficient prefix sum solution.

2. Two Pointers: This approach might seem intuitive at first, but it fails to efficiently handle all cases. The problem with a two-pointer approach is that it's not easy to determine when to move the left or right pointer to find the optimal subarray. Unlike problems where we're looking for a sum or a specific condition that changes monotonically, the balance of 0s and 1s can fluctuate in ways that make a single-pass two-pointer approach unreliable.

#### Final Recommendations

The Prefix Sum with Hash Map approach is the best solution to learn for this problem. It's efficient (O(n) time and space complexity) and demonstrates a clever transformation of the problem that allows for a single-pass solution. This approach also showcases the power of hash maps in solving array-based problems and introduces the concept of cumulative sum, which is applicable to many other problems.

While the Brute Force solution is intuitive and good for understanding the problem, it's not efficient enough for large inputs and wouldn't be suitable in an interview setting for anything but explaining your initial thoughts before moving to a more optimal solution.

### Visualization(s)

To visualize the Prefix Sum with Hash Map approach, we can use a simple ASCII art diagram:

```
Input: [0, 1, 0, 1, 1, 1, 0, 0]
Index:  0  1  2  3  4  5  6  7
Count: -1  0 -1  0  1  2  1  0

Count Map:
{0: -1}  // Initialize
{0: -1, -1: 0}  // After index 0
{0: -1, -1: 0}  // After index 1 (max_length = 2)
{0: -1, -1: 0, -1: 2}  // After index 2
{0: -1, -1: 0, -1: 2}  // After index 3 (max_length = 4)
{0: -1, -1: 0, -1: 2, 1: 4}  // After index 4
{0: -1, -1: 0, -1: 2, 1: 4, 2: 5}  // After index 5
{0: -1, -1: 0, -1: 2, 1: 4, 2: 5}  // After index 6
{0: -1, -1: 0, -1: 2, 1: 4, 2: 5}  // After index 7 (max_length = 8)

Final max_length: 8
```

This visualization shows how the count changes as we iterate through the array and how the count map is updated. The max_length is updated whenever we encounter a count we've seen before or when the count becomes 0.
