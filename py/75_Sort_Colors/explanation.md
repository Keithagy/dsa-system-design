# Explanation: Sort Colors

## Analysis of problem & input data

This problem, known as the Dutch National Flag problem, is a classic sorting problem with a twist. The key characteristics and constraints that influence our solution approach are:

1. In-place sorting: We need to sort the array without using additional data structures, which rules out certain approaches.
2. Limited range of values: The array contains only three distinct values (0, 1, 2), which allows for specialized sorting techniques.
3. One-pass algorithm challenge: The follow-up question suggests we should aim for a single-pass solution.
4. Small to medium-sized input: The constraint of 1 <= n <= 300 suggests that even O(n^2) solutions might be acceptable, but we should aim for better.

The key principle that makes this question simple is the realization that we're not dealing with a general sorting problem, but a partitioning problem with a fixed number of partitions. This allows us to use techniques that wouldn't work for general sorting but are highly efficient for this specific case.

### Test cases

Here are some test cases that cover various scenarios:

1. Standard case:
   Input: [2, 0, 2, 1, 1, 0]
   Expected Output: [0, 0, 1, 1, 2, 2]

2. Already sorted:
   Input: [0, 0, 1, 1, 2, 2]
   Expected Output: [0, 0, 1, 1, 2, 2]

3. Reverse sorted:
   Input: [2, 2, 1, 1, 0, 0]
   Expected Output: [0, 0, 1, 1, 2, 2]

4. All same color:
   Input: [1, 1, 1, 1]
   Expected Output: [1, 1, 1, 1]

5. Two colors only:
   Input: [0, 1, 0, 1]
   Expected Output: [0, 0, 1, 1]

6. Single element:
   Input: [1]
   Expected Output: [1]

7. Empty array:
   Input: []
   Expected Output: []

Here's the Python code to run these test cases:

```python
def sort_colors(nums):
    # Implementation will go here
    pass

def run_tests():
    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [0, 0, 1, 1, 2, 2],
        [2, 2, 1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 1],
        [1],
        []
    ]

    for i, case in enumerate(test_cases):
        original = case.copy()
        sort_colors(case)
        print(f"Test case {i + 1}:")
        print(f"Input:    {original}")
        print(f"Output:   {case}")
        print(f"Correct:  {sorted(original)}")
        print(f"Passed:   {case == sorted(original)}\n")

run_tests()
```

## Solutions

### Overview of solution approaches

#### Solutions worth learning

1. Three-pointer approach (Dutch National Flag algorithm)
2. Two-pointer approach
3. Counting sort
4. Bubble sort

Count: 4 solutions

#### Rejected solutions

1. Quick sort
2. Merge sort
3. Heap sort
4. Radix sort

### Worthy Solutions

#### Three-pointer approach (Dutch National Flag algorithm)

```python
from typing import List

def sort_colors(nums: List[int]) -> None:
    """
    Sort the array nums in-place.

    This implementation uses the Dutch National Flag algorithm,
    which partitions the array into three sections in a single pass.
    """
    # Initialize three pointers
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # Swap the current element with the element at the low pointer
            nums[low], nums[mid] = nums[mid], nums[low]
            # Increment both low and mid pointers
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # The element is already in the correct position, just move forward
            mid += 1
        else:  # nums[mid] == 2
            # Swap the current element with the element at the high pointer
            nums[mid], nums[high] = nums[high], nums[mid]
            # Decrement only the high pointer
            high -= 1

    # The array is now sorted in-place
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we're sorting in-place.

Key intuitions and invariants:

- The array is divided into four sections: [0, low) for 0s, [low, mid) for 1s, [mid, high] for unsorted elements, and (high, end] for 2s.
- The algorithm maintains these invariants throughout its execution.
- By using three pointers, we can sort the array in a single pass.

This solution is highly efficient and elegant, making it the best approach for this problem in an interview setting.

#### Two-pointer approach

```python
from typing import List

def sort_colors(nums: List[int]) -> None:
    """
    Sort the array nums in-place using a two-pointer approach.
    """
    # Initialize two pointers
    left, right = 0, len(nums) - 1

    i = 0
    while i <= right:
        if nums[i] == 0:
            # Swap 0 to the left side
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            # Swap 2 to the right side
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
            # Don't increment i here, as we need to check the swapped element
        else:
            # nums[i] == 1, leave it in place
            i += 1
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we're sorting in-place.

