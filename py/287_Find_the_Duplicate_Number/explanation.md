## Explanation: Find the Duplicate Number

### Analysis of problem & input data

This problem presents a fascinating challenge that combines elements of array manipulation, number theory, and cycle detection. Let's break down the key characteristics:

1. Array structure: We have an array of `n+1` integers, where each integer is in the range `[1, n]`. This peculiar structure is the first clue towards potential solution strategies.

2. Duplicate constraint: There is exactly one number that appears more than once. All other numbers appear exactly once.

3. Space and modification constraints: We must solve the problem without modifying the array and using only constant extra space. This rules out sorting or using additional data structures proportional to the input size.

4. Range of values: The values are bounded between 1 and n, inclusive. This is crucial for certain algorithmic approaches.

The key principle that makes this question tractable is the pigeonhole principle. With `n+1` slots (array indices) and only `n` possible values, there must be at least one duplicate. This guarantee allows us to treat the array as a implicit linked list, where the value at each index points to another index.

The problem then transforms into finding a cycle in this implicit linked list, which is a classic application of Floyd's Cycle Detection algorithm (also known as the "tortoise and hare" algorithm). This realization connects our array problem to graph theory and cycle detection, opening up elegant solution paths.

### Test cases

1. Standard case: `[1,3,4,2,2]` (Output: 2)
2. Duplicate at the beginning: `[3,1,3,4,2]` (Output: 3)
3. All elements are the same: `[3,3,3,3,3]` (Output: 3)
4. Larger array: `[5,2,1,3,5,7,6,4]` (Output: 5)
5. Minimum size array: `[1,1]` (Output: 1)
6. Maximum size array (not practical to write out, but conceptually important)

Here's the Python code for these test cases:

```python
def find_duplicate(nums: List[int]) -> int:
    # Implementation will go here
    pass

# Test cases
test_cases = [
    [1,3,4,2,2],
    [3,1,3,4,2],
    [3,3,3,3,3],
    [5,2,1,3,5,7,6,4],
    [1,1]
]

for i, case in enumerate(test_cases, 1):
    result = find_duplicate(case)
    print(f"Test case {i}: Input = {case}, Output = {result}")

# Note: We can't practically test the maximum size array (10^5 elements) in this environment,
# but it's important to consider for time complexity analysis.
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Floyd's Cycle Detection (Tortoise and Hare) - Neetcode solution
2. Binary Search
3. Bit Manipulation
4. Marking visited elements (violates problem constraints, but worth understanding)

Count: 4 solutions, including 1 Neetcode solution.

##### Rejected solutions

1. Sorting the array (violates the "without modifying the array" constraint)
2. Using a hash set (violates the "constant extra space" constraint)
3. Brute force comparison of all pairs (inefficient, O(n^2) time complexity)

#### Worthy Solutions

##### Floyd's Cycle Detection (Tortoise and Hare)

```python
def find_duplicate(nums: List[int]) -> int:
    # Initialize both pointers to the start of the array
    slow = fast = nums[0]

    # Phase 1: Find the intersection point of the two runners
    while True:
        slow = nums[slow]  # Move slow pointer one step
        fast = nums[nums[fast]]  # Move fast pointer two steps
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
```

Time Complexity: O(n)
Space Complexity: O(1)

Explanation of time and space complexity:

- Time: The algorithm has two phases. In the worst case, the first phase might traverse the entire "linked list" once (O(n)). The second phase will at most traverse the "linked list" once more (O(n)). Therefore, the total time complexity is O(n).
- Space: We only use two pointers (slow and fast) regardless of the input size, hence constant space O(1).

Intuitions and invariants:

- The array can be viewed as a function f(x) = nums[x], creating an implicit linked list.
- Due to the pigeonhole principle, this "linked list" must contain a cycle.
- The start of the cycle corresponds to the duplicate number.
- Floyd's algorithm guarantees finding the cycle in linear time and constant space.

##### Binary Search

```python
def find_duplicate(nums: List[int]) -> int:
    left, right = 1, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        count = sum(num <= mid for num in nums)

        # If count is greater than mid, the duplicate is in the left half
        if count > mid:
            right = mid
        else:
            left = mid + 1

    return left
```

Time Complexity: O(n log n)
Space Complexity: O(1)

Explanation of time and space complexity:

- Time: We perform a binary search on the range [1, n], which takes O(log n) iterations. In each iteration, we count numbers in the array, which takes O(n) time. Thus, the total time complexity is O(n log n).
- Space: We only use a few variables (left, right, mid, count) regardless of the input size, hence constant space O(1).

Intuitions and invariants:

- The duplicate number creates an "excess" in the count of numbers less than or equal to it.
- By binary searching on the range of possible values, we can pinpoint this excess.
- The invariant is that the duplicate number is always in the range we're searching.

##### Bit Manipulation

```python
def find_duplicate(nums: List[int]) -> int:
    duplicate = 0
    n = len(nums) - 1
    bit_max = n.bit_length()

    for bit in range(bit_max):
        mask = 1 << bit
        base_count = sum(i & mask for i in range(1, n+1))
        nums_count = sum(num & mask for num in nums)

        if nums_count > base_count:
            duplicate |= mask

    return duplicate
```

Time Complexity: O(n log n)
Space Complexity: O(1)

Explanation of time and space complexity:

- Time: We iterate through each bit (log n bits for numbers up to n) and for each bit, we traverse the entire array once. This gives us O(n log n) time complexity.
- Space: We only use a few variables (duplicate, mask, base_count, nums_count) regardless of the input size, hence constant space O(1).

Intuitions and invariants:

- Each number can be represented as a binary string.
- The duplicate number will cause an excess in the count of 1s for certain bit positions.
- By checking each bit position, we can reconstruct the duplicate number.

##### Marking visited elements (violates problem constraints)

```python
def find_duplicate(nums: List[int]) -> int:
    for num in nums:
        index = abs(num)
        if nums[index] > 0:
            nums[index] = -nums[index]
        else:
            return index
    return -1  # This line should never be reached given the problem constraints
```

Time Complexity: O(n)
Space Complexity: O(1)

Explanation of time and space complexity:

- Time: We traverse the array once, performing constant-time operations for each element. This gives us O(n) time complexity.
- Space: We modify the input array in-place and use no additional data structures, hence O(1) space.

Intuitions and invariants:

- We use the sign of elements as a marker for visited indices.
- The first number we encounter that points to an already negative number is the duplicate.
- This method is efficient but violates the constraint of not modifying the input array.

#### Rejected Approaches

1. Sorting the array: While this would make finding the duplicate trivial (adjacent elements would be equal), it violates the constraint of not modifying the input array.

2. Using a hash set: This approach, while intuitive and efficient (O(n) time), violates the constant space constraint as it requires O(n) additional space in the worst case.

3. Brute force comparison: Comparing each element with every other element would find the duplicate but has a time complexity of O(n^2), which is inefficient for large inputs.

#### Final Recommendations

The Floyd's Cycle Detection (Tortoise and Hare) method is the best solution to learn for this problem. It's elegant, satisfies all the given constraints (no array modification, constant space), and has optimal time complexity O(n). Moreover, it introduces a powerful algorithm that has applications in various other problems involving linked lists and cycle detection.

The Binary Search and Bit Manipulation methods are also worth understanding as they provide alternative perspectives on the problem and demonstrate how to leverage the constraints of the input data. However, they are slightly less efficient (O(n log n)) and potentially more complex to implement correctly.

The "marking visited elements" approach, while not satisfying the problem constraints, is worth knowing as it demonstrates a clever use of array indices and could be applicable in scenarios where modifying the input is allowed.
