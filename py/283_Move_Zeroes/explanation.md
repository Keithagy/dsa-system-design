# Explanation: Move Zeroes

## Analysis of problem & input data

This problem presents several key characteristics that guide our solution approach:

1. In-place modification: We need to modify the array without creating a new one, which suggests we should focus on swapping or shifting elements.

2. Maintaining order: The relative order of non-zero elements must be preserved, which rules out naive approaches like sorting.

3. Array constraints: The array length can be quite large (up to 10^4), so we need to be mindful of time complexity.

4. Element range: The elements can be any 32-bit integer, including negative numbers. This means we can't use any special properties of positive numbers.

5. Minimizing operations: The follow-up asks about minimizing operations, which hints at the possibility of a single-pass solution.

The key principle that makes this question simple is the realization that we can achieve the desired result by "collecting" all non-zero elements at the beginning of the array, effectively pushing all zeros to the end.

## Solutions

### Solution 1: Two-Pointer Approach

```python
from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Moves all zeros to the end of the array in-place.
    """
    # Pointer for the position where we'll place the next non-zero element
    non_zero_pos = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is non-zero
        if nums[i] != 0:
            # Swap the current element with the element at non_zero_pos
            nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
            # Increment non_zero_pos
            non_zero_pos += 1

    # At this point, all non-zero elements are at the front of the array
    # and all zeros are at the end
```

Time Complexity: O(n), where n is the length of the array. We traverse the array once.
Space Complexity: O(1), as we modify the array in-place without using extra space.

This solution leverages the following intuitions:

- We can use two pointers: one to iterate through the array, and another to keep track of where we should place the next non-zero element.
- By swapping non-zero elements to the front, we automatically push zeros to the end.
- This approach minimizes the number of operations by only performing swaps when necessary.

### Solution 2: Overwrite and Fill

```python
from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Moves all zeros to the end of the array in-place.
    """
    # Position to write the next non-zero element
    write_pos = 0

    # First pass: overwrite with non-zero elements
    for num in nums:
        if num != 0:
            nums[write_pos] = num
            write_pos += 1

    # Second pass: fill the rest with zeros
    while write_pos < len(nums):
        nums[write_pos] = 0
        write_pos += 1
```

Time Complexity: O(n), where n is the length of the array. We traverse the array twice.
Space Complexity: O(1), as we modify the array in-place without using extra space.

This solution leverages the following intuitions:

- We can overwrite the array with non-zero elements, keeping their relative order.
- After overwriting, we know exactly how many zeros we need to append.
- This approach may be more cache-friendly as it avoids swapping.

## Recommendation

I recommend learning the Two-Pointer Approach (Solution 1) for several reasons:

1. It solves the problem in a single pass, which is generally more efficient.
2. It minimizes the number of write operations, which can be beneficial in certain scenarios (e.g., when writing to slower memory).
3. The two-pointer technique is a common pattern in array manipulation problems, making this solution more generalizable to other problems.

While the Overwrite and Fill approach (Solution 2) is also correct and has the same time complexity, it requires two passes through the array and potentially more write operations.

## Test cases

```python
def test_moveZeroes():
    # Test case 1: Standard case
    nums1 = [0, 1, 0, 3, 12]
    moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0], f"Test case 1 failed. Output: {nums1}"

    # Test case 2: All zeros
    nums2 = [0, 0, 0, 0]
    moveZeroes(nums2)
    assert nums2 == [0, 0, 0, 0], f"Test case 2 failed. Output: {nums2}"

    # Test case 3: No zeros
    nums3 = [1, 2, 3, 4]
    moveZeroes(nums3)
    assert nums3 == [1, 2, 3, 4], f"Test case 3 failed. Output: {nums3}"

    # Test case 4: Single element
    nums4 = [0]
    moveZeroes(nums4)
    assert nums4 == [0], f"Test case 4 failed. Output: {nums4}"

    # Test case 5: Zeros at the end
    nums5 = [1, 2, 3, 0, 0]
    moveZeroes(nums5)
    assert nums5 == [1, 2, 3, 0, 0], f"Test case 5 failed. Output: {nums5}"

    print("All test cases passed!")

# Run the tests
test_moveZeroes()
```

## Overview of rejected approaches

1. Sorting approach: While sorting the array would move all zeros to the end, it would not maintain the relative order of non-zero elements. It would also have a time complexity of O(n log n), which is less efficient than our O(n) solutions.

2. Counting zeros and rebuilding the array: We could count the number of zeros, remove all zeros, and then append the counted zeros. This approach would work but requires either extra space (not in-place) or multiple passes through the array, making it less efficient than our chosen solutions.

3. Using a queue or stack: We might consider using a queue to store non-zero elements and then rebuild the array. However, this would require extra space and is unnecessary given the simpler in-place solutions available.

## Visualization(s)

To visualize the Two-Pointer Approach, let's create a simple step-by-step visualization using ASCII art:

### Move Zeroes: Two-Pointer Approach Visualization

Initial array: [0, 1, 0, 3, 12]

Step 1:
[0, 1, 0, 3, 12]
^ ^
| |
| current (i)
non_zero_pos

Step 2 (after swap):
[1, 0, 0, 3, 12]
^ ^
| |
| current (i)
non_zero_pos

Step 3:
[1, 0, 0, 3, 12]
^ ^
| |
| current (i)
non_zero_pos

Step 4 (after swap):
[1, 3, 0, 0, 12]
^ ^
| |
| current (i)
non_zero_pos

Step 5 (after swap):
[1, 3, 12, 0, 0]
^ ^
| |
| current (i)
non_zero_pos

Final array: [1, 3, 12, 0, 0]

This visualization shows how the two pointers move through the array, swapping elements when necessary to move non-zero elements to the front and zeros to the end.

This visualization should help in understanding how the two pointers move through the array and how elements are swapped to achieve the desired result.