Key intuitions and invariants:

- The array is divided into three sections: [0, left) for 0s, [left, right] for 1s or unsorted elements, and (right, end] for 2s.
- We iterate through the array once, swapping 0s to the left and 2s to the right.
- The algorithm terminates when all elements have been processed.

This approach is similar to the three-pointer method but slightly less intuitive. It's still an excellent solution to know.

#### Counting sort

```python
from typing import List

def sort_colors(nums: List[int]) -> None:
    """
    Sort the array nums in-place using counting sort.
    """
    # Count occurrences of each color
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1

    # Overwrite the original array with sorted values
    index = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[index] = color
            index += 1
```

Time Complexity: O(n), where n is the length of the input array.
Space Complexity: O(1), as we're using a fixed-size count array.

Key intuitions and invariants:

- We can count the occurrences of each color in a single pass.
- Since we know the exact count of each color, we can reconstruct the sorted array in-place.
- This method is particularly efficient when the range of possible values is small and known.

While this solution is very efficient, it doesn't generalize well to other sorting problems, making it less valuable in an interview setting compared to the partition-based approaches.

#### Bubble sort

```python
from typing import List

def sort_colors(nums: List[int]) -> None:
    """
    Sort the array nums in-place using bubble sort.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
```

Time Complexity: O(n^2), where n is the length of the input array.
Space Complexity: O(1), as we're sorting in-place.

Key intuitions and invariants:

- In each iteration, the largest unsorted element "bubbles up" to its correct position.
- After i iterations, the last i elements are in their final sorted positions.

While this solution works, it's not optimal for this problem due to its quadratic time complexity. It's included here for completeness but would not be recommended in an interview setting for this particular problem.

### Rejected Approaches

1. Quick sort: While it's an efficient general-purpose sorting algorithm, it's overkill for this problem. The partitioning step of quicksort is similar to what we're doing in the Dutch National Flag algorithm, but quicksort would require multiple passes and doesn't take advantage of the limited range of values.

2. Merge sort: This would require additional space for merging, violating the in-place requirement. It also doesn't leverage the fact that we only have three distinct values.

3. Heap sort: While it sorts in-place, it's unnecessarily complex for this problem and doesn't take advantage of the limited range of values.

4. Radix sort: This is typically used for integers with multiple digits. For only three distinct values, it would be overkill and likely less efficient than the simpler counting sort or partition-based approaches.

### Final Recommendations

The Three-pointer approach (Dutch National Flag algorithm) is the best solution to learn and present in an interview. It's efficient (O(n) time complexity), sorts in-place (O(1) space complexity), and solves the problem in a single pass. Moreover, it demonstrates a deep understanding of the problem's constraints and how to leverage them for an optimal solution.

The Two-pointer approach is a close second and is also worth knowing. It's slightly less intuitive but still very efficient and demonstrates good problem-solving skills.

The Counting sort approach, while efficient for this specific problem, is less generalizable and doesn't demonstrate as much algorithmic thinking. However, it's still a valid solution and worth mentioning if time permits.

The Bubble sort approach, while correct, is not recommended for this problem due to its inefficiency. In an interview, using bubble sort for this problem might suggest a lack of understanding of more efficient sorting techniques or an inability to recognize when simpler, more specialized approaches are available.

Remember, in an interview setting, it's not just about solving the problem, but demonstrating your thought process and understanding of algorithmic efficiency. Start with the most optimal solution (Three-pointer approach) and be prepared to discuss trade-offs and alternatives if asked.

## Visualization(s)

To visualize the Three-pointer approach (Dutch National Flag algorithm), we can use ASCII art to represent the state of the array at each step:

```
Initial state:
[2, 0, 2, 1, 1, 0]
 L
 M
              H

Step 1 (swap 2 with 0):
[0, 0, 2, 1, 1, 2]
 L
 M
           H

Step 2 (move low and mid):
[0, 0, 2, 1, 1, 2]
    L
    M
        H

Step 3 (swap 2 with 1):
[0, 0, 1, 1, 2, 2]
    L
    M
     H

Step 4 (move mid):
[0, 0, 1, 1, 2, 2]
    L
      M
     H

Final state:
[0, 0, 1, 1, 2, 2]
    L
        M
     H
```

This visualization helps to understand how the three pointers (L for low, M for mid, H for high) move and partition the array into three sections: 0s, 1s, and 2s.
