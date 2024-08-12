# Explanation: Search in Rotated Sorted Array

## Analysis of problem & input data

This problem presents a unique variation of the binary search algorithm. The key characteristics and insights are:

1. The input array is initially sorted in ascending order.
2. The array is then rotated at an unknown pivot point.
3. All values in the array are unique.
4. The task is to find a specific target value in O(log n) time complexity.

The crucial insight here is that despite the rotation, the array still maintains partial sorting. It effectively consists of two sorted subarrays. The challenge lies in determining which subarray contains the target and then performing a binary search within that subarray.

The key principle that makes this question solvable in O(log n) time is that in any given half of the rotated array, at least one side is guaranteed to be sorted. This property allows us to make a decision at each step of the binary search about which half to continue searching in.

## Test cases

### Test cases

1. Normal case:

   - Input: nums = [4,5,6,7,0,1,2], target = 0
   - Expected Output: 4

2. Target not in array:

   - Input: nums = [4,5,6,7,0,1,2], target = 3
   - Expected Output: -1

3. Single element array:

   - Input: nums = [1], target = 0
   - Expected Output: -1

4. Target at the beginning of rotated part:

   - Input: nums = [4,5,6,7,0,1,2], target = 4
   - Expected Output: 0

5. Target at the end of rotated part:

   - Input: nums = [4,5,6,7,0,1,2], target = 2
   - Expected Output: 6

6. No rotation:

   - Input: nums = [1,2,3,4,5], target = 3
   - Expected Output: 2

7. Maximum rotation (rotated by n-1 positions):

   - Input: nums = [2,1], target = 2
   - Expected Output: 0

8. Large array:
   - Input: nums = list(range(1000, 10000)) + list(range(0, 1000)), target = 9999
   - Expected Output: 8999

Here's the Python code to run these test cases:

```python
def search(nums: List[int], target: int) -> int:
    # Implementation will be added here
    pass

# Test cases
test_cases = [
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
    ([4,5,6,7,0,1,2], 4, 0),
    ([4,5,6,7,0,1,2], 2, 6),
    ([1,2,3,4,5], 3, 2),
    ([2,1], 2, 0),
    (list(range(1000, 10000)) + list(range(0, 1000)), 9999, 8999)
]

for i, (nums, target, expected) in enumerate(test_cases, 1):
    result = search(nums, target)
    print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
    if result != expected:
        print(f"  Expected: {expected}, Got: {result}")
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Modified Binary Search (most optimal and elegant)
2. Two-pass Binary Search (find pivot, then search)

Count: 2 solutions

#### Rejected solutions

1. Linear Search (O(n) time complexity, doesn't meet the requirement)
2. Standard Binary Search without modifications (fails on rotated arrays)

### Worthy Solutions

#### Modified Binary Search

```python
from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                # Target is in the left half
                right = mid - 1
            else:
                # Target is in the right half
                left = mid + 1
        else:
            # Right half must be sorted
            if nums[mid] < target <= nums[right]:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1

    return -1  # Target not found
```

Time Complexity: O(log n)
Space Complexity: O(1)

Intuition and invariants:

- The key insight is that in a rotated sorted array, at least one half of the array is always sorted.
- We can determine which half is sorted by comparing nums[left] with nums[mid].
- If the left half is sorted and the target is within its range, we search there; otherwise, we search the right half.
- If the right half is sorted and the target is within its range, we search there; otherwise, we search the left half.
- This approach allows us to eliminate half of the search space in each iteration, maintaining the O(log n) time complexity.

#### Two-pass Binary Search

```python
from typing import List

def find_pivot(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            # Pivot is in the right half
            left = mid + 1
        else:
            # Pivot is in the left half or mid is the pivot
            right = mid

    return left

def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def search(nums: List[int], target: int) -> int:
    pivot = find_pivot(nums)

    # Search in the left sorted portion
    if pivot > 0 and nums[0] <= target <= nums[pivot - 1]:
        return binary_search(nums, target, 0, pivot - 1)

    # Search in the right sorted portion
    return binary_search(nums, target, pivot, len(nums) - 1)
```

Time Complexity: O(log n)
Space Complexity: O(1)

Intuition and invariants:

- This approach first finds the pivot (the point where the array is rotated) using binary search.
- The pivot is the smallest element in the array, and it's the only element smaller than its previous element.
- Once we find the pivot, we know that the array is split into two sorted subarrays.
- We can then perform a standard binary search on the appropriate subarray.
- This method is conceptually simpler but requires two passes through the array.

### Rejected Approaches

1. Linear Search (O(n)):

   - While this would work, it doesn't meet the O(log n) time complexity requirement.
   - It's a brute force approach that doesn't leverage the sorted nature of the array.

2. Standard Binary Search:

   - This fails because it assumes the entire array is sorted, which is not true in this case.
   - It would work only if the array wasn't rotated.

3. Recursive Binary Search:
   - While this could work, it's not as space-efficient as the iterative approach due to the call stack.
   - The iterative approach achieves the same result with O(1) space complexity.

### Final Recommendations

The Modified Binary Search (first approach) is the best solution to learn and implement for this problem. Here's why:

1. It meets the O(log n) time complexity requirement.
2. It uses O(1) space, which is optimal.
3. It solves the problem in a single pass through the array.
4. It directly addresses the rotated nature of the array without needing to find the pivot explicitly.

The Two-pass Binary Search is also a valid approach and might be easier to understand conceptually. However, it's slightly less efficient as it requires two binary searches in the worst case.

When approaching similar problems, always consider:

1. Can we modify a known efficient algorithm (like binary search) to fit the problem?
2. Are there any invariants in the data structure that we can exploit?
3. Can we make decisions at each step to eliminate a large portion of the search space?

Avoid the temptation to use linear search or any O(n) solutions when dealing with sorted arrays, even if they're rotated. The sorting property, even when partially disrupted, usually allows for more efficient logarithmic time solutions.

## Visualization(s)

To visualize the Modified Binary Search approach, we can use a simple ASCII representation:

```
Initial array: [4, 5, 6, 7, 0, 1, 2]
Target: 0

Step 1:
[4, 5, 6, 7, 0, 1, 2]
 L     M        R
Left half is sorted, but target is smaller than left, so search right half

Step 2:
[4, 5, 6, 7, 0, 1, 2]
          L  M     R
Right half is sorted, target is within range, so search left half

Step 3:
[4, 5, 6, 7, 0, 1, 2]
          L  M  R
Found target at index 4
```

This visualization demonstrates how the algorithm narrows down the search space by determining which half is sorted and whether the target could be in that half.
